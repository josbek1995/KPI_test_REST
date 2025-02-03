from flask import Flask, jsonify
import os
from flask_mysqldb import MySQL
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# MySQL configurations
app.config["MYSQL_HOST"] = os.getenv("MYSQL_HOST")
app.config["MYSQL_USER"] = os.getenv("MYSQL_USER")
app.config["MYSQL_PASSWORD"] = os.getenv("MYSQL_PASSWORD")
app.config["MYSQL_DB"] = os.getenv("MYSQL_DB")
app.config["MYSQL_CURSORCLASS"] = os.getenv("MYSQL_CURSORCLASS", "DictCursor")
app.config["MYSQL_PORT"] = int(os.getenv("MYSQL_PORT", 3306))

# Initialize MySQL
mysql = MySQL(app)

@app.route('/monthly-sales', methods=['GET'])
def monthly_sales():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM KPI_Ventas_Mensuales")
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

@app.route('/inventory-turnover', methods=['GET'])
def inventory_turnover():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM KPI_Rotacion_Inventarios")
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

@app.route('/profitability', methods=['GET'])
def profitability():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM KPI_Rentabilidad")
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

@app.route('/products-by-customer', methods=['GET'])
def products_by_customer():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM KPI_Productos_Por_Cliente")
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
