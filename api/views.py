from os import stat
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .serializers import TodoSerializer
from .models import Todo

@api_view(['GET', 'POST'])
def todo_list(request):

	if request.method == 'GET':
		todos = Todo.objects.all().order_by('-updatedAt')
		serializer = TodoSerializer(todos, many=True)
	
	if request.method == 'POST':
		serializer = TodoSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()

	return Response(serializer.data)  

@api_view(['PATCH', 'DELETE'])
def single_todo(request, pk):
	todo = Todo.objects.get(pk=pk)
	serializer = TodoSerializer(instance=todo, data=request.data)

	if request.method == 'PATCH':
		if serializer.is_valid():
			serializer.save()
		return Response(serializer.data)
	
	if request.method == 'DELETE':
		todo.delete()
		return Response(status=status.HTTP_200_OK)


