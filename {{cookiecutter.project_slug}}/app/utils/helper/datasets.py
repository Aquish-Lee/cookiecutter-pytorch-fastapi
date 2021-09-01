import numpy as np
import torch.nn.functional as F


def pad_to_square(img, pad_value):
    # 将图片补全为正方形。pad_value补全部分填充的值
    c, h, w = img.shape
    dim_diff = np.abs(h - w) # 长宽差异的绝对值
    # (upper / left) padding and (lower / right) padding
    pad1, pad2 = dim_diff // 2, dim_diff - dim_diff // 2 # 左上/右下的补全padding。整除
    # Determine padding
    pad = (0, 0, pad1, pad2) if h <= w else (pad1, pad2, 0, 0) # 四维tuple
    # Add padding
    img = F.pad(img, pad, "constant", value=pad_value) # img->Tensor 

    return img, pad


def resize(image, size):
    # 上/下采样 3,size,size -> 1,3,size,size -> 1,3,new_size,new_size -> 3,new_size,new_size
    image = F.interpolate(image.unsqueeze(0), size=size, mode="nearest").squeeze(0)
    return image
