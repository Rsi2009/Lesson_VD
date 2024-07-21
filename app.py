from flask import Flask
from datetime import datetime

app = Flask(__name__)  # Используйте __name__, а не name

@app.route('/')
def home():
    now = datetime.now()
    current_time = now.strftime("%d-%m-%Y %H:%M:%S")
    return f'Текущая дата и время: {current_time}'

if __name__ == '__main__':  # Исправьте на __name__ == '__main__'
    app.run(debug=True)
