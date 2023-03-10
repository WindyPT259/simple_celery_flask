# APIURL
API_URL = "http://127.0.0.1:5008"
# Connect DB
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:250997@localhost/sampleapp?charset=utf8mb4'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_POOL_TIMEOUT = 20

DEBUG = True

# Celery configuration
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_INCLUDE = ['app.tasks', 'main']
CELERY_TRACK_STARTED = True
CELERY_SEND_EVENTS = True
# import tasks
# imports = ('app.tasks.add')
