from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from django.contrib.auth.models import Group
from rest_framework.mixins import ListModelMixin, CreateModelMixin
 
from .serializers import GroupsSerializer
 
@api_view()
def hello_world_view(requestr: Request):
    return Response({"message": "Hello World!"})
      
      
class GroupListView(ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupsSerializer
     
    