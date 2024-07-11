#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# # # # # # # # # # # # 
"""
 ╭───────────────────────────────────────╮  
 │ __init__.py   2024/7/11-22:21
 ╰───────────────────────────────────────╯ 
 │ Description:
    
"""  # [By: HuYw]

# region |- Import -|
import os
# endregion

def browser():
    """
    查看当前存在的环境名称
    :return:
    """
    envs = os.listdir(os.path.split(os.path.realpath(__file__))[0])
    for i, e in enumerate(envs):
        fname, ftype = os.path.splitext(e)
        if ftype == ".pkl":
            print(f"{i} -\t{fname}")