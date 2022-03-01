# coding:utf-8
from django.http import JsonResponse
from utils import jwt
from functools import wraps
from .result import R
from utils.enums import StatusCodeEnum


def auth(permission):
    def decorator(func):
        @wraps(func)  # 加上此装饰器后被装饰的函数名和函数的doc不会发生改变
        def returned_wrapper(request, *args, **kwargs):
            jwt_token = request.META.get("HTTP_JWT_TOKEN")
            print(request.META.get("HTTP_HOST"))
            print(jwt_token)
            info = jwt.analysis_token(jwt_token)
            if permission == "abc":
                f = func(request, *args, **kwargs)
                return f
            else:
                return JsonResponse(R.set_result(StatusCodeEnum.NO_PERMISSION).data())

        return returned_wrapper

    return decorator
