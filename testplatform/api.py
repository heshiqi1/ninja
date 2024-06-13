from ninja import NinjaAPI
from mock.api import mock_router
from mock.util import dynamicroute
from user.api import router as user_router
from user.authentication import AuthBear

api = NinjaAPI(auth=AuthBear())


@api.get("/token", auth=None)
def token(request):
    return {"token": request.auth}


api.add_router('/mock/', mock_router)
api.add_router('/user/', user_router)
api.add_router('', dynamicroute)  #动态路由要放到最后，这个优先级最低
