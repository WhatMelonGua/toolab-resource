#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# # # # # # # # # # # # 
"""
 ╭───────────────────────────────────────╮  
 │ utils.py   2024/7/11-11:47
 ╰───────────────────────────────────────╯ 
 │ Description:
    
"""  # [By: HuYw]

# region |- Import -|
# import sys
# sys.path.append("../")
import toolab
# endregion

logger = toolab.logger.get()
logger.info("Log Test")

def log(any):
    logger.warn(any)


log("any")