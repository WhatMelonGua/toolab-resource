#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# # # # # # # # # # # # 
"""
 ╭───────────────────────────────────────╮  
 │ t_env.py   2024/7/11-21:56
 ╰───────────────────────────────────────╯ 
 │ Description:
    
"""  # [By: HuYw]

# region |- Import -|
from toolab import center
# endregion

lab = center.Environment("toolab")
lab.linklib('abspath/of/toolab')
engine = lab.drive()
lab.save(safe=True)
lab.export('./export')
lab.load('abspath/of/export')