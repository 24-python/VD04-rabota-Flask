from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%Y-%m-%d")
    return f"Текущее время: {current_time}, Текущая дата: {current_date}"


if __name__ == '__main__':
    app.run()