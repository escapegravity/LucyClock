from datetime import datetime
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.now()
    morningShift = now.replace(minute=30, hour=7, second=00)
    nightShift = now.replace(minute=30, hour=19, second=00)
     
    if now < morningShift or now > nightShift:
        template = 'night.html'
    else:
        template = 'day.html'

    return render_template(template)