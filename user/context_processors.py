#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : context_processors.py
@Time : 5/12/22 1:25 PM
@Desc: 
"""

from .models import SiteSetting


def site_settings(request):
    return {
        "site_settings": SiteSetting.load()
    }
