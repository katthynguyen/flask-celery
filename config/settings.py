# DEV settings.py
import os


DEBUG = True

# Secret key
SECRET_KEY = os.urandom(24)


# Celery Config
CELERY_BROKER_URL = 'redis://0'
CELERY_RESULT_BACKEND = 'redis://6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_REDIS_MAX_CONNECTIONS = 5

