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
import time
from pathlib import Path
from contextlib import contextmanager
import shutil   # 查询磁盘剩余空间
import sys
import os
# endregion

System = sys.platform   # System

def isWin():
    return System.lower().find("win") >= 0

def isLinux():
    return System.lower().find("linux") >= 0

def getRunDir():
    return os.path.normpath(os.getcwd())

def getScriptDir(file=__file__):
    try:
        return os.path.normpath(os.path.split(os.path.realpath(file))[0])
    except Exception as e:
        print("Interactive Mods, get path: current dir")
        return getRunDir()


# region |- Main Class Promise-IO -|
class PromiseIO:
    units = ['b', 'kb', 'mb', 'gb']
    unit = 'gb'
    def __init__(self, root='./', unit='gb', block_dir=None):
        """
        初始化

        :param root: 要执行监管操作的root目录 (输出目录)
        :param unit: 使用的内存单位 'b', 'kb', 'mb', 'gb'
        :param block_dir: 存放block的目录名称
        """
        unit = unit.lower()
        assert unit in self.units, "PromiseIO unit only can be b, kb, mb, gb!"
        self.root = Path(os.path.abspath(root))     # abs path
        self.unit = unit
        self.factor = 1024**self.units.index(self.unit)  # 计算内存的缩放因子
        # block system
        block_dir = block_dir or 'block.tmp'
        self.block_dir = self.root / block_dir
        self.block_ind = 0
        self.block_queue = {}   # size: block list
    @contextmanager
    def write(self, path: str, memory=1, max_try=-1, delay=10, mode=0o755):
        """
        涉及系统写入操作的 许诺上下文管理器

        :param path: 监测的 写入路径, 若是目录请在后方以目录符 '/' 封尾
        :param memory: 触发写入的最小剩余空间 单位根据初始化相关
        :param max_try: 最大尝试次数, -1/0代表始终尝试(默认-1)
        :param delay: 轮询磁盘空间时间
        :return:
        """
        # update inputs param
        t_dir = os.path.normpath(os.path.dirname(path))   # use str format
        memory *= self.factor
        path = Path(path)   # turn to Path format
        # prepare dir
        if not os.path.isdir(t_dir):
            os.makedirs(t_dir, mode=mode)
        # start
        attempts = 0    # try times record
        while max_try > 0 and attempts < max_try:
            attempts += 1
            # 轮询
            left_memory = shutil.disk_usage(t_dir).free
            if left_memory < memory:
                time.sleep(delay)
                continue    # step in next query
            try:
                yield path
                break
            except Exception as e:
                print(f"Promise Try [{attempts}] times Failed, Exception:\n{e}")
                continue
    def createBlockFile(self, memory=1, unit=None, mode=0o755):
        unit = unit or self.unit
        assert unit in self.units, "PromiseIO unit only can be b, kb, mb, gb!"
        # 将memory unit转换为字节
        factor = 1024**self.units.index(unit)
        memory = memory * factor
        self.block_ind += 1
        if not os.path.isdir(self.block_dir):
            os.makedirs(self.block_dir, mode=mode)
        # sure key val
        fname = f'apply{self.block_ind}.block'
        # create
        with open(self.block_dir/fname, 'wb') as f:
            # 写入一个字节作为开始
            f.write(b'\x00')
            # 直接跳到文件的末尾
            f.seek(memory - 2)
            # 写入一个字节到文件的最后一个位置, 达到指定大小
            f.write(b'\x00')
        # end
        return fname
    def applyBlock(self, name, memory=1, unit=None, mode=0o755):
        # if exists, del first
        if name in self.block_queue.keys():
            self.releaseBlock(name)
        # create
        fname = self.createBlockFile(memory, unit, mode)
        self.block_queue[name] = fname
        print(f"Promise Block[{name}] created in: {self.block_dir/fname}")
        #
    def releaseBlock(self, name):
        if name in self.block_queue.keys():
            os.remove(self.block_dir/self.block_queue[name])
        else:
            print(f"Promise Block Queue Not existed {name}, {list(self.block_queue.keys())}")
    def cleanBlock(self):
        for k, v in self.block_queue.items():
            try:
                os.remove(self.block_dir/self.block_queue[k])
                print(f"Block Clean: [{k}: {v}]")
            except Exception as e:
                print(f"Promise remove Block [{k}: {v}] with Error: {e}")
        # 删除文件夹
        try:
            shutil.rmtree(self.block_dir)
            print("Promise All tmp Block has been removed")
        except Exception as e:
            pass


# endregion