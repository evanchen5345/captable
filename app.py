import config, sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    founderName = request.args.get('founderName')
    founderTitle = request.args.get('founderName')
    ownership = request.args.get('founderName')

    cursor = get_db_cur()
    # cursor.excecute("""
    #     INSERT INTO investors (name)
    # """)
    return render_template('index.html')


def get_db_cur():
    connection = sqlite3.connect(config.DB_FILE)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    return cursor