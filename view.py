# coding=utf-8
from tkinter import *
import config


def get_tk():
    """
    获得一个TK对象
    :return:Tk()
    """
    return Tk()


def set_tk(tk, title, size):
    """设置窗口大小，size的格式为：widthxheight,如：size = '200x100'."""
    tk.title(title)
    tk.geometry(size)


def get_canvas(tk, bg):
    return Canvas(tk, bg=bg, height=config.Y * 5, width=config.X * 5)
