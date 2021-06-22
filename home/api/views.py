from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializer
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime

from .models import Todo

from django.contrib.auth import get_user_model
User = get_user_model()

from django.contrib.auth import logout

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
    
@api_view(['POST'])
def todoLogin(request):
        username = request.data['username']
        password = request.data['password']

        user = User.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', 'HS256').decode('utf-8')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
#        print(token)
        
        return response
    
@api_view(['POST'])
def todoLogout(request):
#    logout(request)
#    response = redirect('/')
    response = Response()
    response.delete_cookie('jwt')
#    token = request.COOKIES.get('jwt')
#    print(token)
    response.data = {
        'message': 'Logged Out Successfully'
    }
    return response


@api_view(['GET'])
def todoList(request):
    token = request.COOKIES.get('jwt')

    if not token:
       raise AuthenticationFailed('Unauthenticated!')

    print(token)

    try:
       decoded = jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
       raise AuthenticationFailed('Unauthenticated!')

    print(decoded['id'])
    todo = Todo.objects.filter(user=decoded['id']).order_by('-id')
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
