# cookiecutter-pytorch-fastapi

Python cookiecutter API for quick deployments of Pytorch models with FastAPI

## Requirements
- Python >= 3.6 with pip installed

## Quickstart

### Install the latest [Cookiecutter](https://github.com/audreyr/cookiecutter) if you haven't installed it yet (this requires Cookiecutter 1.4.0 or higher):
```
apt-get install cookiecutter
```

### Point cookiecutter to this GitHub repository to automatically download and generate your project

```
cookiecutter https://github.com/Microsoft/cookiecutter-azure-search-cognitive-skill
```

View the README.md of your new project for instructions on next steps

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
