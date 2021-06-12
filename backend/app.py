from flask import Flask, request
import pymysql
import json

#连接数据库
from flask_cors import CORS

conn=pymysql.connect(host=''
,user = '' # 用户名
,passwd='' # 密码
,port= 3306 # 端口，默认为3306
,db='' # 数据库名称
,charset='utf8' # 字符编码
)

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/login')
def login():
    a = request
    if request.args["username"] and request.args["password"]:
        if request.args["username"] == "admin" and request.args["password"] == "123456":
            result = {"msg": "ok", "code": 200, "user": "Admin"}
            return json.dumps(result)
    else:
        result = {"msg": "wrong", "code": 202, "user": "Admin"}
        return json.dumps(result)

@app.route('/user/list')
def getUserList():
    conn.ping(reconnect=True)
    try:
        cur = conn.cursor()  # 生成游标对象
        if request.args['name']:
            sql = "select * from `user` where real_name=\"" + request.args['name'] +"\""
        else:
            sql = "select * from `user` "  # SQL语句
        users = []
        cur.execute(sql)  # 执行SQL语句
        data = cur.fetchall()  # 通过fetchall方法获得数据
        for each in data:  # 打印输出所有数据
            user={'id':each[0], 'nick':each[1], 'name':each[2], 'campus':each[3], 'college':each[4], 'major':each[5], 'grade':each[6]}
            users.append(user)
    finally:
        cur.close()  # 关闭游标
        conn.close()  # 关闭连接
        return json.dumps(users)

@app.route('/user/filter')
def getUserFilter():
    conn.ping(reconnect=True)
    users = []
    cur = conn.cursor()  # 生成游标对象
    try:
        sql = "select * from `user` where user_id=" + request.args['id']
        cur.execute(sql)  # 执行SQL语句
        data = cur.fetchall()  # 通过fetchall方法获得数据
        for each in data:  # 打印输出所有数据
            user = {'id': each[0], 'nick': each[1], 'name': each[2], 'campus': each[3], 'college': each[4],
                    'major': each[5], 'grade': each[6]}
            users.append(user)
        cur.close()  # 关闭游标
    except:
        sql = "select * from `user` "  # SQL语句
        cur.execute(sql)  # 执行SQL语句
        data = cur.fetchall()  # 通过fetchall方法获得数据
        for each in data:  # 打印输出所有数据
            user = {'id': each[0], 'nick': each[1], 'name': each[2], 'campus': each[3], 'college': each[4],
                    'major': each[5], 'grade': each[6]}
            users.append(user)
        cur.close()  # 关闭游标
    try:
        conn.close()  # 关闭连接
    finally:
        return json.dumps(users)

@app.route('/goods/list')
def getGoodsList():
    a = request
    conn.ping(reconnect=True)
    cur = conn.cursor()  # 生成游标对象
    result = json.dumps([])
    try:
        sql = "select * from `Good` where sellerid=" + request.args['id']
        goods = []
        cur.execute(sql)  # 执行SQL语句
        data = cur.fetchall()  # 通过fetchall方法获得数据
        for each in data:  # 打印输出所有数据
            good = {'goodid': each[0], 'name': each[1], 'price': each[2], 'description': each[3], 'campus': each[4],
                    'old': each[5], "sellerid": each[7], "publishdate": str(each[8]), "tag": each[9],
                    "sold_out": each[10]}
            goods.append(good)
        result = json.dumps(goods)
    except:
        sql = "select * from `Good` "  # SQL语句
        goods = []
        cur.execute(sql)  # 执行SQL语句
        data = cur.fetchall()  # 通过fetchall方法获得数据
        for each in data:  # 打印输出所有数据
            good={'goodid':each[0], 'name':each[1], 'price':each[2], 'description':each[3], 'campus':each[4],
                  'old':each[5], "sellerid":each[7], "publishdate":str(each[8]), "tag":each[9],
                  "sold_out":each[10]}
            goods.append(good)
        result = json.dumps(goods)
    finally:
        cur.close()  # 关闭游标
        conn.close()  # 关闭连接
        return result

