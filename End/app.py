from concurrent.futures.process import BrokenProcessPool
from email.policy import default
from flask import Flask
from flask.views import MethodView
from extension import db,cors
from models import User
from flask_cors import CORS
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite'
app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
CORS().init_app(app)
cors.init_app(app)

@app.cli.command()
def create():
    db.drop_all()
    db.create_all()
    User.init_db()

@app.route('/')
def hello_word():
    return 'Hello World!'

class UserApi(MethodView):
    def get(self):
        users: [User] = User.query.all()
        results = [
            {
                'id':user.id,
                'user_accountant':user.accountant,
                'user_password':user.password,
                'user_account':user.account,
                'user_telephone':user.telephone,
            }
         for user in users
        ]

        return {
            'status':'success',
            'message':'数据查询成功',
            'results':results
        }

user_view = UserApi.as_view('user_api')
app.add_url_rule('/users/',
                view_func=user_view,methods=['GET',])
    
if __name__ == '__main__':
    app.run(debug=True)