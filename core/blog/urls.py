"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
# from blog.views import indexView
from blog import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

app_name = 'blog'
urlpatterns = [
    path('cbv-index',views.IndexView.as_view(), name='cbv-index'),
    path('go-to-maktabkhooneh/<int:pk>/',views.RedirectToMaktab.as_view(), name='redirect_to_maktabkhooneh'),
    # path('post/',views.Postlist.as_view(),name='post_list'),
    
    # fbv-index 
    # path('fbv-index', indexView, name="fbv-test"),
    
    # cbv-index two way 
    # path('cbv-index',views.IndexView.as_view(), name='cbv-index'),
    # path('cbv-index',TemplateView.as_view(template_name="index.html",extra_context={'name':'ali'})),
   
    # path('go-to-maktabkhooneh',
    #      RedirectView.as_view(url='https://maktabkhooneh.com/'),
    #      name='redirect_to_maktabkhoneh'),
  
    # path('go-to-index',
    #      RedirectView.as_view(pattern_name = 'blog:cbv-index'),
    #      name='redirect_to_index'),
]

