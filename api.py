from flask import Flask, jsonify
from sqlalchemy import create_engine
from datetime import datetime
from flask_restx import Api, Namespace, Resource, \
    reqparse, inputs, fields

# user = "root"
# passw = "CapstoneIsTheVeryBestThing2023__"
# host = "34.175.214.128"
# database = "capstone-db"

user = "root"
passw = "pikachu123"
host = "34.175.191.144"
database = "main"

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = host

api = Api(app, version = '1.0',
    title = 'The famous REST API with FLASK!',
    description = """
        This RESTS API is an API to built with FLASK
        and FLASK-RESTX libraries
        """,
    contact = "gabriela.endros@student.ie.edu",
    endpoint = "/api/v1"
)

def connect():
    db = create_engine(
    'mysql+pymysql://{0}:{1}@{2}/{3}' \
        .format(user, passw, host, database), \
    connect_args = {'connect_timeout': 10})
    conn = db.connect()
    return conn

def disconnect(conn):
    conn.close()

customers = Namespace('customers',
    description = 'All operations related to customers',
    path='/api/v1')
api.add_namespace(customers)

@customers.route("/customers")
class get_all_users(Resource):

    def get(self):
        conn = connect()
        select = """
            SELECT *
            FROM customers
           """
        result = conn.execute(select).fetchall()
        disconnect(conn)
        return jsonify({'result': [dict(row) for row in result]})

@customers.route("/customers/<string:id>")
@customers.doc(params = {'id': 'The ID of the user'})
class select_user(Resource):

    @api.response(404, "CUSTOMER not found")
    def get(self, id):
        id = str(id)
        conn = connect()
        select = """
            SELECT *
            FROM customers
            WHERE customer_id = '{0}';""".format(id)
        result = conn.execute(select).fetchall()
        disconnect(conn)
        return jsonify({'result': [dict(row) for row in result]})

transactions = Namespace('transactions',
    description = 'All operations related to transactions',
    path='/api/v1')
api.add_namespace(transactions)

@transactions.route("/transactions")
class get_all_users(Resource):

    def get(self):
        conn = connect()
        select = """
            SELECT *
            FROM transactions
            LIMIT 1000; """
        result = conn.execute(select).fetchall()
        disconnect(conn)
        return jsonify({'result': [dict(row) for row in result]})

@transactions.route("/transactions/<string:id>")
@transactions.doc(params = {'id': 'The Channel of the transaction'})
class select_user(Resource):

    @api.response(404, "TRANSACTION not found")
    def get(self, id):
        id = str(id)
        conn = connect()
        select = """
            SELECT *
            FROM transactions
            WHERE sales_channel_id = '0';""".format(id)
        result = conn.execute(select).fetchall()
        disconnect(conn)
        return jsonify({'result': [dict(row) for row in result]})

articles = Namespace('articles',
    description = 'All operations related to articles',
    path='/api/v1')
api.add_namespace(articles)

@articles.route("/articles")
class get_all_users(Resource):

    def get(self):
        conn = connect()
        select = """
            SELECT *
            FROM articles
            LIMIT 1000;"""
        result = conn.execute(select).fetchall()
        disconnect(conn)
        return jsonify({'result': [dict(row) for row in result]})

@articles.route("/articles/<string:id>")
@articles.doc(params = {'id': 'The ID of the article'})
class select_user(Resource):

    @api.response(404, "ARTICLE not found")
    def get(self, id):
        id = str(id)
        conn = connect()
        select = """
            SELECT *
            FROM articles
            WHERE article_id = '{0}';""".format(id)
        result = conn.execute(select).fetchall()
        disconnect(conn)
        return jsonify({'result': [dict(row) for row in result]})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug = True)