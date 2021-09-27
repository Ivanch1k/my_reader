from celery.decorators import task


@task
def task_hello():
    print('hello')
    return 'hello'
