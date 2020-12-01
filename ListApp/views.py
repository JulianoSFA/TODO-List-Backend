from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser 
from rest_framework import status
from ListApp.models import ListItem
from ListApp.serializers import ListSerializer

# Create your views here.

@csrf_exempt
def List_Edit(request):
    if request.method == 'GET':
        List_All = ListItem.listItem.all()
        List_Serializer = ListSerializer(List_All, many=True)
        return JsonResponse(List_Serializer.data, safe=False)

    elif request.method == 'POST':
        listItem_Data = JSONParser().parse(request)
        List_Serializer = ListSerializer(data=listItem_Data)
        if List_Serializer.is_valid():
            List_Serializer.save()
            return JsonResponse(List_Serializer.data)
        return JsonResponse(List_Serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt 
def TODO_detail(request, pk):
    try: 
        todo = ListItem.listItem.get(pk=pk)
    except ListItem.listItem.DoesNotExist: 
        return HttpResponse(status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        List_Serializer = ListSerializer(todo) 
        return JsonResponse(List_Serializer.data) 
 
    elif request.method == 'PUT': 
        ListItem_Data = JSONParser().parse(request) 
        List_Serializer = ListSerializer(todo, data=ListItem_Data) 
        if List_Serializer.is_valid(): 
            List_Serializer.save() 
            return JsonResponse(List_Serializer.data) 
        return JsonResponse(List_Serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        todo.delete() 
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)