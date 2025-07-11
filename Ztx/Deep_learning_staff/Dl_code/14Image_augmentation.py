
'''

图像增广和模型微调助于提高模型的泛化能力

    增广方法
1.  图像翻转/裁剪
2.  改变RGB颜色值
3.  融合方法1,2

'''

import d2lzh as d2l 
import mxnet as mx 
from mxnet import autograd, gluon, image, init, nd
from mxnet.gluon import data as gdata, loss as gloo, utils as gutils 
import sys
import time 
from PIL import Image
import numpy as np 
import os


# img = image.imread('img/cat1.jpg').asnumpy().astype(np.uint8)

# pil_image = Image.fromarray(img)

# pil_image.save('cat.jpg', quality=95)


    