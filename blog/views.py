from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BlogPost
from .serializers import BlogSerializer

@api_view(['GET'])
def post(request,pk):

    post = BlogPost.objects.get(pk = pk)
    snippet = post.content[0:150]
    data = {
        "id":post.id,
        "title":post.title,
        "content":post.content,
        "snippet":snippet+'...',
        "uploades":post.uploaded
    }

    return Response(data)