@app.route('/goods/filter')
def getGoodsFilter():
    a = request
    conn.ping(reconnect=True)
    cur = conn.cursor()  # 生成游标对象
    result = json.dumps([])
    try:
        sql = "select * from `Good` where description LIKE \"%" + request.args['filter'] + "%\" or name LIKE \"%" + request.args['filter'] + "%\""
        goods = []
        cur.execute(sql)  # 执行SQL语句
        data = cur.fetchall()  # 通过fetchall方法获得数据
        for each in data:  # 打印输出所有数据
            good = {'goodid': each[0], 'name': each[1], 'price': each[2], 'description': each[3], 'campus': each[4],
                    'old': each[5], "sellerid": each[7], "publishdate": str(each[8]), "tag": each[9],
                    "sold_out": each[10]}
            goods.append(good)
        result = json.dumps(goods)
    except:
        sql = "select * from `Good` "  # SQL语句
        goods = []
        cur.execute(sql)  # 执行SQL语句
        data = cur.fetchall()  # 通过fetchall方法获得数据
        for each in data:  # 打印输出所有数据
            good={'goodid':each[0], 'name':each[1], 'price':each[2], 'description':each[3], 'campus':each[4],
                  'old':each[5], "sellerid":each[7], "publishdate":str(each[8]), "tag":each[9],
                  "sold_out":each[10]}
            goods.append(good)
        result = json.dumps(goods)
    finally:
        cur.close()  # 关闭游标
        conn.close()  # 关闭连接
        return result

@app.route('/qiugou/list')
def getQiugouList():
    a = request
    conn.ping(reconnect=True)
    cur = conn.cursor()  # 生成游标对象
    result = []
    try:
        sql = "select * from `AskForGoodPost` where user_id=" + request.args['id']
        cur.execute(sql)  # 执行SQL语句
        data = cur.fetchall()  # 通过fetchall方法获得数据
        for each in data:  # 打印输出所有数据
            qiugou = {'postid': each[0], 'userid': each[1], 'intro': each[2], 'title': each[3], 'tag': each[4],
                    'campus': each[5], "price": str(each[6]), "condition": each[7], "time": str(each[8])}
            result.append(qiugou)
    except:
        sql = "select * from `AskForGoodPost` "  # SQL语句
        cur.execute(sql)  # 执行SQL语句
        data = cur.fetchall()  # 通过fetchall方法获得数据
        for each in data:  # 打印输出所有数据
            qiugou = {'postid': each[0], 'userid': each[1], 'intro': each[2], 'title': each[3], 'tag': each[4],
                      'campus': each[5], "price": str(each[6]), "condition": each[7], "time": str(each[8])}
            result.append(qiugou)
    finally:
        cur.close()  # 关闭游标
        conn.close()  # 关闭连接
        return json.dumps(result)

@app.route('/qiugou/filter')
def getQiugouFilter():
    a = request
    conn.ping(reconnect=True)
    cur = conn.cursor()  # 生成游标对象
    result = []
    try:
        sql = "select * from `AskForGoodPost` where afg_intro LIKE \"%" + request.args['filter'] + "%\" or afg_title LIKE \"%" + request.args['filter'] + "%\""
        cur.execute(sql)  # 执行SQL语句
        data = cur.fetchall()  # 通过fetchall方法获得数据
        for each in data:  # 打印输出所有数据
            qiugou = {'postid': each[0], 'userid': each[1], 'intro': each[2], 'title': each[3], 'tag': each[4],
                    'campus': each[5], "price": str(each[6]), "condition": each[7], "time": str(each[8])}
            result.append(qiugou)
    except:
        sql = "select * from `AskForGoodPost` "  # SQL语句
        cur.execute(sql)  # 执行SQL语句
        data = cur.fetchall()  # 通过fetchall方法获得数据
        for each in data:  # 打印输出所有数据
            qiugou = {'postid': each[0], 'userid': each[1], 'intro': each[2], 'title': each[3], 'tag': each[4],
                      'campus': each[5], "price": str(each[6]), "condition": each[7], "time": str(each[8])}
            result.append(qiugou)
    finally:
        cur.close()  # 关闭游标
        conn.close()  # 关闭连接
        return json.dumps(result)

