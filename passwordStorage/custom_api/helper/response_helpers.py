
from rest_framework.response import Response

def error_response(status, msg, data, *args, **kwargs):
    response = {
        "status_code": status,
        "status": "failure",
        "detail": msg,
        "data": data,
    }

    return Response(data=response, status=status)

def success_response(status, msg, data,**kwargs):
    response = {
        "status_code": status,
        "status": "success",
        "detail": msg,
        "data": data,
    }
    if kwargs:
        response.update(**kwargs)
    return Response(data=response, status=status)
