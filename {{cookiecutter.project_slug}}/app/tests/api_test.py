# -*- coding: utf-8 -*-
# @Author  : Aquish
# @Organization : NTT
"""
fastapi、nginx内部连通性测试
"""
import os
import time
import json
import base64
import requests
from logzero import logger


# 文件目录遍历，返回[fileP, fileN]
def get_filepaths(path):
    pathlists = []
    for root, dirs, files in os.walk(path):
        for file in files:
            pathlists.append([os.path.join(root, file), file])
    return pathlists


class api_test:
    def __init__(self):
        self.url = "http://0.0.0.0:5000/inference"  # fastapi url

    @staticmethod
    def read_img_base64(p):
        with open(p,'rb') as f:
            img_string = base64.b64encode(f.read())
        return img_string.decode()

    def send_post(self, img_path):
        imgstring = self.read_img_base64(img_path)

        data = {
        'img_string': imgstring
        }
        
        start_time = time.time()
        session = requests.session()
        response = session.post(self.url, json.dumps(data))  # Json格式请求

        logger.info("time: {}".format(time.time()-start_time, '.2f')+"s")
        logger.info(response.status_code)
        logger.info(response.text)

        session.close()
        response.close()


if __name__ == "__main__":
    # 开始单元测试
    api = api_test()
    
    # 文件夹测试
#     img_dir_path = 'tests/images'
#     img_type = ['png', 'jpg', 'jpeg', 'bmp', 'JPEG']
#     filelists = get_filepaths(img_dir_path)
#     for imgP, imgN in filelists:
#         print(imgP)
#         if imgN.split('.')[-1] in img_type:
#             api.send_post(imgP)

    # 单张图片测试
    img_path = "tests/images/1.jpg"
    api.send_post(img_path)