@app.route('/question/list')
def getQuestionlist():
    a = request
    conn.ping(reconnect=True)
    cur = conn.cursor()  # 生成游标对象
    result = []
    try:
        sql = "select * from `QuestionPost` where user_id=" + request.args['id']
        cur.execute(sql)  # 执行SQL语句
        data = cur.fetchall()  # 通过fetchall方法获得数据
        for each in data:  # 打印输出所有数据
            question = {'postid': each[0], 'userid': each[1], 'content': each[2], 'title': each[3], "time": str(each[4])}
            result.append(question)
    except:
        sql = "select * from `QuestionPost` "  # SQL语句
        cur.execute(sql)  # 执行SQL语句
        data = cur.fetchall()  # 通过fetchall方法获得数据
        for each in data:  # 打印输出所有数据
            question = {'postid': each[0], 'userid': each[1], 'content': each[2], 'title': each[3],
                        "time": str(each[4])}
            result.append(question)
    finally:
        cur.close()  # 关闭游标
        conn.close()  # 关闭连接
        return json.dumps(result)

@app.route('/question/filter')
def getQuestionfilter():
    a = request
    conn.ping(reconnect=True)
    cur = conn.cursor()  # 生成游标对象
    result = []
    try:
        sql = "select * from `QuestionPost` where q_content LIKE \"%" + request.args['filter'] + "%\" or q_title LIKE \"%" + request.args['filter'] + "%\""
        cur.execute(sql)  # 执行SQL语句
        data = cur.fetchall()  # 通过fetchall方法获得数据
        for each in data:  # 打印输出所有数据
            question = {'postid': each[0], 'userid': each[1], 'content': each[2], 'title': each[3], "time": str(each[4])}
            result.append(question)
    except:
        sql = "select * from `QuestionPost` "  # SQL语句
        cur.execute(sql)  # 执行SQL语句
        data = cur.fetchall()  # 通过fetchall方法获得数据
        for each in data:  # 打印输出所有数据
            question = {'postid': each[0], 'userid': each[1], 'content': each[2], 'title': each[3],
                        "time": str(each[4])}
            result.append(question)
    finally:
        cur.close()  # 关闭游标
        conn.close()  # 关闭连接
        return json.dumps(result)

@app.route('/recommend/list')
def getRecommend():
    a = request
    conn.ping(reconnect=True)
    cur = conn.cursor()  # 生成游标对象
    result = []
    try:
        sql = "select * from `RecommendGoodsPost` where user_id=" + request.args['id']
        cur.execute(sql)  # 执行SQL语句
        data = cur.fetchall()  # 通过fetchall方法获得数据
        for each in data:  # 打印输出所有数据
            recommend = {'postid': each[0], 'userid': each[1], 'content': each[2], 'title': each[3], "tag": each[4], "time": str(each[5])}
            result.append(recommend)
    except:
        sql = "select * from `RecommendGoodsPost` "  # SQL语句
        cur.execute(sql)  # 执行SQL语句
        data = cur.fetchall()  # 通过fetchall方法获得数据
        for each in data:  # 打印输出所有数据
            recommend = {'postid': each[0], 'userid': each[1], 'content': each[2], 'title': each[3], "tag": each[4],
                         "time": str(each[5])}
            result.append(recommend)
    finally:
        cur.close()  # 关闭游标
        conn.close()  # 关闭连接
        return json.dumps(result)

