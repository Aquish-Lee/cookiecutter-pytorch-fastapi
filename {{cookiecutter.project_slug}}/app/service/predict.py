import os
import cv2
import torch
import numpy as np
import torchvision.transforms as transforms

from PIL import Image
from torch.autograd import Variable
from collections import OrderedDict
from utils.asserts.network_crnn import CRNN
from utils.asserts.network_yolo import Darknet
from utils.helper.keys import alphabetEnglish as alphabet  # 指定字典
from utils.helper.datasets import pad_to_square, resize
from utils.helper.utils import non_max_suppression, rescale_boxes, strLabelConverter, resizeNormalize

# LOG Define==================================
from logzero import logger

# CONFIG Define================================
os.environ["CUDA_VISIBLE_DEVICES"] = "0"


class infer_obj:
    CONF_THRES = 0.8
    NMS_THRES = 0.2
    IMG_SIZE = 416

    def __init__(self):
        self.classes = ['id']
        self.model_def = os.path.join("utils/asserts/config", "yolov3.cfg")
        self.yolo_weights_path = os.path.join("utils/asserts/checkpoints", "yolo.pth")
        self.ocr_weights_path = os.path.join("utils/asserts/checkpoints", "ocr-english.pth")

        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.Tensor = torch.cuda.FloatTensor if torch.cuda.is_available() else torch.FloatTensor

        if self.device == "cuda": logger.info(f"Using Device {self.device}") 

        self._init_ocr()
        self._init_yolo()


    def _init_ocr(self):
        # 定义网络
        self.crnn = CRNN(32, 1, len(alphabet)+1, 256, lstmFlag=True).cuda()
        # 加载权重
        trainWeights = torch.load(self.ocr_weights_path, map_location=lambda storage, loc: storage)
        modelWeights = OrderedDict()
        for k, v in trainWeights.items():
            name = k.replace('module.','') # remove `module.`
            modelWeights[name] = v
        self.crnn.load_state_dict(modelWeights)
        self.crnn.eval()
        self._init_stuff()
        logger.info("OCR Init Success ...")


    def _init_stuff(self):
        self.converter = strLabelConverter(alphabet)


    def _init_yolo(self):
        self.yolo = Darknet(self.model_def, self.IMG_SIZE).to(self.device)
        self.yolo.load_state_dict(torch.load(self.yolo_weights_path, map_location=lambda storage, loc: storage))
        self.yolo.eval()
        logger.info("YOLO Init Success ...")


    @torch.no_grad()
    def predict(self, img):
        """
        img: cv2.imread
        """
        # yolo数据预处理
        img_ = transforms.ToTensor()(img)
        img_, _ = pad_to_square(img_, 0)
        img_ = resize(img_, self.IMG_SIZE)
        img_ = torch.unsqueeze(img_, 0)
        if self.device == "cuda":
            img_ = img_.cuda()
        else:
            img_ = img_.cpu()
        img_ = Variable(img_.type(self.Tensor))

        # yolo推理
        img_detections = []
        detections = self.yolo(img_)
        detections = non_max_suppression(detections, self.CONF_THRES, self.NMS_THRES)
        img_detections.extend(detections)

        # yolo后处理
        if img_detections:

            # Rescale boxes to original image
            detections_ = rescale_boxes(img_detections[0], self.IMG_SIZE, img.shape[0], img.shape[1])
            if len(detections_) != 1:
                logger.info("=========Detection Mistake=========")
                return ""

            for x1, y1, x2, y2, conf, cls_conf, cls_pred in detections_:
                class_name = self.classes[int(cls_pred)]
                x1, x2, y1 ,y2 = int(x1.numpy()), int(x2.numpy()), int(y1.numpy()), int(y2.numpy())
            
            # 获取ROI区域，开始CRNN识别
            ocr_img = img[y1-5:y2+5, x1-5:x2+5]
            # opencv -> PIL
            ocr_img = Image.fromarray(cv2.cvtColor(ocr_img, cv2.COLOR_BGR2RGB)).convert("L")
            
            # CRNN数据预处理
            scale = ocr_img.size[1]*1.0 / 32
            w = int(ocr_img.size[0] / scale)
            transformer = resizeNormalize((w, 32))

            ocr_img = transformer(ocr_img).astype(np.float32)
            ocr_img = torch.from_numpy(ocr_img)
            if self.device == "cuda":
                ocr_img = ocr_img.cuda()
            else:
                ocr_img = ocr_img.cpu()
            ocr_img = ocr_img.view(1, 1, *ocr_img.size())
            ocr_img = Variable(ocr_img.type(self.Tensor))
            
            # CRNN推理
            preds = self.crnn(ocr_img)
            _, preds = preds.max(2)
            preds = preds.transpose(1, 0).contiguous().view(-1)

            if len(self.converter.decode(preds)) != 18:
                logger.info("=========Recognition False=========")
                return ""
            else:
                # CRNN后处理
                return self.converter.decode(preds)

        else:
            logger.info("=========No Detected ID Area=========")
            return ""

        del _
        del img
        del img_
        del ocr_img
        del transformer
        del detections
        del detections_
        del img_detections


if __name__ == "__main__":
    img = cv2.imread("tests/images/1.jpg")
    
    infer = infer_obj()
    res = infer.predict(img)

    print(res)
