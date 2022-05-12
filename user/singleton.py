#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : singleton.py
@Time : 5/12/22 1:20 PM
@Desc: 
"""
from django.db import models


class SingletonBaseModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj
