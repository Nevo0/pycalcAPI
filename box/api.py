from rest_framework.decorators import api_view
from rest_framework.response import Response
from box.models import Order
from .serializers import OrderSerializers
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import json
from rest_framework.parsers import JSONParser


@api_view(['GET', 'POST'])
def seveOrder(request):
    print(request)
    routes = [
        'GET /',
        'GET /api/rooms',
        'GET /api/rooms/:id',
    ]
    if request.method == "POST":
        array = []
        print("POST")
        name = request.POST.get('name')
        email = request.POST.get('email')
        company = request.POST.get('company')
        panels = request.POST.get('panels')
        json_mylist = json.dumps(panels, separators=(',', ':'))
        loads = json.loads(panels)
        array.append(name)
        array.append(email)
        array.append(company)
        array.append(loads)
        serializer = OrderSerializers(
            data={'email': email, 'name': name, 'company': company, })
        print(serializer.is_valid())
        print(serializer.errors)
        if serializer.is_valid():
            print("done")
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    return Response(routes)
