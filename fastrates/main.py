import json
import sqlite3
from typing import Optional
import psycopg2
import os

import requests
from fastapi import FastAPI, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi_utils.tasks import repeat_every
from sqlalchemy import Column, Date, String, JSON
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Databases engine with Sqlalchemy
# SQLALCHEMY_DATABASE_URL = "sqlite:///sql_app.db"
SQLALCHEMY_DATABASE_URL = os.environ.get('DATABASE_URL')

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=True, autoflush=False, bind=engine)

Base = declarative_base()


# Database variables
#db = sqlite3.connect("sql_app.db")
db = psycopg2.connect(SQLALCHEMY_DATABASE_URL)
cursor = db.cursor()


# Database Model
class Currency(Base):
    __tablename__ = "currency"
    ticker = Column(String)
    date = Column(Date)
    rates = Column(JSONB, primary_key=True)


Base.metadata.create_all(bind=engine)


tags_metadata = [
        {
            "name": "Latest",
            "description": "Get the latest rates."
        },
        {
            "name": "Historical",
            "description": "Get historical rates"
        },
        {   "name": "Homepage",
            "description": "",
        }
]


# FastAPI
app = FastAPI(
    title="Fast Rates API",
    description="Free API service for currency rates",
    version="0.1.0",
    openapi_tags=tags_metadata,
)

# For static files
templates = Jinja2Templates(directory="fastrates/frontend/templates")
app.mount("/static", StaticFiles(directory="fastrates/frontend/static"), name="static")




# Tickers for updating database
tickers = ['USD', "EUR", "RUB", "CAD", 'PHP', 'DKK', 'HUF', 'CZK', 'AUD', 'RON', 'SEK', 'IDR',
           'INR', 'BRL', 'RUB', 'HRK', 'JPY', 'THB', 'CHF', 'SGD', 'PLN', 'BGN', 'TRY',
           'CNY', 'NOK', 'NZD', 'ZAR', 'MXN', 'ILS', 'GBP', 'KRW', 'MYR', 'CAD']



# Updates database
async def update_db(tick, preference):
    """
    Updates database asynchronously
    """
    if preference == "initial":
        from datetime import datetime
        today = datetime.today().strftime("%Y-%m-%d")
        r = requests.get(f"https://api.exchangeratesapi.io/history?start_at=2010-01-01&end_at={today}&base={tick}")
        data = r.json()

        try:
            for idx, d in enumerate(list(data["rates"])):
                date = list(data["rates"].keys())[idx]
                rates = data["rates"][date]
                cursor.execute("""
                INSERT INTO currency(ticker, date, rates)
                VALUES(%s, %s, %s)
                ON CONFLICT(rates)
                DO NOTHING""",((tick), (date), json.dumps(rates)))

                db.commit()
        except KeyError:
            pass

    if preference == "daily":
        r = requests.get(f"https://api.exchangeratesapi.io/latest?base={tick}")
        data = r.json()
        try:
            for d in data:
                date = data["date"]
                rates = data["rates"]
                ticker = tick
                cursor.execute("""
                INSERT INTO currency(ticker, date, rates)
                VALUES(%s, %s, %s) ON CONFLICT(rates)
                DO NOTHING""",((ticker), (date), json.dumps(rates)))
                db.commit()
        except KeyError:
            pass


@app.on_event("startup")
async def initial_updater():
    """
    Updates whole database for once
    """
    for tick in tickers:
        await update_db(tick, "initial")



@repeat_every(seconds=60 * 60 * 4)
async def daily_updater():
    """
    Updates database in every 4 hour
    """
    for tick in tickers:
        await update_db(tick, "daily")


@app.get("/historical", tags=["Historical"])
async def historical(base: Optional[str] = None, start_at: Optional[str] = None,
                     end_at: Optional[str] = None, symbols: Optional[str] = None, date: Optional[str] = None):


    if not base:
        base = "EUR"


    if date:
        try:
            currency = cursor.execute(f"""
            SELECT rates,date,ticker
            FROM currency
            WHERE ticker = %s
            AND date = %s """, (base, date,))
        except:
            raise HTTPException(status_code=404, detail="Invalid currency or invalid date")


    elif end_at and start_at and symbols:
        try:
            cur_symbols = symbols.split(",")
            currency = cursor.execute(f"""
            SELECT rates,date,ticker
            FROM currency
            WHERE ticker = (%s)
            AND date BETWEEN SYMMETRIC %s AND %s """, (base, start_at, end_at,))
            currency = cursor.fetchall()
            result = {}
            for i in currency:
                temp = {}
                for k,v in i[0].items():
                    print(i[1],{k:v})
                    if str(k) in cur_symbols:
                        temp.update({k:v})
                result.update({i[1]:temp})
                temp = {}
            if result == {}:
                raise HTTPException(status_code=404, detail="Invalid currency or invalid date")
            else:
                return {"rates": result, "base": base}
        except:
            raise HTTPException(status_code=404, detail="Invalid currency or invalid date")

    # End at & Start at
    elif end_at and start_at:
        try:
            currency = cursor.execute("""
            SELECT rates,date,ticker
            FROM currency
            WHERE ticker = (%s)
            AND date BETWEEN SYMMETRIC %s AND %s """, (base, start_at, end_at, ))
        except:
            raise HTTPException(status_code=404, detail="Invalid currency or invalid date")

    # Start at
    elif start_at:
        try:
            currency = cursor.execute(f"""
            SELECT rates,date,ticker
            FROM currency
            WHERE ticker = (%s)
            AND date > %s """,(base, start_at,))
        except:
            raise HTTPException(status_code=404, detail="Invalid currency or invalid date")

    # End at
    elif end_at:
        try:
            currency = cursor.execute(f"""
            SELECT rates,date,ticker
            FROM currency
            WHERE ticker = (%s)
            AND date < %s """, (base, end_at,))
        except:
            raise HTTPException(status_code=404, detail="Invalid currency or invalid date")


    """Fetchs data from database"""
    currency = cursor.fetchall()
    result = {}
    for idx, i in enumerate(currency):
        dates = currency[idx][1]
        rates = currency[idx][0]
        result.update({dates: rates})
    if result == {}:
        raise HTTPException(status_code=404, detail="Invalid currency or invalid date")
    else:
        return {"rates": result, "base": base}



# Latest
@app.get("/latest", tags=["Latest"])
async def latest(base: Optional[str] = None, symbols: Optional[str] = None):

    # Default base is EUR
    if not base:
        base = "EUR"

    # Symbols
    if symbols:
        cur_symbols = symbols.split(",")
        currency = cursor.execute(f"""
        SELECT rates,date,ticker
        FROM currency
        WHERE ticker = (%s)
        ORDER BY date DESC LIMIT 1;""", (base,))

        currency = cursor.fetchall()
        result = {}
        for i in currency:
            for k, v in i[0].items():
                if k in cur_symbols:
                    result.update({k: v})

        return {"rates": result, "base": base}

    currency = cursor.execute(f"""
    SELECT rates,date,ticker
    FROM currency
    WHERE ticker = (%s)
    ORDER BY date DESC LIMIT 1;""", (base,))

    """Fetchs data from database"""
    currency = cursor.fetchall()
    result = {}
    for idx, i in enumerate(currency):
        dates = currency[idx][1]
        rates = currency[idx][0]
        result.update({dates: rates})

    if result.values() == {}:
        raise HTTPException(status_code=404, detail="Invalid currency or invalid date")
    else:
        return {"rates": result, "base": base}


# Homepage
@app.get("/", tags=["Homepage"])
async def home(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})
