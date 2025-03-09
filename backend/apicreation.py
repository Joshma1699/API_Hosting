from flask import Flask, jsonify
import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Database connection
def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

# 1. Get all plans (filtered)
@app.route('/plans', methods=['GET'])
def get_filtered_all_plans():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT category, plans, price, description FROM plans")
        plans = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(plans)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 2. Get all plans (full details)
@app.route('/plans/full', methods=['GET'])
def get_all_plans_full():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM plans")
        plans = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(plans)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 3. Get category details (filtered)
@app.route('/plans/category/<category>', methods=['GET'])
def get_filtered_plans_by_category(category):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT category, plans, price, description FROM plans WHERE category = %s", (category,))
        plans = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(plans)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 4. Get category details (full)
@app.route('/plans/category/<category>/full', methods=['GET'])
def get_plans_by_category_full(category):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM plans WHERE category = %s", (category,))
        plans = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(plans)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 5. Get plan details (filtered)
@app.route('/plans/<plan_name>', methods=['GET'])
def get_filtered_plan_by_name(plan_name):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT category, plans, price, description FROM plans WHERE plans = %s", (plan_name,))
        plan = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(plan)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 6. Get plan details (full)
@app.route('/plans/<plan_name>/full', methods=['GET'])
def get_plan_by_name_full(plan_name):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM plans WHERE plans = %s", (plan_name,))
        plan = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(plan)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
