# coding=utf-8
import logging

__author__ = 'superewg'
X = 100
Y = 100
ALL = {}  # 所有细胞

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    # filename='myapp.log',
                    filemode='w')
