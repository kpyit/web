# -*- coding: utf-8 -*-
# в студии чтобы выбрать созданный интерпритатор Ctrl+Shift+P
# conda install -n Flask -c conda-forge redis
#    redis              pkgs/main/noarch::redis-3.5.3-pyhd3eb1b0_0
# conda install -n Flask -c conda-forge arrow
#    arrow              conda-forge/noarch::arrow-1.3.0-pyhd8ed1ab_0
# conda install -n Flask -c conda-forge flask_bcrypt
# conda install -n Flask -c conda-forge flask-bcrypt
#    bcrypt             conda-forge/win-64::bcrypt-3.2.0-py310he2412df_3
# conda install -n Flask -c conda-forge flask-bootstrap
# обновить коду пришлось    conda update -n base -c defaults conda
# conda install -n Flask -c conda-forge flask-debugtoolbar
#    cryptography-41.0.7        |  py310hb1f9477_1         1.0 MB  conda-forge
# conda install   -c conda-forge flask-sqlalchemy
# conda update -n Flask flask-sqlalchemy
# conda install -n Flask -c conda-forge pluggy
#    pluggy-1.3.0               |     pyhd8ed1ab_0          22 KB  conda-forge
# conda install -n Flask -c auto alipay
#  не найден и закоментированн весь рабочий код
# conda install -n Flask -c conda-forge libgravatar
#  не ставится
# conda install -n Flask -c conda-forge phonenumbers
#  phonenumbers-8.13.26       |     pyhd8ed1ab_0         1.4 MB  conda-forge
# conda install -n Flask -c conda-forge elasticsearch
#   elastic-transport-8.10.0   |     pyhd8ed1ab_0          42 KB  conda-forge
# conda install -n Flask -c conda-forge elasticsearch-dsl
#    elasticsearch-dsl-8.11.0   |  py310h5588dad_0          95 KB  conda-forge
# conda install -n Flask -c conda-forge faker
#    faker-20.1.0               |     pyhd8ed1ab_0         1.3 MB  conda-forge

# поставил ругался на данные >pip install -U bootstrap-flask
#заработали формы
"""Create an application instance."""
from flaskshop.app import create_app

app = create_app()
 


 
 