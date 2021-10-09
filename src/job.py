import time

from celery import Celery

job = Celery('tasks', broker='redis://redis:6379')

# タスク実行後の結果をredisに格納する
job.conf.result_backend = 'redis://redis:6379/0'


@job.task
def test_celery_task(message: str) -> None:
    time.sleep(10)
    print(message)
