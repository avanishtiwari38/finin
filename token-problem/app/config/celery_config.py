from celery import Celery

from app.config.local_config import Config


# You need to replace the next values with the appropriate values for your configuration
def make_celery(app):
    celery_app = Celery('app.tasks.tasks', backend=Config.result_backend,
                        broker=Config.broker_url)
    # celery_app.conf.update(
    #     task_serializer='json',
    #     accept_content=['json'],  # Ignore other content
    #     result_serializer='json',
    #     timezone='Asia/Calcutta',
    #     enable_utc=False,
    #     result_persistent=True,
    #     celery_task_routes=Config.celery_task_routes,
    #     task_queues=Config.task_queues,
    #     task_default_queue=Config.task_default_queue,
    #     worker_hijack_root_logger=False,
    #     task_ignore_result=True,
    #     broker_heartbeat=10,
    #     broker_pool_limit=None,
    #     broker_connection_retry=True,
    #     broker_connection_max_retries=None,
    #     broker_connection_timeout=120

    # )
    celery_app.conf.update(app.config)

    class ContextTask(celery_app.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_app.Task = ContextTask
    return celery_app