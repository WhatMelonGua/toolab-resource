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
from toolab import logger
import pandas as pd
# endregion

logger = logger.get("test.log")
logger.info("Log Test")

# test str
fr = pd.DataFrame([[0, 0], [1, 1]], columns=['A', 'B'])
logger.error(fr)

def log(any):
    logger.warn(any)


log("any")