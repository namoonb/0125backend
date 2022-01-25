#가장 기초적인 화면
from flask import Blueprint, jsonify, request
from .Database import mongo
#from flask_cors import cross_origin
#@cross_origin()

bp = Blueprint('caltest', __name__, url_prefix='/')

# ----------------------------------------------------------------------
@bp.route("/select", methods=["GET"])
def select_test():
    # DB 연결
    db_test = mongo.db.test

    # select
    result = []
    for i in db_test.find():
        print(i)
        result.append({'data':i['data'], 'number':i['number']})
    
    # 디버깅용
    #print(result)

    return jsonify({'results':result})

'''
테스트용 데이터

[
  {
    "data": "Hello, World!", 
    "number": "1"
  }, 
  {
    "data": "Bye, World!", 
    "number": "2"
  }
]
'''

# ----------------------------------------------------------------------
@bp.route("/insert", methods=["POST"])
def insert_test():
    # DB 연결 여부 확인용
    db_test = mongo.db.test

    # Auto count 'number'
    number = 1
    for i in db_test.find():
        number += 1
    print(number)
    
    # form data 받아오기
    result = request.get_json()
    data = result['data']

    db_test.insert({
        'data' : data,
        'number' : str(number)
    })
    
    return jsonify({'results':'insert success'})

    # insert



# ----------------------------------------------------------------------
@bp.route("/update", methods=["POST"])
def update_test():
    # DB 연결 여부 확인용
    db_test = mongo.db.test

    # form data 받아오기
    data = request.get_json()

    db_test.update({'number': data['number']}
                  , {'$set' : { 'data' : data['data']}})

    # 디버깅용
    print(db_test.find_one({'number':data['number']}))
    
    return jsonify({'results':'update success'})

    # update


# ----------------------------------------------------------------------
@bp.route("/delete", methods=["POST"])
def delete_test():
    # DB 연결 여부 확인용
    db_test = mongo.db.test

    # form data 받아오기
    data = request.get_json()

    # delete_one(), remove()
    db_test.delete_one({'number':data['number']})
    
    return jsonify({'results':'delete success'})

    # delete
