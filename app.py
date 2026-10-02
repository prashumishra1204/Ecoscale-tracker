from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Function to connect directly to our local cloud MySQL database
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        database="ecoscale"
    )

@app.route('/')
def home():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Check if our table exists
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()
        
        cursor.close()
        conn.close()
        
        return jsonify({
            "status": "Success",
            "message": "EcoScale backend is running and successfully connected to MySQL!",
            "database_tables": tables
        })
    except Exception as e:
        return jsonify({"status": "Error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
