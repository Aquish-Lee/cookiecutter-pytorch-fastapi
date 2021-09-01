# {{cookiecutter.project_name}}

{{cookiecutter.project_short_description}}

---

## Resources
This project has six key dependencies:

| Dependency Name | Documentation                             | Description                                                  |
| --------------- | ----------------------------------------- | ------------------------------------------------------------ |
| Pytorch         | https://pytorch.org/                      | An open source machine learning framework                    |
| Celery          | https://docs.celeryproject.org/en/stable/ | Distributed Task Queue                                       |
| FastAPI         | https://fastapi.tiangolo.com              | FastAPI framework, high performance, easy to learn, fast to code, ready for production |
| Gunicorn        | https://gunicorn.org/                     | A Python WSGI HTTP Server for UNIX with pre-fork worker model |
| Nginx           | https://www.nginx.com/                    | An HTTP and reverse proxy server, Support load balancer and HTTP cache |
| Supervisor      | http://supervisord.org/                   | A client/server system, support monitor and control a number of processes on UNIX-like operating systems |
---

## Major Functions
This project mainly realizes the following functions:
- 

- 
-  

## Run With Docker
To run locally in terminal:

```
cd ./{{cookiecutter.project_slug}}
# build images
docker build -t xxx:xxx .
# start container
docker run -itd --name container_name -p port:8000 image_name:tag bash
# link into container
docker exec -it container_name bash
# start server
/etc/init.d/supervisor start
```
Open your browser to http://localhost:port/docs to view the OpenAPI UI.

[![hwDwz4.md.png](https://z3.ax1x.com/2021/09/01/hwDwz4.md.png)](https://imgtu.com/i/hwDwz4)


For an alternate view of the docs navigate to http://localhost:port/redoc

## Recognition results display

paste original image here



paste recognition results here