# -*- coding: utf-8 -*-
from distutils.core import setup

import py2exe

options = {"py2exe":

               {"compressed": 1,#压缩

                "optimize": 2,

                "bundle_files": 3#所有文件打包成一个exe文件,64位环境下不支持

                }

           }

setup(

    version="1.0.0",

    description="url编码工具 python3.4",

    name="url编码工具",

    options=options,

    zipfile=None,

    windows=["win_app.py"],

)