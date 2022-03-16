from rest_framework.decorators import api_view
from rest_framework.response import Response
from box.models import Box
from .serializers import BoxSerializers, TerminaSerializers
from django.http import HttpResponse, JsonResponse
from django.core import serializers


@api_view(['GET', 'POST'])
def getRoutes(request):
    print(request)
    routes = [
        'GET /',
        'GET /api/rooms',
        'GET /api/rooms/:id',

    ]
    return Response(routes)


@api_view(['GET'])
def getProjekts(request):
    projets = Box.objects.all()
    serialized_queryset = serializers.serialize('json', projets)
    # many=True dlatego ze bedzie wiele obiektów
    serializer = BoxSerializers(projets, many=True)
    # serializer = TerminaSerializers(projets, many=True)
    # trzeba dodac data atrybut
    return Response(serializer.data)
    # trzeba dodac data atrybut
    return JsonResponse(max_hubs_side_c_d)


@api_view(['GET'])
def getProjekt(request, pk):
    projets = Box.objects.get(id=pk)
    # many=True dlatego ze bedzie wiele obiektów
    serializer = BoxSerializers(projets, many=False)
    return Response(serializer.data)  # trzeba dodac data atrybut
    # trzeba dodac data atrybut
    return JsonResponse(serializer.data, safe=False)
