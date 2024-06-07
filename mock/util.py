from django.http import JsonResponse
from ninja import Router
from mock.models import MockModel

dynamicroute = Router()


@dynamicroute.get("{path:path}")
def dynamic_route(request, path: str):
    try:
        print(str(path))
        route = MockModel.objects.get(path=f"/{path}")
        print(route)
        return route.res
    except MockModel.DoesNotExist:
        return JsonResponse({"error": "Route not found"}, status=404)