from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Task
# Create your views here.

class TaskView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request, pk=None):
        if pk:
            try:
                data = Task.objects.filter(pk=pk, user = request.user)

                status_param = request.GET.get('status')
                priority_param = request.GET.get('priority')

                if status_param:
                    data = data.filter(status=status_param)
                if priority_param:
                    data = data.filter(priority=priority_param)

                serializer = TaskSerializer(data, many=True)

                return Response({
                    'data': serializer.data,
                    'message': "Tasks fetched"
                }, status= status.HTTP_200_OK)

            except Exception as e:
                return Response(
                        {
                            "data" : {},
                            "message": "Error occured"
                        }, status = status.HTTP_400_BAD_REQUEST
                    )
        try:
            data = Task.objects.filter(user = request.user).order_by("status")

            status_param = request.GET.get('status')
            priority_param = request.GET.get('priority')

            if status_param:
                data = data.filter(status=status_param)
            if priority_param:
                data = data.filter(priority=priority_param)

            serializer = TaskSerializer(data, many=True)

            return Response({
                'data': serializer.data,
                'message': "Tasks fetched"
            }, status= status.HTTP_200_OK)

        except Exception as e:
            return Response(
                    {
                        "data" : {},
                        "message": "Error occured"
                    }, status = status.HTTP_400_BAD_REQUEST
                )

    def post(self, request):

        try:
            data = request.data
            data['user'] = request.user.id
            serializer = TaskSerializer(data = data)

            if not serializer.is_valid():
                return Response(
                    {
                        "data" : serializer.errors,
                        "message": "Error occured"
                    }, status = status.HTTP_400_BAD_REQUEST
                )
            
            serializer.save()

            return Response({
                'data': serializer.data,
                'message': "Task created"
            }, status= status.HTTP_201_CREATED)


        except Exception as e:
            return Response(
                    {
                        "data" : {},
                        "message": "Error occured"
                    }, status = status.HTTP_400_BAD_REQUEST
                )
        
    def patch(self, request, pk=None):
        if not pk:
            return Response(
                {
                    "date": {},
                    "message": "Task ID is required"
                }, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            data = Task.objects.get(pk=pk, user=request.user)
            serializer = TaskSerializer(data, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response({
                    "data": serializer.data,
                    "message": "Task updated"
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "data": serializer.errors,
                    "message": "Error updating task"
                }, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            print(e)
            return Response({"message": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, pk=None):
        if not pk:
            return Response(
                {
                    "date": {},
                    "message": "Task ID is required"
                }, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            data = Task.objects.get(pk=pk, user=request.user)
            
            data.delete()
            return Response({
                "data": {},
                "message": "Task deleted"
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            print(e)
            return Response({"message": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
        
class DashboardView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        user = request.user
        data = Task.objects.filter(user=user)
        total = data.count()
        completed = data.filter(status='Completed').count()
        pending = data.filter(status='Pending').count()

        serializer = TaskSerializer(data.order_by('-due_date'), many=True)

        return Response({
            "data": {
                "total_tasks": total,
                "completed_tasks": completed,
                "pending_tasks": pending,
            },
            "tasks": serializer.data
        }, status=status.HTTP_200_OK)