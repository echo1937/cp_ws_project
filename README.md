# cp_ws_project

celery progress websocket project.

This is an example project demonstrating the capabilities of [this project](https://github.com/czue/celery-progress).

### Channels

- [Installation](https://channels.readthedocs.io/en/stable/installation.html)
- [Tutorial](https://channels.readthedocs.io/en/stable/tutorial/index.html)
- [Demo](http://) to be continued

### Celery

- [Installation](https://docs.celeryq.dev/en/stable/getting-started/introduction.html#installation)
- [First steps with Django](https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html)

### Using

- Start your redis server
- Start both the django and celery servers

    ```shell
    celery -A cp_ws_project worker -l DEBUG
    ```

- Go to index page (http://localhost:8000 usually) to view various optional tests

### Question

1、重要参数的梳理

- CELERY_BROKER_URL -- 接收和发送任务的消息中间件
- CELERY_RESULT_BACKEND -- 记录任务执行结果的组件
- [CHANNEL_LAYERS](https://channels.readthedocs.io/en/stable/topics/channel_layers.html)

