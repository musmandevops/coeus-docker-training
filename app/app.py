from flask import Flask
from waitress import serve
from flaskext.mysql import MySQL
import json
import os
import threading

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = os.environ.get('DB_USER')
app.config['MYSQL_DATABASE_PASSWORD'] = os.environ.get('DB_PASSWORD')
app.config['MYSQL_DATABASE_DB'] = os.environ.get('DB_NAME')
app.config['MYSQL_DATABASE_HOST'] = os.environ.get('DB_HOST')
mysql.init_app(app)

@app.route('/')
def main_page():
    return 'Coeus sol App Main Page!'

@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/user/')
def users():
    query = "select id,username,email,created_at from users"
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
    except Exception as e:
        return "Execption in database: " + str(e)

    response = {}
    for row in data:
        response[row[0]] = {"username": str(row[1]), "email": str(row[2]), "created_at": str(row[3])}
    if not response:
        response = {"message": "record not found"}
    response = json.dumps(response)
    return response

def start_server():
    serve(app, host='0.0.0.0', port=8080, debug=True)

if __name__ == '__main__':
    print("Application is starting...")
    # t = threading.Thread(target=start_server)
    # t.start()
    # print(f"Application is up and running on http://0.0.0.0:8080")
    app.run(debug=True, host='0.0.0.0', port=8080)
    print(f"Application is up and running on http://0.0.0.0:8080")
