from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Houses,Users
from.favorites import Favorites
# Create your views here.
@api_view(['POST'])
def register(request):
    """
    注册接口
    请求体: {
        "username": "zhangsan",
        "password": "123456",
        "phone": "13800138000",
        "email": "test@example.com",
        "real_name": "张三"
    }
    """
    try:
        phone=request.data.get("phone")
        email=request.data.get("email")
        real_name=request.data.get("real_name")
        # if not password:
        #     return Response({
        #         "code":400,"message":"密码不能为空"
        #     },status=status.HTTP_400_BAD_REQUEST
        #     )

        # pyrefly: ignore [missing-attribute]
        if Users.objects.filter(phone=phone).exists():
            return Response({"code":400,"message":"手机号已被注册"
            },status=status.HTTP_400_BAD_REQUEST
            )
        # pyrefly: ignore [missing-attribute]
        user=Users.objects.create(
            phone=phone,
            email=email,
            real_name=real_name,
            role="租客",
            status="正常")
        return Response({
             'code': 200,
            'message': '注册成功',
            'data': {
                'phone': user.phone,
            }
        }, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response(
            {'code': 500, 'message': f'注册失败: {str(e)}'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['POST'])
def login(request):
    """
    登录接口
    请求体: {
        "phone": "",
        "password": "123456"
    }
    """
    try:
        # 1. 获取参数
        phone = request.data.get('phone')
        
        # 2. 参数校验
        if not phone:
            return Response(
                {'code': 400, 'message': '用户名和密码不能为空'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # 3. 查询用户
        try:
            # pyrefly: ignore [missing-attribute]
            user = Users.objects.get(phone=phone)
        # pyrefly: ignore [missing-attribute]
        except Users.DoesNotExist:
            # 为了安全，不要明确说"用户不存在"，统一说"用户名或密码错误"
            return Response(
                {'code': 401, 'message': '用户名或密码错误'},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        # 4. 检查用户状态
        if user.status != '正常':
            return Response(
                {'code': 403, 'message': f'账户状态：{user.status}，请联系管理员'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        # 5. 验证密码
        # if not check_password(password, user.password):
        #     return Response(
        #         {'code': 401, 'message': '用户名或密码错误'},
        #         status=status.HTTP_401_UNAUTHORIZED
        #     )
        
        # 6. 生成 JWT Token
        # pyrefly: ignore [bad-specialization]
        refresh = RefreshToken.for_user(user)
        
        # 7. 返回成功信息
        return Response({
            'code': 200,
            'message': '登录成功',
            'data': {
                'access': str(refresh.access_token),
                'refresh': str(refresh),
                'user': {
                    'user_id': user.user_id,
                    'username': user.username,
                    'real_name': user.real_name,
                    'phone': user.phone,
                    'email': user.email,
                    'role': user.role
                }
            }
        }, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response(
            {'code': 500, 'message': f'登录失败: {str(e)}'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['PATCH'])
def update_user_to_landlord(request):
    """
    将用户角色更新为房东
    请求体: {
        "phone": ”12345678901”,
    }
    """
    try:
        phone=request.data.get('phone')
        if(not phone):
            return Response({
                "code":"400",
                "massage":"用户手机不能为空"
            },status=status.HTTP_400_BAD_REQUEST)
        try:
            user=Users.objects.get(phone=phone)
        except Users.DoesNotExist:
            return Response({
                'code':'400','message':'所请求的用户不存在！'
            },status=status.HTTP_400_BAD_REQUEST)
        if user.role=="业主":
            return Response({
                "code":"400",
                "message":"用户已是房东"
            },status=status.HTTP_400_BAD_REQUEST)
        user.role="业主"
        user.save()
        return Response({
            "code":"200","message":"successs!"

        },status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            'code':'500','message':f'切换失败{str(e)}'
        },status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def add_favor(request):
    """
    {
    'phone':"1",
    "house_id":""
    }
    """
    phone=request.data.get('phone')
    house_id=request.data.get('house_id')
    if not Favorites.objects.filter(house_id=house_id and phone=phone)
    return Response({
        'code':'200','message':'suceess!'
    },status=status.HTTP_200_OK)