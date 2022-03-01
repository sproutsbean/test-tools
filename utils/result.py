#!/usr/bin/python3
# -*- coding: utf-8 -*-

from .enums import StatusCodeEnum
from django.http import JsonResponse


class R(object):
    """
    统一项目信息返回结果类
    """

    def __init__(self):
        self.code = None
        self.msg = None
        self._data = dict()

    @staticmethod
    def ok(data=None):
        """
        组织成功响应信息
        :return:
        """
        context = {
            'code': StatusCodeEnum.OK.code,
            'msg': StatusCodeEnum.OK.errmsg,
            'data': data
        }
        # r = R()
        # r.code = StatusCodeEnum.OK.code
        # r.msg = StatusCodeEnum.OK.errmsg
        return JsonResponse(context)

    @staticmethod
    def error():
        """
        组织错误响应信息
        :return:
        """
        r = R()
        r.code = StatusCodeEnum.ERROR.code
        r.msg = StatusCodeEnum.ERROR.errmsg
        return r

    @staticmethod
    def server_error():
        """
        组织服务器错误信息
        :return:
        """
        r = R()
        r.code = StatusCodeEnum.SERVER_ERR.code
        r.msg = StatusCodeEnum.SERVER_ERR.errmsg
        return r

    @staticmethod
    def set_result(enum):
        """
        组织对应枚举类的响应信息
        :param enum: 状态枚举类
        :return:
        """
        r = R()
        r.code = enum.code
        r.msg = enum.errmsg
        return r

    def data(self, key=None, obj=None):
        """统一后端返回的数据"""

        if key:
            self._data[key] = obj

        context = {
            'code': self.code,
            'msg': self.msg,
            'data': self._data
        }
        return context
