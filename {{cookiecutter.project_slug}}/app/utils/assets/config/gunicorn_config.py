# -*- coding: utf-8 -*-
# @Author  : Aquish
# @Organization : NTT
bind = ":5000"
pidfile = 'logs/gunicorn.pid'
workers = 3 # 推荐核数*2+1发挥最佳性能
worker_class = 'uvicorn.workers.UvicornWorker'
threads = 1
worker_connections = 2000
timeout = 600  # 深度学习模型加载比较耗时，设长一点
reload = True
daemon = False

accesslog = 'logs/access.log'
errorlog = 'logs/error.log'
loglevel = 'info'
