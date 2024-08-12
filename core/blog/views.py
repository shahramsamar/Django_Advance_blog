from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import ListView
from blog.models import Post

'''
fbv for templateview
'''
# def indexView(request):
#     '''
#     a function based view to show index page
#     '''
#     name = "ali"
#     context = {"name":name}
#     return render(request, 'index.html',context)

'''
fbv for redirect
'''
# from django.shortcuts  import redirect
# def RedirectToMaktab(request):
#     return redirect("https://maktabkhooneh.com")


class IndexView(TemplateView):
    '''
    a class  based templateview to show Index page
    '''
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "ali"
        context["posts"] = Post.objects.all()
        return context
   


class  RedirectToMaktab(RedirectView): 
    '''
    a class  based redirectview to show redirect_to_maktabkhooneh page
    '''
    url ='https://maktabkhooneh.com'
    
    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post,pk=kwargs['pk'])
        print(post)
        return super().get_redirect_url(*args, **kwargs)


class Postlist(ListView):
    
    '''
    a class  based listview to show post_list page
    '''
    # this two command to way for  get object all 
    # model = Post
    # queryset = Post.objects.all()
    
    # change name for object_list and choses your opinion name
    context_object_name = 'posts'
    paginate_by = 2
    
    
    def get_queryset(self):
        posts = Post.objects.filter(status=True)
        return posts
    
        
    url = "https://maktabkhooneh.com" 