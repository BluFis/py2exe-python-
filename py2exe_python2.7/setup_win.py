# -*- coding: utf-8 -*-
from distutils.core import setup

import py2exe

includes = ["encodings", "encodings.*"]

options = {"py2exe":

               {"compressed": 1,#压缩

                "optimize": 2,

                "includes": includes,

                "bundle_files": 3#所有文件打包成一个exe文件,64位环境下不支持

                }

           }

setup(

    version="1.0.0",

    description="url编码工具 python2.7",

    name="url编码工具",

    zipfile=None,

    windows=["win_app.py"],

)