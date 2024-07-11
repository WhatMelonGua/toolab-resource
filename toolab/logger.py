#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# # # # # # # # # # # # 
"""
 ╭───────────────────────────────────────╮  
 │ logger.py   2024/7/11-2:22
 ╰───────────────────────────────────────╯ 
 │ Description:
    Logger info/ just solve for problem with osError: disk quote!
"""  # [By: HuYw]

# region |- Import -|
import logging
# endregion

def get(path=None, lv=logging.INFO, formats=None):
    # format
    formats = formats or "[%(levelname)s] %(asctime)s: %(message)s, " \
                         "%(filename)s[%(lineno)d] > %(module)s > %(funcName)s"
    formatter = logging.Formatter(formats)
    # get logger from scripts/lib name
    logger = logging.getLogger(__name__)
    logger.setLevel(lv)
    # handler > console / file.txt
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(lv)
    logger.addHandler(console_handler)
    if path is not None:
        file_handler = logging.FileHandler(path, mode='w')
        file_handler.setFormatter(formatter)
        file_handler.setLevel(logging.DEBUG)
        logger.addHandler(file_handler)
    # return
    return logger