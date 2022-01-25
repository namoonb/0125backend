from flask import Flask, jsonify
from flask_cors import CORS

# 각 화면 import
from functions import Test

# 실행 객체
app = Flask(__name__)
#CORS(app)
CORS(app, resources={r"/*": {"origins": "*"}})

# 환경 설정
app.config['MONGO_DBNAME'] = 'test'
#app.config['MONGO_URI'] = 'mongodb://localhost:27017/test'
app.config['MONGO_URI'] = 'mongodb+srv://calendar:start2021%21%40%23%2A@calendar.r0sdd.mongodb.net/test'
app.config['JSON_AS_ASCII'] = False

# DB
from functions.Database import mongo
mongo.init_app(app)

# --------------------------------- [edit] ---------------------------------- #    
app.register_blueprint(Test.bp)
# --------------------------------------------------------------------------- #    

# flask 실행
if __name__ == '__main__':
    app.run(debug=True)
