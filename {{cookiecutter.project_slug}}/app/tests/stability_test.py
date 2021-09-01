# -*- coding:utf-8 -*-
"""
多进程请求测试服务可用性
"""
import os
import time
import json
import base64
import requests
from multiprocessing import Process


# 文件目录遍历，返回[fileP, fileN]
def get_filepaths(path):
    pathlists = []
    for root, dirs, files in os.walk(path):
        for file in files:
            pathlists.append([os.path.join(root, file), file])
    return pathlists


#推理请求
def main_request(imgP):
    url = "http://0.0.0.0:8000/inference"  # nginx url
    with open(imgP,'rb') as f:
        imgString = base64.b64encode(f.read())

    # 传输的数据格式
    data = {
        'img_string': imgString.decode(),
    }

    response = requests.post(url, json.dumps(data)) #本地测试

    return response


#循环——推理
def start_det(strN, imgpath):
    epoch = 0
    img_type = ['png', 'jpg', 'jpeg', 'bmp', 'JPEG']

    while True:
        filelists = get_filepaths(imgpath)
        for imgP, imgN in filelists:
            if imgN.split('.')[-1] in img_type:
                start_time = time.time()
                response = main_request(imgP)
                print('epoch:%d--worknum:%s--time:%f--response:%s' % (epoch, strN, time.time()-start_time, response.json()))

        epoch += 1


# 设置工程进程数量
def multiprocess_requests(worknum, imgpath):
    proc_record = []
    for i in range(worknum):
        p = Process(target=start_det, name=str(i), args=(str(i), imgpath))
        p.start()
        proc_record.append(p)
    for p in proc_record:
        p.join()


if __name__ == '__main__':
    worknum = 30  # 请求进程数
    imgpath = 'tests/test_imgs'  # 图片目录
    multiprocess_requests(worknum, imgpath)
