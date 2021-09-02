# -*- coding: utf-8 -*-
# @Author  : Aquish
# @Organization : NTT
from celery import Celery
from msg_queue.celery_config import broker_url, backend_url


app = Celery('celery_app',
            broker=broker_url,
            backend=backend_url)  # 实例化Celery对象
app.config_from_object('msg_queue.celery_config')  # 加载配置文件