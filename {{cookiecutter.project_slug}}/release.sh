#! /bin/bash
# 构建 Docker镜像并发布至镜像仓库
docker build -t {{cookiecutter.project_name}}:latest .
echo "docker build success..."
docker login --username=aqu****** registry.cn-hangzhou.aliyuncs.com  # 修改为自己的仓库源
echo "docker login success"
docker tag {{cookiecutter.project_name}}:latest registry.cn-hangzhou.aliyuncs.com/idcard/idcard_project:{{cookiecutter.project_name}}_latest
echo "docker tag success"
docker push registry.cn-hangzhou.aliyuncs.com/idcard/idcard_project:{{cookiecutter.project_name}}_latest
echo "docker push success"
