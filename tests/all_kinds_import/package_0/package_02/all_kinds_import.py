#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 1. 标准导入
import datetime

# 2. 多重导入
import json
import os

# 4. 带点号的导入
import os.path
import sys
import xml.dom.minidom

# 5. from 导入
from math import pi

# 6. from 多重导入
from os import makedirs, path, remove

# 8. from 带点号导入
from os.path import exists, join
from time import sleep
from xml.dom.minidom import parse

# 3. 带别名的导入
import numpy as np
import pandas as pd

# 7. from 带别名导入
from tensorflow import keras as k
from torch.nn import functional as F

# 9. 相对导入
from ... import module_0
from ...module_1 import functionB
from .. import module_01
from ..package_01 import module_010
from .module_020 import functionA

# 10. 条件导入
try:
    import scipy
except ImportError:
    import numpy


# 11. 函数内导入
def some_function():
    import requests
    from PIL import Image

    return requests, Image


# 12. 类内导入
class SomeClass:
    import threading

    def __init__(self):
        import queue

        self.queue = queue.Queue()

    def method(self):
        from collections import defaultdict

        return defaultdict(list)


# 13. if 条件下的导入
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

# 14. 带 * 的导入
from math import *

# 15. 复杂的 from import
from torch.nn.functional import dropout, gelu, relu
from torch.nn.functional import softmax as soft


# 16. 动态导入 unable to analyze
def dynamic_import():
    module_name = "yaml"
    # 使用 __import__
    yaml1 = __import__(module_name)

    # 使用 importlib
    import importlib

    yaml2 = importlib.import_module(module_name)

    return yaml1, yaml2


# 17. 嵌套的条件导入
try:
    import torch

    try:
        import torch.cuda
    except ImportError:
        import torch.cpu
except ImportError:
    try:
        import tensorflow as tf
    except ImportError:
        import theano


# 18. with 语句中的导入
def with_import():
    with open("test.txt") as f:
        import csv

        return csv


# 19. 在列表/字典推导式中的导入
def comprehension_import():
    return [__import__(x) for x in ["os", "sys", "time"]]


# 20. 异步上下文中的导入
async def async_function():
    import asyncio

    import aiohttp

    return aiohttp, asyncio


if __name__ == "__main__":
    # 实际使用一些导入的模块，防止被优化掉
    print(f"Python version: {sys.version}")
    print(f"Current directory: {os.getcwd()}")
    print(f"Pi value: {pi}")
    print(f"NumPy random: {np.random.rand()}")
