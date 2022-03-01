#!/usr/bin/python3
# -*- coding: utf-8 -*-


from django.db import DatabaseError
from django.http.response import JsonResponse
from django.http import HttpResponseServerError
from django.middleware.common import MiddlewareMixin

from utils.result import R
from utils.enums import StatusCodeEnum
from toolSystem.exceptions.business_exception import BusinessException

from loguru import logger


class ExceptionMiddleware(MiddlewareMixin):
    """统一异常处理中间件"""

    @staticmethod
    def process_exception(request, exception):
        """
        统一异常处理
        :param request: 请求对象
        :param exception: 异常对象
        :return:
        """
        if isinstance(exception, BusinessException):
            # 业务异常处理
            data = R.set_result(exception.enum_cls).data()
            return JsonResponse(data)

        elif isinstance(exception, DatabaseError):
            # 数据库异常
            data = R.set_result(StatusCodeEnum.DB_ERR).data()
            logger.error(data)
            # return HttpResponseServerError(StatusCodeEnum.DB_ERR.errmsg)
            return JsonResponse(data)

        elif isinstance(exception, Exception):
            # 服务器异常处理
            r = R.server_error()
            data = r.data()
            logger.error(data)
            # return HttpResponseServerError(r.msg)
            return JsonResponse(data)
        return None
