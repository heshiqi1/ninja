from typing import Any
from django.http import HttpRequest
from ninja.security import APIKeyHeader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from ninja import Router
from user.serializer import UserSchema
from user.models import UserToken
from django.forms import model_to_dict
from django.http import JsonResponse


router = Router(tags=["user"])


#自定义认证器
class GlobalAuth(APIKeyHeader):
  def authenticate(self, request, key):
    try:
      token = key.split("")[1]
      user = User.objects.get(auth_token=token)
      return user.token
    except User.DoesNotExist:
      return "用户过期或者不存在"


@router.get("/login")
# @mock_router.get("/mock", response=MockSchema)
def get(request, name: str):
    return {"name": name}


@router.post("/register")
def register(request, body: UserSchema):
    username = body.username
    password = body.password
    email = body.email
    try:
        if username and password and email:
            user = User.objects.create_user(username, email, password)
            print(user)
            return {"msg": f"创建用户{user.username}"}
        else:
            return {"msg": "注册需要填写账号、密码和邮箱"}
    except Exception as e:
        return {"msg": f"创建用户{username}失败","res":e}


@router.post("/login", auth=None)
def login(request, body: UserSchema):
    # 用户对象 (假设已经通过其他方式获取)
    is_user = authenticate(**body.dict())
    print(is_user)
    if is_user:
        user = User.objects.get(username=body.username)
        # 获取或创建与用户关联的 Token 对象
        token, created = UserToken.objects.get_or_create(user=user)
        if created:
            print(f"Created new token: {token.token}")
        else:
            print(f"Retrieved existing token: {token.token}")
        # 打印 Token 对象的详细信息
        return(f"Token details: Bearer {token.token}")
    else:
       return JsonResponse({"msg": f"当前用户{body.username}账号密码是否正确或者是否用户存在"}, status=404)


@router.post("/logout")
def logout(request):
   token = request.auth
   print(f"token{token}")
   if token:
      try:
          token_obj = UserToken.objects.get(token=token)
          token_obj.delete()
          return JsonResponse({"msh": "用户退出登录成功"}, status=200)
      except UserToken.DoesNotExist:
          return JsonResponse({"msh": "用户token不存在"}, status=404)