@app.route('/recommend/filter')
def getRecommendFilter():
    a = request
    conn.ping(reconnect=True)
    cur = conn.cursor()  # 生成游标对象
    result = []
    try:
        sql = "select * from `RecommendGoodsPost` where rg_intro LIKE \"%" + request.args['filter'] + "%\" or rg_title LIKE \"%" + request.args['filter'] + "%\""
        cur.execute(sql)  # 执行SQL语句
        data = cur.fetchall()  # 通过fetchall方法获得数据
        for each in data:  # 打印输出所有数据
            recommend = {'postid': each[0], 'userid': each[1], 'content': each[2], 'title': each[3], "tag": each[4], "time": str(each[5])}
            result.append(recommend)
    except:
        sql = "select * from `RecommendGoodsPost` "  # SQL语句
        cur.execute(sql)  # 执行SQL语句
        data = cur.fetchall()  # 通过fetchall方法获得数据
        for each in data:  # 打印输出所有数据
            recommend = {'postid': each[0], 'userid': each[1], 'content': each[2], 'title': each[3], "tag": each[4],
                         "time": str(each[5])}
            result.append(recommend)
    finally:
        cur.close()  # 关闭游标
        conn.close()  # 关闭连接
        return json.dumps(result)

@app.route('/user/remove')
def deleteUsers():
    conn.ping(reconnect=True)
    cur = conn.cursor()  # 生成游标对象
    try:
        sql = "DELETE FROM `user` WHERE user_id=" + request.args['id']
        cur.execute(sql)  # 执行SQL语句
        conn.commit()
    finally:
        cur.close()  # 关闭游标
        conn.close()  # 关闭连接
        return "ok"

@app.route('/user/edit')
def editUser():
    a = request
    conn.ping(reconnect=True)
    cur = conn.cursor()  # 生成游标对象
    try:
        sql = "update `user` set nick_name=\"" + request.args["nick"] + "\",campus=" + request.args["campus"] + " WHERE user_id=" + request.args['id']
        cur.execute(sql)  # 执行SQL语句
        conn.commit()
    finally:
        cur.close()  # 关闭游标
        conn.close()  # 关闭连接
    return "ok"

@app.route('/good/remove')
def deleteGoods():
    a = request
    conn.ping(reconnect=True)
    cur = conn.cursor()  # 生成游标对象
    try:
        sql = "DELETE FROM `Good` WHERE goodid=" + request.args['id']
        cur.execute(sql)  # 执行SQL语句
        conn.commit()
    finally:
        cur.close()  # 关闭游标
        conn.close()  # 关闭连接
        return "ok"

@app.route('/qiugou/remove')
def deleteQiugous():
    a = request
    conn.ping(reconnect=True)
    cur = conn.cursor()  # 生成游标对象
    try:
        sql = "DELETE FROM `AskForGoodPost` WHERE afg_post_id=" + request.args['id']
        cur.execute(sql)  # 执行SQL语句
        conn.commit()
    finally:
        cur.close()  # 关闭游标
        conn.close()  # 关闭连接
        return "ok"

@app.route('/question/remove')
def deleteQuestions():
    a = request
    conn.ping(reconnect=True)
    cur = conn.cursor()  # 生成游标对象
    try:
        sql = "DELETE FROM `QuestionPost` WHERE q_post_id=" + request.args['id']
        cur.execute(sql)  # 执行SQL语句
        conn.commit()
    finally:
        cur.close()  # 关闭游标
        conn.close()  # 关闭连接
        return "ok"

@app.route('/recommend/remove')
def deleteRecommends():
    a = request
    conn.ping(reconnect=True)
    cur = conn.cursor()  # 生成游标对象
    try:
        sql = "DELETE FROM `RecommendGoodsPost` WHERE rg_post_id=" + request.args['id']
        cur.execute(sql)  # 执行SQL语句
        conn.commit()
    finally:
        cur.close()  # 关闭游标
        conn.close()  # 关闭连接
        return "ok"

if __name__ == '__main__':
    app.run(host="localhost", port=5015)
