# torch GPU env with nginx and supervisor
# FROM ubuntu:18.04
FROM nvidia/cuda:10.0-cudnn7-runtime-ubuntu18.04

LABEL maintainer "Aquish"

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
&& apt-get install -y software-properties-common \
# torch dependence
&& apt install -y libglib2.0-0 libsm6 libxrender1 libxext-dev \
&& apt install -y vim htop cmake gcc redis-server nginx supervisor ipython \
&& apt autoremove -y \
&& apt-get install -y python3 python3-dev python3-pip \
&& apt-get install -y build-essential \
&& apt-get install -y python3-tk && pip3 install scikit-build

RUN mkdir -p /{{cookiecutter.project_slug}}
WORKDIR /{{cookiecutter.project_slug}}

# src
COPY . /{{cookiecutter.project_slug}}

RUN pip3 install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com --upgrade pip
RUN pip3 install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com -r requirements/base.txt \
&& rm -rf ~/.cache/pip

# Nginx config
COPY requirements/default /etc/nginx/sites-available/default
COPY requirements/nginx.conf /etc/nginx/nginx.conf
# Supervisor config
COPY requirements/supervisord.conf /etc/supervisor/supervisord.conf

# CN support
ENV LANG C.UTF-8

EXPOSE 8000

# Start supervisor
CMD ["/etc/init.d/supervisor", "start"]
