
from django.urls import path
from blog.api.v1 import views


app_name = 'api-v1'
urlpatterns = [
    # path('post/',views.post_list,name="post_list"),
    # path('post/<int:id>/',views.post_detail,name="post_detail"),
    # path('post/',views.PostList.as_view(),name="post_list"),
    # path('post/<int:pk>/',views.PostDetail.as_view(),name="post_detail"),
    path('post/',views.PostViewSet.as_view({'get':'list'}),name='post_list'),   
    path('post/<int:pk>/',views.PostViewSet.as_view({'get':'list'}),name='post_detail'),
]
