# {{cookiecutter.project_name}}

{{cookiecutter.project_short_description}}

---



## 相关资源

项目主要涉及到六个依赖：

| Dependency Name | Documentation                             | Description                                                  |
| --------------- | ----------------------------------------- | ------------------------------------------------------------ |
| Pytorch         | https://pytorch.org/                      | An open source machine learning framework                    |
| Celery          | https://docs.celeryproject.org/en/stable/ | Distributed Task Queue                                       |
| FastAPI         | https://fastapi.tiangolo.com              | FastAPI framework, high performance, easy to learn, fast to code, ready for production |
| Gunicorn        | https://gunicorn.org/                     | A Python WSGI HTTP Server for UNIX with pre-fork worker model |
| Nginx           | https://www.nginx.com/                    | An HTTP and reverse proxy server, Support load balancer and HTTP cache |
| Supervisor      | http://supervisord.org/                   | A client/server system, support monitor and control a number of processes on UNIX-like operating systems |

---



## 实现功能

该项目主要实现了以下功能：

- 基于Celery部署深度学习，实现分布式任务调度

- 基于FastAPI提供WEB Server服务

- 基于Gunicorn+Nginx实现WEB部署
- Supervisor实现项目组件管控
- 支持Docker部署



## Project structure

[![hDf9Ig.md.png](https://z3.ax1x.com/2021/09/02/hDf9Ig.md.png)](https://imgtu.com/i/hDf9Ig)



## 自定义模块规范

```python
- app/service/predict.py:
    infer_obj():
  		__init__(): 定义模型需要的变量并执行_init_model()_
  		init_model(): 加载变量完成网络模型搭建、权重加载
  		predict(): 定义网络接收图片后预处理、推理、后处理的pipeline

- utils/assets/checkpoints 存放模型权重文件
- utils/assets/models 存放网络结构定义函数
- utils/assets/config 存放配置文件（如网络结构配置文件等）
- utils/helper 存放模型推理所需的自定义函数(如resize、pad等）
```



## 可修改配置文件项

```python
- 项目三方包依赖修改：
{{cookiecutter.project_name}}/requirements/base.txt

- Nginx 配置修改(代理端口、worker数)：{{cookiecutter.project_name}}/requirements/default|nginx.conf

- celery worker数修改：{{cookiecutter.project_slug}}/app/msg_queue/celery_config.py

- gunicorn worker数修改：{{cookiecutter.project_slug}}/app/utils/assets/config/gunicorn_config.py
```



## Docker运行

将app/service/predict.py 填充内容并单测通过后，运行Docker发布脚本

```bash
# 定位到目录 {{cookiecutter.project_slug}}/
# 构建镜像并推送至仓库（需修改仓库地址）
sh release.sh
# 构建完毕后运行容器
docker run -itd --name container_name -p port:8000 {{cookiecutter.project_name}}:latest bash
# 链接到容器内
docker exec -it container_name bash
# 开启服务
/etc/init.d/supervisor start
```

服务正常开启后可访问 http://localhost:port/docs查看FastAPI的UI界面

[![hwDwz4.md.png](https://z3.ax1x.com/2021/09/01/hwDwz4.md.png)](https://imgtu.com/i/hwDwz4)


也可访问 http://localhost:8000/redoc



## 识别结果展示

原图：



识别结果：

