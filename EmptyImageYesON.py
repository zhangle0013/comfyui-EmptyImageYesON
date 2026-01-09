# image_auto_disable_node.py
import torch
import numpy as np
from PIL import Image
import folder_paths

class ImageAutoDisableNode:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "optional": {
                "image": ("IMAGE",),
            }
        }
    
    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("output_image",)
    FUNCTION = "process_image"
    CATEGORY = "image/utils"
    
    def process_image(self, image=None):
        # 如果图像无效，返回None
        if not self.is_valid_image(image):
            return (None,)
        return (image,)
    
    def is_valid_image(self, image):
        """检查图像是否有效"""
        if image is None:
            return False
        if not isinstance(image, torch.Tensor):
            return False
        if image.nelement() == 0:
            return False
        if len(image.shape) < 3:
            return False
        if image.shape[1] == 0 or image.shape[2] == 0:
            return False
        return True
    
    @classmethod
    def IS_CHANGED(cls, image=None, **kwargs):
        """这个方法控制节点是否重新执行"""
        # 创建实例来调用检查方法
        instance = cls()
        if instance.is_valid_image(image):
            # 图像有效，节点正常执行
            return float("inf")
        else:
            # 图像无效，节点禁用
            return None

NODE_CLASS_MAPPINGS = {
    "ImageAutoDisableNode": ImageAutoDisableNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ImageAutoDisableNode": "Image Auto Disable Node",
}