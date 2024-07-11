#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# # # # # # # # # # # # 
"""
 ╭───────────────────────────────────────╮  
 │ time.py   2024/7/11-12:00
 ╰───────────────────────────────────────╯ 
 │ Description:
    
"""  # [By: HuYw]

# region |- Import -|
from toolab import timeClock
import time
# endregion

clock = timeClock.Clock()
clock.tick("test")
time.sleep(3)
clock.tick("test")
clock.tick("test")  # x3
clock.tick("other")
clock.tick("other") # x2

print(f"Now, the time is: {clock}")
print("Add " + clock + " Radd")
print(clock.toDataFrame("s"))
print(clock.toDataFrame("m"))
print(clock.toDataFrame("h"))
clock.delTick("test")
print(clock.toDataFrame())

