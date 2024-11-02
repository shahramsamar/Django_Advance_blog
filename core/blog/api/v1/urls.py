
from django.urls import path
from blog.api.v1 import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('post', views.PostModelViewSet,basename='post')
router.register('category', views.CategoryModelViewSet,basename='category')

urlpatterns = router.urls

app_name = 'api-v1'

# urlpatterns = [
#     # path('post/',views.post_list,name="post_list"),
#     # path('post/<int:id>/',views.post_detail,name="post_detail"),
#     # path('post/',views.PostList.as_view(),name="post_list"),
#     # path('post/<int:pk>/',views.PostDetail.as_view(),name="post_detail"),
#     path('post/',views.PostViewSet.as_view({'get':'list','put':'create'}),name='post_list'),   
#     path('post/<int:pk>/',views.PostViewSet.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}),name='post_detail'),
# ]
