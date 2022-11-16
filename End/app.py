from flask import Flask,request,render_template
from sqlalchemy import create_engine
import pymysql as mysql
from flask_cors import *
from sqlalchemy import Column,String,Integer
from sqlalchemy.ext.declarative import declarative_base
import json
# HOSTNAME = '127.0.0.1'
# DATABASE = 'login'
# PORT = 3306
# USERNAME = 'root'
# PASSWORD = '13862720623hyy'
# DB_URL = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
# engine = create_engine(DB_URL)

# Base = declarative_base(engine)

# class User(Base):
#     #创建表结构操作
#     #表名
#     __tablename__ = "users"
#     id = Column(String(50),primary_key=True,nullable=False)
#     useraccount = Column(String(50),nullable = False)
#     userpassword= Column(String(50),nullable = False)
#     useremail = Column(String(50),nullable = False)
#     usertelephone = Column(String(50),nullable = False)

# Base.metadata.create_all()#映射到数据库


con = mysql.connect(user='root',password='13862720623hyy',db='login')
con.autocommit(True)
cur = con.cursor()#游标
app = Flask(__name__) #新建app
CORS(app,supports_credentials=True)

@app.errorhandler(500)
def server_error(error):
    return '出错,请重新尝试或联系客服'

@app.route('/')
def hello_word():
    return 'Hello World!'

@app.route("/users/")
def userlist():
    sql ="select * from users"
    cur.execute(sql)
    data = cur.fetchall()
    if data.__len__ != 0:
        dump_data = json.dumps(data)
        return dump_data
    else:
        return "no data"
    

@app.route("/delete/")
def delete():
    useraccount = request.args.get("useraccount")
    print(useraccount)
    sql = 'delete from users where useraccount="%s"'%(useraccount)
    print(sql)
    cur.execute(sql)
    return "ok"

@app.route('/add/',methods=['POST'])
def add():
    id = request.form.get('id')
    useraccount = request.form.get('useraccount')
    userpassword = request.form.get('userpassword')
    useremail = request.form.get("useremail")
    usertelephone = request.form.get('usertelephone')
    print(id)
    sql = 'insert into users values("%s","%s","%s","%s","%s")' %(id,useraccount,userpassword,useremail,usertelephone)
    print(sql)
    cur.execute(sql)
    return "ok"



# class UserApi(MethodView):
#     def get(self,user_id):
#         if not user_id:
#             users: [User] = User.query.all()
#             results = [
#                 {
#                     'id':user.id,
#                     'user_accountant':user.accountant,
#                     'user_password':user.password,
#                     'user_account':user.account,
#                     'user_telephone':user.telephone,
#                 }for user in users
#             ]
#             return{
#                 'status':'success',
#                 'message':'数据查询成功',
#                 'results':results
#             }
#         user: User = User.query.get(user_id)
#         return {
#             'status':'success',
#             'message':'数据查询成功',
#             'result':{
#                 'id':user.id,
#                 'user_accountant':user.accountant,
#                 'user_password':user.password,
#                 'user_account':user.account,
#                 'user_telephone':user.telephone,
#             }
#         }

#     def post(self):
#         form = request.json
#         user = User()
#         user.user_accountant = form.get('user_accountant')
#         user.user_password = form.get('user_password')
#         user.user_account = form.get('user_account')
#         user.user_telephone = form.get('user_telephone')
#         db.session.add(user)
#         db.session.commit()

#         return {
#             'status':'success',
#             'message':'数据添加成功'
#         }

#     def delete(self,user_id):
#         user = User.query.get(user_id)
#         db.session.delete(user)
#         db.session.commit()
#         return {
#             'status':'success',
#             'message':'数据删除成功'
#         }
    
#     def put(self,user_id):
#         user: User = User.query.get(user_id)
#         user.accountant = request.json.get('user_accountant')
#         user.password = request.json.get('user_password')
#         user.account = request.json.get('user_account')
#         user.telephone = request.json.get('user_telephone')
#         db.session.commit()
#         return {
#             'status':'success',
#             'message':'数据修改成功'
#         }


# user_view = UserApi.as_view('user_api')
# app.add_url_rule('/users/',defaults = {'user_id':None},
#                 view_func=user_view,methods=['GET',  ])
# app.add_url_rule('/users/',view_func=user_view,methods=['POST',])
# app.add_url_rule('/users/<int:user_id>',view_func=user_view,methods=['GET', 'PUT', 'DELETE'])

# if __name__ == '__main__':
#     app.debug = True
#     app.run(debug=True)