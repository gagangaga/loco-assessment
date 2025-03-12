# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello():
#     return 'Hello, LOCO!\n'

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=80)

from flask import Flask, render_template, jsonify
import datetime
import random

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.datetime.now()
    random_number = random.randint(1, 100)
    return render_template('index.html', current_time=now, random_number=random_number)

@app.route('/api/random')
def random_api():
    random_data = {
        "value": random.randint(1, 1000),
        "timestamp": datetime.datetime.now().isoformat()
    }
    return jsonify(random_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)