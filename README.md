<img src="https://lh3.googleusercontent.com/l2fY_lURi_e8DZDBTiQDthVbg2uEtbMrFZkh7h1mk2QGHoE4oU2yNcgGbOwX05nQYzJSplD5zdVc9Te1YZWm1j6Fi6DeHkjEzznFPBh-vheedQ7fuUeCOJbzFZXqnnMoMxFbFs8-Bs8DUFCtdAT7xkgUHU6t_VLMliM1dR-TZzYWQKOOvS_c6Yo7AycUcsgHa6SOpEJRd7udLcW4zzFJc5kLbUf43MB1SjUY-fagPfeyoFZOcVsQUepTngDimJBHxSBZmJa6iCWD6-80SDvWf8lljDo9QaeYZ_6ma5ABX0afnG9OUPSlCFZ2hvqoUJVqB_D-uRBrKCfwYXu2V10_QSYNT-Lf1y7yTM2ZaoowKZnZnieTaLMQ-5BxBxg1H0w3N1N1v1kYRDfq8L_6QHwDWLXtNOuKnIdYOQNSSRbV3zG-Vyl3pBhmg1QVy76HKNRDL9LWsmkWhoAJgXFTblOIftHdBSeYr__y1bK8csjR8lpABSNeb4BIpeOftkh4OJHuqjdiFuuOwePHjEZDvuKTPyXEs53CKnopJ-ktOJIhGniGc887B7Jlp97atpeGr1mYCGt8H5icznCjZymMLTHoz9K8F5EdRONfAtzvZDuCHrG1Er0qonyz0C1zC2Tni8gwapt4V59wEc7oXL95Jf6RK0_l2CKTrez8Yc-QWU4mvBbGp-fCwq574pMfue1Q=w500-h167-no?authuser=0" width=500>

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


