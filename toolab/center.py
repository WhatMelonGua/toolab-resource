#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# # # # # # # # # # # # 
"""
 ╭───────────────────────────────────────╮  
 │ center.py   2024/7/11-13:22
 ╰───────────────────────────────────────╯ 
 │ Description:
    Save Custom Tool env by pickle lib
"""  # [By: HuYw]

# region |- Import -|
from . import io
from importlib import import_module
from pathlib import Path
import shutil
import pickle   # save env data
import sys
import os
# endregion

ENV_ROOT = Path(os.path.normpath(f"{io.getScriptDir(__file__)}/envs"))

def browser():
    """
    查看当前存在的环境名称
    :return:
    """
    envs = os.listdir(ENV_ROOT)
    for i, e in enumerate(envs):
        fname, ftype = os.path.splitext(e)
        if ftype == ".pkl":
            print(f"{i} -\t{fname}")

# region |- Class Env-Data -|
class Domain:
    def __init__(self, data={}):
        assert isinstance(data, dict)
        self.data = data
    def __setitem__(self, key, val):
        self.data[key] = val
    def __getitem__(self, key):
        return self.data.get(key)
    def __str__(self):
        return str(self.data)
# endregion

# region |- Main Class Env -|
class Environment:
    ROOT = ENV_ROOT
    path = None     # lib path
    engine = None   # lib object
    def __init__(self, name):
        self.name = name
        self.domain = Domain()
    def linklib(self, path):
        """
        声明环境的import 绝对路径

        :param path: 例子如 [disk/user/mylib]
        :return:
        """
        self.path = os.path.normpath(path)
        return self
    def drive(self):
        sys.path.insert(0, os.path.dirname(self.path))
        self.engine = import_module(os.path.basename(self.path))
        sys.path.pop(0)  # Delete path
        return self.engine
    def save(self, safe=True):
        """
        储存该环境文件, 之后可以随时加载

        :param safe: 安全模式, 默认开启 ——当存在env时提示是否覆盖, 否则将直接覆盖
        :return:
        """
        assert os.path.isabs(self.path), "Environment path must be an Absolute Path"    # 仅支持绝对定位 & 目录
        assert os.path.isdir(self.path), "Environment path can only be a Dir"
        save_path = os.path.normpath(self.ROOT / f'{self.name}.pkl')
        if os.path.exists(save_path):
            status = True and safe
            while status:
                replace = input(f"There has been an env called: {self.name}, overwrite ?(yes/no)\n")
                if replace == 'yes':
                    break
                elif replace == 'no':
                    return
                else:
                    continue
        # store as name.pkl
        with open(save_path, "wb") as cfg:
            pickle.dump({
                "name": self.name,
                "path": self.path,
                "domain": self.domain,
            }, cfg)
        print(f"Environment [{self.name}] has been saved to: {save_path}")
        return self
    def __construct(self, name, domain, path):
        self.name = name
        self.domain = domain
        self.linklib(path)
    def load_pkl(self, name):
        """
        由环境名称/路径 加载

        :param name: 环境名称
        :return:
        """
        assert not os.path.isabs(name), "Environment Name illegal, browser by function: center.browser()"
        env_file = self.ROOT / f'{name}.pkl'
        with open(env_file, "rb") as cfg:
            cfg = pickle.load(cfg)
        # make
        self.__construct(
            name=cfg['name'],
            domain=cfg['domain'],
            path=cfg['path']
        )
        return self
    def load_path(self, path):
        """
        load from one export dir path
        :param path: the 'path' of self.export
        :return:
        """
        assert os.path.isabs(path), "Environment Path illegal, must be an Absolute Path"
        path = Path(os.path.normpath(path))
        # load domain data
        with open(path / "domain.pkl", "rb") as dom:
            domain = pickle.load(dom)
        # make
        self.__construct(
            name=os.path.basename(path),
            domain=domain,
            path=path / "engine"
        )
        return self
    def load(self, name):
        if os.path.isabs(name):
            self.load_path(name)
        else:
            self.load_pkl(name)
    def rename(self, name):
        self.name = name
        return self
    def export(self, path):
        """
        将Engine目录 即 domain数据导出至该路径 path

        :param path: 导出路径
        :return:
        """
        path = Path(os.path.normpath(path))
        if not os.path.exists(path):
            os.mkdir(path)
        # make sure
        engine_path = path / "engine"
        if os.path.exists(engine_path):
            status = True
            while status:
                replace = input(f"Dir has been existed [{engine_path}], overwrite ?(yes/no)\n")
                if replace == 'yes':
                    shutil.rmtree(engine_path)
                    break
                elif replace == 'no':
                    return
                else:
                    continue
        shutil.copytree(self.path, engine_path)     # 复制engine
        # store domain data
        with open(path / "domain.pkl", "wb") as dd:
            pickle.dump(self.domain, dd)
        print(f"Env export to: {path}\n Named as [{os.path.basename(path)}]")
    def delete(self):
        """
        删除对应 name 的环境文件
        :param name:
        :return:
        """
        envs = os.listdir(self.ROOT)
        for e in envs:
            fname, ftype = os.path.splitext(e)
            if ftype == ".pkl" and fname == self.name:
                os.remove(self.ROOT / e)
                print(f"Env File [{e}] has been removed")
                return
        print(f"Failed! Env [{self.name}] not found, use 'center.browser()' to list all envs.")
# endregion


