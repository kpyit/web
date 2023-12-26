from random import randint
from sqlalchemy.exc import IntegrityError
from faker import Faker
from . import db
from .models import User, Post

class Fake_data():
    #Заполнение базы псевдо данными с помощь модуля Faker
    @staticmethod
    def fake_users(count=100):
        fake = Faker()
        i = 0
        while i < count:
            u = User(email=fake.email(),
                    username=fake.user_name(),
                    password='password',
                    confirmed=True,
                    name=fake.name(),
                    location=fake.city(),
                    about_me=fake.text(),
                    member_since=fake.past_date())
            db.session.add(u)
            try:
                db.session.commit()
                i += 1
            except IntegrityError:
                db.session.rollback()

    @staticmethod
    def fake_posts(count=100):
        fake = Faker()
        user_count = User.query.count()
        for i in range(count):
            u = User.query.offset(randint(0, user_count - 1)).first()
            p = Post(body=fake.text(),
                    timestamp=fake.past_date(),
                    author=u)
            db.session.add(p)
        db.session.commit()

    def __repr__(self):
        return '<Fake %r>' % self.name