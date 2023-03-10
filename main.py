from datetime import timedelta
from flask import Flask
from app.celery import make_celery
from flask_cors import CORS
from celery.schedules import crontab


app = Flask(__name__)

app.config.from_object('config')
CORS(app)
celery = make_celery(app)


@celery.task()
def add_together(a, b):
    print(" RUN TASK add_together ")
    return a + b


@app.route('/')
def index():
    try:
        result = add_together.delay(2, 3)
        a = result.get()
        return f'Task ID: {result.id} --- Kết quả {a}'
    except Exception as e:
        return str(e)


celery.conf["CELERYBEAT_SCHEDULE"] = {
    'add_task': {
        'task': 'app.tasks.add',
        'schedule': crontab(minute='*'),
        'args': (3, 4)
    },
}


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, threaded=True)
