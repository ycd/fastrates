from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_main_home():
    response = client.get("/")
    assert response.status_code == 200


def test_latest():
    response = client.get("/latest")
    assert response.status_code == 200


def test_latest():
    response = client.get("/latest?base=USD")
    assert response.status_code == 200


def test_latest_symbols():
    response = client.get("/latest?symbols=USD,TRY")
    assert response.status_code == 200


def test_historical_date():
    response = client.get("/historical?date=2010-01-18")
    assert response.status_code == 200
    assert response.json() == {
                               "rates":{
                                  "2010-01-18":{
                                     "AUD":1.5511,
                                     "BGN":1.9558,
                                     "BRL":2.5505,
                                     "CAD":1.4741,
                                     "CHF":1.4745,
                                     "CNY":9.8097,
                                     "CZK":25.889,
                                     "DKK":7.4418,
                                     "EEK":15.6466,
                                     "GBP":0.8795,
                                     "HKD":11.1529,
                                     "HRK":7.2893,
                                     "HUF":267.75,
                                     "IDR":13268.3,
                                     "INR":65.408,
                                     "JPY":130.33,
                                     "KRW":1616.18,
                                     "LTL":3.4528,
                                     "LVL":0.7085,
                                     "MXN":18.2228,
                                     "MYR":4.8014,
                                     "NOK":8.1435,
                                     "NZD":1.9456,
                                     "PHP":65.957,
                                     "PLN":4.0227,
                                     "RON":4.1053,
                                     "RUB":42.538,
                                     "SEK":10.1295,
                                     "SGD":1.9965,
                                     "THB":47.202,
                                     "TRY":2.0854,
                                     "USD":1.4369,
                                     "ZAR":10.6356
                                  }
                               },
                               "base":"EUR"
                            }


def test_latest_symbols():
    response = client.get("/latest?symbols=USD,TRY")
    assert response.status_code == 200

def test_end_at():
    response = client.get("")
    assert response.status_code == 200
    assert response.json() == {
                               "rates":{
                                  "2010-01-04":{
                                     "AUD":1.1039683091,
                                     "BGN":1.3592327472,
                                     "BRL":1.7316700257,
                                     "CAD":1.0391966085,
                                     "CHF":1.0336368059,
                                     "CNY":6.8272986309,
                                     "CZK":18.2674265064,
                                     "DKK":5.1716589061,
                                     "EEK":10.874000973,
                                     "EUR":0.6949753284,
                                     "GBP":0.6195010077,
                                     "HKD":7.7564806449,
                                     "HRK":5.068872055,
                                     "HUF":187.5390923622,
                                     "IDR":9411.779831816,
                                     "INR":46.2999513517,
                                     "JPY":92.8626033776,
                                     "KRW":1155.3061366321,
                                     "LTL":2.3996108138,
                                     "LVL":0.4929460004,
                                     "MXN":12.9726874696,
                                     "MYR":3.3975258878,
                                     "NOK":5.7189519772,
                                     "NZD":1.373549239,
                                     "PHP":45.9378692056,
                                     "PLN":2.8514837723,
                                     "RON":2.936479255,
                                     "RUB":29.9951351727,
                                     "SEK":7.0838835221,
                                     "SGD":1.3987073459,
                                     "THB":33.2052262145,
                                     "TRY":1.4880116756,
                                     "USD":1.0,
                                     "ZAR":7.3401904232
                                  }
                               },
                               "base":"USD"
                            }
