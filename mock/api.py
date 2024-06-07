from ninja import Router
from mock.models import MockModel
from django.shortcuts import get_object_or_404
from django.forms import model_to_dict
from mock.serializers import MockSchema, ResponSchema


mock_router = Router()


@mock_router.get("/mock/mock2")
def mock2(request):
    return "mock2"


@mock_router.post("/mock", response={200: ResponSchema, 400: ResponSchema})
def create(request, data: MockSchema):
    name = data.dict()["name"]
    try:
        mock_data = MockModel.objects.get_or_create(**data.dict())
        if mock_data[1]:
            return 200, {"body": [{"id": model_to_dict(mock_data[0])["id"]}]}
        else:
            return 400, {"msg": f"{name}已经存在，换个名字"}
    except:
        return 400, {"msg": f"name or path已经存在，换个名字"}


@mock_router.get("/mock")
# @mock_router.get("/mock", response=MockSchema)
def get(request, name: str):
    data = get_object_or_404(MockModel, name=name)
    return model_to_dict(data, exclude=["method"])


# @mock_router.get("/mocks", response=List[MockSchema])
@mock_router.get("/mocks", response={201: ResponSchema, 403: ResponSchema})
def get_list(request):
    try:
        data = MockModel.objects.values()
        return 201, {"body": list(data)}
    except Exception as e:
        return 403, {"msg": e}


@mock_router.put("/mock/{id}")
def put(request, id: int, payload: MockSchema):
    name = payload.dict()["name"]
    data = get_object_or_404(MockModel, id=id)
    for attr, value in payload.dict(exclude_unset=True).items():
        setattr(data, attr, value)
        # data.attr = value
    data.save()
    data = get_object_or_404(MockModel, id=id)
    return model_to_dict(data)


@mock_router.delete("/mock/{id}")
def delete(request, id):
    data = get_object_or_404(MockModel, id=id)
    data.delete()
    return model_to_dict(data)

