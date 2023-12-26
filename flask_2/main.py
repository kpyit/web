import os 
import sys
import click
from flask_migrate import Migrate, upgrade
from app import create_app, db 
from app.models import (User, Follow, Role, Permission, Post, Comment)
# добавление фейковых пользователей через shell
from app.fake_data import Fake_data

app = create_app() 
# Для доступа из консоли
# нормально заработало только после добавления .flaskenv  https://stackoverflow.com/questions/71354617
@app.shell_context_processor
def make_shell_context():
    # return dict(db=db, User=User, Follow=Follow, Role=Role,
    #             Permission=Permission, Post=Post, Comment=Comment, 
    #             Fake_data=Fake_data)
    return {
        "db":db,
        "User":User,
        "Follow":Follow, 
        "Role":Role,
        "Permission":Permission, 
        "Post":Post, 
        "Comment":Comment, 
        "Fake_data":Fake_data}



# Консольная команда  - flask init-db
@app.cli.command('init-db')
def deploy_db():
    """Run deployment tasks."""
    # migrate database to latest revision
    # upgrade()
    # create or update user roles
    Role.insert_roles()

    # ensure all users are following themselves
    User.add_self_follows()
    
# в окружении  через миграцию    
# flask db init
# flask db migrate -m "Initial migration."
# flask db upgrade

# set FLASK_APP=app.py
# flask shell
# >>> 
# >>> Role.insert_roles()
# >>> Fake_data.fake_users(20) 
