# -*- coding: utf-8 -*-
# @Author  : Aquish
# @Organization : NTT
"""
infer_obj:
    __init__(): 定义模型需要的变量并执行_init_model()
    _init_model(): 加载变量完成网络模型搭建、权重加载
    predict(): 定义网络接收图片后预处理、推理、后处理的pipeline
    
约定：
    utils/assets/checkpoints 存放模型权重文件
    utils/assets/models 存放网络结构定义函数
    utils/assets/config 存放配置文件（如网络结构配置文件等）
    
    utils/helper 存放模型推理所需的自定义函数(如resize、pad等）
"""
# 模型相关三方库、自定义函数导入

# 日志设置，采用logger.info记录
from logzero import logger
# GPU设置
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"


class infer_obj:
    """
    图片尺寸、阈值等不常变但重要的值设为常量
    如 IMG_SIZE = 416
    """

    def __init__(self):
        """
        定义模型所需的变量，如model_def文件路径、class_name、model_weights文件路径等
        并调用self._init_model()实现模型网络定义及权重加载。
        """ 
        pass 


    def _init_model(self):
        """
        取用__init__中定义的变量执行：读取配置文件、加载网络模型、加载模型权重等操作
        """
        # 定义网络并加载权重
        pass


    @torch.no_grad()
    def predict(self, img):
        """
        img: cv2.imread
            数据预处理->模型推理->结果后处理
        实现网络接收ndarray并输出结果的推理pipeline
        根据业务内容相应做异常处理及日志记录
        """
        res = do_somethin()

        return json.dumps(res)


if __name__ == "__main__":
    infer = infer_obj()

    img_path = ""
    res = infer.predict(cv2.imread(img_path))
    logger.info(f"识别结果: {json.loads(res)}")
