from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from ...models import Post, Category
from .serializers import PostSerializer, CategorySerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView
from rest_framework import mixins
from rest_framework import viewsets
from .permission import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
# data = {
#     'id':1,
#     'title':'hello'
# }

# """"""""""""""""""""""""""@api_view(["GET","POST"])""""""""""""""""""""""""""
""" getting a list of post and creating new posts"""
# model to set auth (IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser)
# @api_view(["GET","POST"])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def post_list(request):
#     if request.method =='GET':
#         post = Post.objects.filter(status=True)
#         serializer = PostSerializer(post,many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = PostSerializer(data=request.data)
#         # if serializer.is_valid():
#         #     serializer.save()
#         #     return Response(serializer.data)
#         # else:
#         #     return Response (serializer.errors)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)


""" getting a list of post and creating,delete,update posts"""
# @api_view(["GET","PUT","DELETE"])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def post_detail(request,id):
#     # try:
#     #     post = Post.objects.get(pk=id)
#     #     # print(post.__dict__)
#     #     serializer = PostSerializer(post)
#     #     # print(serializer.data)
#     #     return Response(serializer.data)
#     # except Post.DoesNotExist:
#         # return Response({"detail":"post dose not exist"},status=status.HTTP_404_NOT_FOUND)
    
#         post = get_object_or_404(Post, pk=id, status=True)
#         if  request.method == 'GET':
#             serializer = PostSerializer(post)
#             return Response(serializer.data)
#         elif request.method == "PUT":
#             serializer = PostSerializer(post, data=request.data)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#             return Response(serializer.data)
#         elif request.method == "DELETE":
#             post.delete()
#             return Response({"detail":"Item removed successfully"},status=status.HTTP_204_NO_CONTENT)
            


# """"""""""""""""""""""""""(APIView)""""""""""""""""""""""""""
# class PostList(APIView):
#     """ getting a list of post and creating new posts"""
#     permission_classes =[IsAuthenticated]
#     serializer_class = PostSerializer
    
#     """ retrieving a list of posts"""
#     def get(self,request):
#             post = Post.objects.filter(status=True)
#             serializer = PostSerializer(post,many=True)
#             return Response(serializer.data)
        
#     """creating a post with provided data"""
#     def post(self,request):
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
       
'''class PostDetail(APIView):
    """ getting detail of the post and edit plus removing it"""
    permission_classes =[IsAuthenticated]
    serializer_class = PostSerializer
    
    """retrieving the post data"""
    def get(self,request,id):
        post =  get_object_or_404(Post, pk=id, status=True)
        serializer = self.serializer_class(post)
        return Response(serializer.data)
    """editing the post data"""
    def put(self,request,id):
        post =  get_object_or_404(Post, pk=id, status=True)
        serializer = self.serializer_class(post)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    """ deleting the post object """
    def delete(self,request,id):
        post = get_object_or_404(Post, pk=id, status=True)
        post.delete()
        return Response({"detail":"Item removed successfully"},status=status.HTTP_204_NO_CONTENT)'''
                 
       
#  """"""""""""""""""""""""""(GenericAPIView,mixins)""""""""""""""""""""""""""    
# class PostList(GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
#     """ getting a list of post and creating new posts"""
#     permission_classes =[IsAuthenticated]
#     serializer_class = PostSerializer
#     queryset = Post.objects.filter(status=True)
    
#     """ retrieving a list of posts"""
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
          
#     """creating a post with provided data"""    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

   
'''class PostDetail(GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    """ getting detail of the post and edit plus removing it"""
    permission_classes =[IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    # lookup_field = "id"
    """retrieving the post data"""
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
     
    # """editing the post data"""
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    """ deleting the post object """
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
         '''
#  """"""""""""""""""""""""""(APIView)""""""""""""""""""""""""""    
# class PostList(ListCreateAPIView):
#     """ getting a list of post and creating new posts"""
#     permission_classes =[IsAuthenticated]
#     serializer_class = PostSerializer
#     queryset = Post.objects.filter(status=True)
    
 
# class PostDetail(RetrieveUpdateDestroyAPIView):
#     """ getting detail of the post and edit plus removing it"""
#     permission_classes =[IsAuthenticated]
#     serializer_class = PostSerializer
#     queryset = Post.objects.filter(status=True)
#     # lookup_field = "id"
#     """retrieving the post data"""
#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)
     
#     # """editing the post data"""
#     def put(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)
    
#     """ deleting the post object """
#     def delete(self,request,*args,**kwargs):
#         return self.destroy(request,*args,**kwargs)



# # Example for ViewSets in CBV
# class PostViewSet(viewsets.viewsets):
#     """ getting a list of post and creating new posts"""
#     permission_classes =[IsAuthenticated]
#     serializer_class = PostSerializer
#     queryset = Post.objects.filter(status=True)   
    
#     def list(self,request):
#         serializer = self.serializer_class(self.queryset, many=True)    
#         return Response(serializer.data)  
    
#     def retrieve(self, request, pk=None):
#         post_object = get_object_or_404(self.queryset, pk=pk)
#         serializer = self.serializer_class(post_object)    
#         return Response(serializer.data) 
    
#     def create (self, request):
#         pass
    
#     def update(self,request,pk=None):
#         pass
    
#     def partial_update(self,request,pk=None):
#         pass
    
#     def destroy(self,request,pk=None):
#         pass

# Example for ModelViewSet in CBV
class PostModelViewSet(viewsets.ModelViewSet):
    """ getting a CRUD for posts"""
    permission_classes =[IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter] 
    filterset_fields = ['status', 'author', 'category']
    ordering_fields = ['published_date']


# Example for ModelViewSet in CBV
class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
      