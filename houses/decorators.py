from functools import wraps
from rest_framework.response import Response
from rest_framework import status



def role_required(*roles):
    def decorator(view_func):
        @wraps(view_func)
        def wapper(request,*args, **kwargs):
            user=request.user
            if not user:
                return Response({
                    'code':'401','detail':'未认证用户访问！'
                },status=status.HTTP_401_UNAUTHORIZED)
            return view_func(request,*args, **kwargs)
        return wapper
    return decorator