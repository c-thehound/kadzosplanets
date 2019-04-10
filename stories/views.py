from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Story
from .serializers import StorySerializer

@api_view(['GET'])
def story(request,pk):
    
    story = Story.objects.get(pk = pk)
    serializer = StorySerializer(story)

    return Response(serializer.data)