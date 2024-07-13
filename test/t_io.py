#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# # # # # # # # # # # # 
"""
 ╭───────────────────────────────────────╮  
 │ t_io.py   2024/7/11-20:34
 ╰───────────────────────────────────────╯ 
 │ Description:
    主要测试 内存不足的Promise操作
    模拟Linux下的内存不足，教程源自：https://www.jianshu.com/p/b6fb59508c7b
"""  # [By: HuYw]

# region |- Import -|
import toolab
# endregion
print(toolab.io.getScriptDir(__file__))
print(toolab.io.getRunDir())


pio = toolab.io.PromiseIO()

# pio.applyBlock('test', 4)