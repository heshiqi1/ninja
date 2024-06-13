from django.contrib.auth.models import User
from django.http import HttpRequest
from ninja.security import HttpBearer
from user.models import UserToken
from django.http import JsonResponse


class AuthBear(HttpBearer):
  def authenticate(self, request: HttpRequest, token: str):
      param_name = "Authorization"
      try:        
        token_obj = UserToken.objects.get(token=token)
        print(f"token_obj:{token_obj}")
        if token_obj is not None:
            return token_obj.token
      except (UserToken.DoesNotExist, IndexError):
          return None