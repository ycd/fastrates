<img src="https://github.com/ycd/fastrates/blob/master/fastrates/frontend/static/logo.png" width=500>

![](https://img.shields.io/github/forks/ycd/fastrates?style=for-the-badge)
![](https://img.shields.io/github/stars/ycd/fastrates?style=for-the-badge)
![](https://img.shields.io/github/issues/ycd/fastrates?style=for-the-badge)
![](https://img.shields.io/bitbucket/pr-raw/ycd/fastrates?style=for-the-badge)
![](https://img.shields.io/github/license/ycd/fastrates?style=for-the-badge)


## Give it a try! :triangular_flag_on_post:

You can give it a try [online](https://fastrates.herokuapp.com/) or you can run it locally with Sqlite3 support.


## Installation :pushpin:
```shell
git clone https://github.com/ycd/fastrates.git
cd fastrates
virtualenv env
source env/bin/activate
pip install -r requirements.txt
uvicorn sqlite_main:app --reload
```


## Features :rocket:

* **Production ready**  You can deploy it to the heroku in a few minutes with Postgresql support.
* **Python <a href="https://github.com/tiangolo/fastapi" class="external-link" target="_blank">**FastAPI**</a> backend.**
* **SQLAlchemy** models
* **Asynchronous** Thanks to Uvicorn Fast Rates comes with a lightning-fast ASGI server,
* **Open source** Everything from the code base is opensource and free to use under a permissive MIT license.

## Contributing :heavy_check_mark:
All pull requests are welcome from developers of all skill levels. To get started, simply fork the master branch on GitHub to your personal account and then clone the fork into your development environment. 

## Release Notes :mega:

### Latest Changes

### 0.1.0

* Prototype of project with small database support.


## License

This project is licensed under the terms of the MIT license.


