from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to our simple Flask Web Application!"

@app.route('/time')
def show_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    return f"Current server time is: {current_time}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 