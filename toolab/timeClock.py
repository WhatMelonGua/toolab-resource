#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# # # # # # # # # # # # 
"""
 ╭───────────────────────────────────────╮  
 │ time.py   2024/7/11-0:27
 ╰───────────────────────────────────────╯ 
 │ Description:
    Time Formatter & Ticker
"""  # [By: HuYw]

# region |- Import -|
import pandas as pd
import datetime
import time
# endregion

# region |- Main Class: Time -|
class Clock:
    def __init__(self):
        self.createTime = time.time()
        self.records = {}
    # print / f"{self}"
    def __str__(self):
        return datetime.datetime.now().strftime("%Y%m%d_%Hh%Mm%Ss")
    # self + other
    def __add__(self, other):
        if isinstance(other, str):
            return str(self) + other
        else:
            raise TypeError("can only concatenate Time to str")
    # other + self
    def __radd__(self, other):
        if isinstance(other, str):
            return other + str(self)
        else:
            raise TypeError("can only concatenate Time to str")
    # get timer / self["tick"]
    def __getitem__(self, item):
        return self.records.get(item, [])
    # function s
    #
    # timer
    def tick(self, name):
        if name in self.records.keys():
            duration = time.time()-self.records[name][-1]
            self.records[name].append(duration)
        else:
            self.records[name] = [time.time()]
    # del timer
    def delTick(self, name):
        if name in self.records.keys():
            del self.records[name]
    # timer dataframe
    def toDataFrame(self, unit="m", ndigits=4):
        """
        Turn self.records to a pandas.DataFrame, with unit transfer & round ndigits

        :param unit: h / m / s  (map to hour/minute/second)
        :param ndigits: round ndigits
        :return:
        """
        if len(self.records) == 0: return pd.DataFrame()
        # unit options
        units = ["s", "m", "h"]
        unit = unit if unit in units else "m"
        unit_exp = units.index(unit)
        # copy
        dictdata = self.records.copy()
        # datafrme 列数
        l = max(len(arr) for arr in dictdata.values())
        for k in dictdata.keys():
            adder = l - len(dictdata[k])
            if adder > 0:
                dictdata[k] = dictdata[k] + [0]*adder
        # make dataframe
        df = pd.DataFrame.from_dict(dictdata)
        # unit
        df = df.div(60**unit_exp)
        df.columns = [f"{name}/{unit}" for name in df.columns]
        return df.round(ndigits)

# endregion

