from pickle import FALSE
from extension import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    accountant = db.Column(db.String(255),nullable=False)
    password = db.Column(db.String(255),nullable=False)
    account = db.Column(db.String(255),nullable = False)
    telephone = db.Column(db.String(255),nullable = False)

    @staticmethod
    def init_db():
        rets = [
            (1,'001','hyy','123456','3206212000','13862720091'),
            (2,'002','wj','123456','32172890192','1382941821'),
        ]
        for ret in rets:
            user =User()
            user.id = ret[0]
            user.accountant = ret[1]
            user.password = ret[2]
            user.account = ret[3]
            user.telephone = ret[4]
            db.session.add(user)
        db.session.commit()