from celery import Celery

app = Celery('tasks')


class  CeleryConfig:

    timezone = 'Asia/Ho_Chi_Minh'
    broker_url = 'redis://localhost:6379/0'
    result_backend = 'redis://localhost:6379/0'


app.config_from_object(CeleryConfig)

@app.task
def example():
    return 'celery config'