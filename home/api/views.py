from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializer

from .models import Todo
# Create your views here.

#@api_view(['GET'])
#def apiOverview(request):
#	api_urls = {
#		'List':'/task-list/',
#		'Detail View':'/task-detail/<str:pk>/',
#		'Create':'/task-create/',
#		'Update':'/task-update/<str:pk>/',
#		'Delete':'/task-delete/<str:pk>/',
#		}
#
#	return Response(api_urls)
#

#def frontend(request):
    




@api_view(['GET'])
def todoList(request):
	todo = Todo.objects.all().order_by('-id')
	serializer = TodoSerializer(todo, many=True)
	return Response(serializer.data)


@api_view(['GET'])
def todoDetail(request, pk):
	todo = Todo.objects.get(id=pk)
	serializer = TodoSerializer(todo, many=False)
	return Response(serializer.data)



@api_view(['POST'])
def todoCreate(request):
	serializer = TodoSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def todoUpdate(request, pk):
	todo = Todo.objects.get(id=pk)
	serializer = TodoSerializer(instance=todo, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def todoDelete(request, pk):
	todo = Todo.objects.get(id=pk)
	todo.delete()

	return Response('Item succsesfully delete!')