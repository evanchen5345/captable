import config, sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    founderName = request.args.get('founderName', None)
    ownership = request.args.get('ownership', None)
    seriesName = request.args.get('seriesName', None)
    investorName = request.args.get('investorName', None)
    investorFirm = request.args.get('investorFirm', None)
    committedCapital = request.args.get('committedCapital', None)
    postVal = request.args.get('postVal', None)

    connection = sqlite3.connect(config.DB_FILE)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    if founderName is not None and ownership is not None:
        cursor.execute("INSERT INTO investors (seriesName, name, ownership) VALUES (?,?,?)", ("Founders",founderName, ownership))
    if seriesName is not None and investorName is not None and committedCapital is not None and postVal is not None:
        invOwnership = committedCapital / postVal
        cursor.execute("INSERT INTO investors (seriesName, name, firm, capital, ownership) VALUES (?,?)", (seriesName, investorName, investorFirm, committedCapital, invOwnership))

    cursor.execute("SELECT name, ownership FROM investors")
    captable = {row[0]:row[1] for row in cursor.fetchall()}

    connection.commit()
    return render_template('index.html', captable=captable)


def get_db_cur():
    connection = sqlite3.connect(config.DB_FILE)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    return cursor