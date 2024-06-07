from ninja import NinjaAPI
from mock.api import mock_router
from mock.models import MockModel
from mock.util import dynamicroute

api = NinjaAPI(csrf=True)


api.add_router('mock/', mock_router)
api.add_router('', dynamicroute)