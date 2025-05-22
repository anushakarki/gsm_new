from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/')
def control():
    return render_template('index.html')

@app.route('/relay')
def relay_control():
    state = request.args.get('state')
    print(f"Relay state requested: {state}")

    con = sqlite3.connect('gsm_data.db')
    cursor = con.cursor()

    # Check if there's an existing state row
    cursor.execute("SELECT STATE FROM data WHERE id = 1")
    value = cursor.fetchone()

    if value is None:
        cursor.execute("INSERT INTO data (STATE) VALUES (?)",(state,))
    else:
        cursor.execute("UPDATE data SET STATE = ? WHERE id = 1", (state,))

    con.commit()
    con.close()

    return redirect(url_for("control"))

@app.route("/send_state")
def send_state():
    con = sqlite3.connect('gsm_data.db')
    cursor = con.cursor()
    cursor.execute("SELECT STATE FROM data WHERE id = 1")
    value = cursor.fetchone()
    con.close()

    return str(value[1]) if value else "UNKNOWN"

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
