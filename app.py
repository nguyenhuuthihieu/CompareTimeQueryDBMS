from flask import Flask, render_template, jsonify, redirect, url_for

from Mysql.MysqlConnect import mysqlConnect, restart_mysql
from ArangoDB.ArangoDBConnect import arangoDBConnect, restart_arangodb

from data import (
    select_mysql, select_arangodb,
    select2_arangodb, select2_mysql,
    sort_arangodb, sort_mysql,
    update_mysql, update_arangodb,
    delete_arangodb, delete_mysql,
    join_arangodb, join_mysql
)

app = Flask(__name__)
# select, #sort, update, delete, join


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/restart_dbms')
def restart():
    restart_mysql()
    restart_arangodb()
    return redirect(url_for('hello_world'))


# moi ham tra ve cau lenh va thoi gian thuc thi
@app.route('/mysql_select', methods=['POST'])
def mysql_select():
    output = []
    q = select_mysql
    result = mysqlConnect(q, 0)
    output.append(q)
    output.append(result[1])
    return jsonify(output)

@app.route('/arangodb_select', methods=['POST'])
def arangodb_select():
    output = []
    q = select_arangodb
    result = arangoDBConnect(q)
    output.append(q)
    output.append(result)
    return jsonify(output)

@app.route('/mysql_select2', methods=['POST'])
def mysql_select2():
    output = []
    q = select2_mysql
    result = mysqlConnect(q, 0)
    output.append(q)
    output.append(result[1])
    return jsonify(output)

@app.route('/arangodb_select2', methods=['POST'])
def arangodb_select2():
    output = []
    q = select2_arangodb
    result = arangoDBConnect(q)
    output.append(q)
    output.append(result)
    return jsonify(output)

@app.route('/mysql_sort', methods=['POST'])
def mysql_sort():
    output = []
    q = sort_mysql
    result = mysqlConnect(q, 0)#1
    output.append(q)
    output.append(result[1])
    return jsonify(output)

@app.route('/arangodb_sort', methods=['POST'])
def arangodb_sort():
    output = []
    q = sort_arangodb
    result = arangoDBConnect(q)
    output.append(q)
    output.append(result)
    return jsonify(output)

@app.route('/mysql_update', methods=['POST'])
def mysql_update():
    output = []
    q = update_mysql
    result = mysqlConnect(q, 0)#1
    output.append(q)
    output.append(result[1])
    return jsonify(output)

@app.route('/arangodb_update', methods=['POST'])
def arangodb_update():
    output = []
    q = update_arangodb
    result = arangoDBConnect(q)
    output.append(q)
    output.append(result)
    return jsonify(output)

@app.route('/mysql_delete', methods=['POST'])
def mysql_delete():
    output = []
    q = delete_mysql
    result = mysqlConnect(q, 0)#1
    output.append(q)
    output.append(result[1])
    return jsonify(output)

@app.route('/arangodb_delete', methods=['POST'])
def arangodb_delete():
    output = []
    q = delete_arangodb
    result = arangoDBConnect(q)
    output.append(q)
    output.append(result)
    return jsonify(output)

@app.route('/mysql_join', methods=['POST'])
def mysql_join():
    output = []
    q = join_mysql
    result = mysqlConnect(q, 0)
    output.append(q)
    output.append(result[1])
    return jsonify(output)

@app.route('/arangodb_join', methods=['POST'])
def arangodb_join():
    output = []
    q = join_arangodb
    result = arangoDBConnect(q)
    output.append(q)
    output.append(result)
    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True)
