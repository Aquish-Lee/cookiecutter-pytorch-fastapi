# -*- coding: utf-8 -*-
# @Author  : Aquish
# @Organization : NTT
broker_url = "redis://localhost:6379/0"
backend_url = "redis://localhost:6379/1"

result_expires = 60  # 一分钟超时时间
worker_concurrency = 4  # worker 并发数
task_serializer = 'json'
accept_content = ['json']
result_serializer = 'json'
worker_max_tasks_per_child = 2000  # worker执行多少任务后kill

# 导入任务
imports = (
    'msg_queue.tasks'
)
