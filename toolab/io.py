#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# # # # # # # # # # # # 
"""
 ╭───────────────────────────────────────╮  
 │ io.py   2024/7/11-20:26
 ╰───────────────────────────────────────╯ 
 │ Description:
    
"""  # [By: HuYw]

# region |- Import -|
from pathlib import Path
import sys
import os
# endregion

def getRunDir():
    return os.path.normpath(os.getcwd())

def getScriptDir(file=__file__):
    try:
        return os.path.normpath(os.path.split(os.path.realpath(file))[0])
    except Exception as e:
        print("Interactive Mods, get path: current dir")
        return getRunDir()


# region |- Main Class Promise-IO -|

# endregion