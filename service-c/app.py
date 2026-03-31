from flask import Flask
import psycopg2

app = Flask(__name__)

def get_db_time():
    conn = psycopg2.connect(
        host="db-service",
        database="testdb",
        user="postgres",
        password="password"
    )
    cur = conn.cursor()
    cur.execute("SELECT NOW();")
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result[0]

@app.route("/inventory")
def inventory():
    try:
        time = get_db_time()
        return f"Inventory OK → DB Time: {time}"
    except Exception as e:
        return f"DB Error: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
