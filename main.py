from datetime import datetime
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.now()
    
    if now.today().weekday() > 4:
        morningShift = now.replace(hour=7, minute=30, second=00)
    else:
        morningShift = now.replace(hour=7, minute=00, second=00)

    nightShift = now.replace(hour=20, minute=00, second=00)
     
    if now < morningShift or now > nightShift:
        template = 'night.html'
    else:
        template = 'day.html'

    return render_template(template)