# -*- coding: utf-8 -*-
# @Author  : Aquish
# @Organization : NTT
"""
celery pipeline连通性测试
"""
import json
import base64
from logzero import logger
from controller.model_controller import controller_inference


def read_img_base64(p):
    with open(p,'rb') as f:
        img_string = base64.b64encode(f.read())
    return img_string.decode()


if __name__ == "__main__":
    # 开始单元测试
    img_path = "tests/images/1.jpg"
    imgString = read_img_base64(img_path)  # string 类型的base64 bytes

    data = {
        "img_string": imgString
}

    res = controller_inference(json.dumps(data))
    logger.info(f"celery task id: {res.id}")
    logger.info(f"inference result: {json.loads(res.get())}")
