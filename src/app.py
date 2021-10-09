from flask import Flask

from src.job import test_celery_task


api = Flask(__name__)


@api.route('/')
def test_task():  # put application's code here
    test_celery_task.delay("Hello Celery!!")
    return {
        'message': 'OK'
    }


if __name__ == '__main__':
    api.run()
