from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from ...models import Post
from .serializers import PostSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser




# data = {
#     'id':1,
#     'title':'hello'
# }

# model to set auth (IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser)
@permission_classes([IsAuthenticated])
@api_view()
def post_list(request):
    if request.method =='GET':
        post = Post.objects.filter(status=True)
        serializer = PostSerializer(post,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # else:
        #     return Response (serializer.errors)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
     

@api_view(["GET","PUT","DELETE"])
def post_detail(request,id):
    # try:
    #     post = Post.objects.get(pk=id)
    #     # print(post.__dict__)
    #     serializer = PostSerializer(post)
    #     # print(serializer.data)
    #     return Response(serializer.data)
    # except Post.DoesNotExist:
        # return Response({"detail":"post dose not exist"},status=status.HTTP_404_NOT_FOUND)
    
        post = get_object_or_404(Post, pk=id, status=True)
        if  request.method == 'GET':
            serializer = PostSerializer(post)
            return Response(serializer.data)
        elif request.method == "PUT":
            serializer = PostSerializer(post, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        elif request.method == "DELETE":
            post.delete()
            return Response({"detail":"Item removed successfully"},status=status.HTTP_204_NO_CONTENT)
            
