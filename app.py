from flask import Flask, render_template, jsonify

from Mysql.MysqlConnect import mysqlConnect
from ArangoDB.ArangoDBConnect import arangoDBConnect

from data import (
    select_mysql,
    select_arangodb
)

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/mysql_select', methods=['POST'])
def mysql_select():
    output = []
    q = select_mysql
    result = mysqlConnect(q, 1)
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





if __name__ == '__main__':
    app.run(debug=True)
