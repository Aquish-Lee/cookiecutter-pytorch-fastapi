# -*- coding: utf-8 -*-
# @Author  : Aquish
# @Organization : NTT
import os
import sys
sys.path.insert(0, os.getcwd())

import cv2
import json
import base64
import importlib
import numpy as np

from . import app
from celery import Task
from logzero import logger


def base64_to_ndarray(b64_data):
    # 进行base64解码 base64 -> ndarray
    img = base64.b64decode(b64_data)
    # 二进制数据流转np.ndarray [np.uint8: 8位像素]
    img = cv2.imdecode(np.frombuffer(img, np.uint8), cv2.IMREAD_ANYCOLOR)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    return img


class PredictTask(Task):
    """
    Abstraction of Celery's Task class to support loading DL model.
    """
    def __init__(self):
        """
        Load model on first init
        Avoids the need to load model on each task request
        """
        super().__init__()
        self.model = None

    def __call__(self, *args, **kwargs):
        if not self.model:
            logger.info('Loading Model...')
            module_import = importlib.import_module(self.path[0])
            model_obj = getattr(module_import, self.path[1])
            self.model = model_obj()
            logger.info('Model loaded')

        return self.run(*args, **kwargs)


@app.task(ignore_result=False, bind=True, base=PredictTask,
          path=('service.predict', 'infer_obj'),
          name='{}.{}'.format(__name__, 'inference'))
def inference(self, data):
    """
    Essentially the run method of PredictTask
    data : imgstring
    """

    result = None
    # imgstring -> ndarray
    data = json.loads(data)
    try:
        img = base64_to_ndarray(data["img_string"].encode())
    except Exception:
        logger.info("base64 to ndarray error")

    try:
        result = self.model.predict(img)
    except Exception:
        logger.info("predict error")

    return result