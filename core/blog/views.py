from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from blog.models import Post
from blog.form import ContactForm, PostForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
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


# class IndexView(TemplateView):
#     '''
#     a class  based templateview to show Index page
#     '''
#     template_name = "index.html"
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["name"] = "ali"
#         context["posts"] = Post.objects.all()
#         return context
   


# class  RedirectToMaktab(RedirectView): 
#     '''
#     a class  based redirectview to show redirect_to_maktabkhooneh page
#     '''
#     url ='https://maktabkhooneh.com'
    
#     def get_redirect_url(self, *args, **kwargs):
#         post = get_object_or_404(Post,pk=kwargs['pk'])
#         print(post)
#         return super().get_redirect_url(*args, **kwargs)


class PostListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    
    '''
    a class  based listview to show post_list page
    '''
    # this two command to way for  get object all 
    permission_required = "blog.view_post"
    
    model = Post
    # queryset = Post.objects.all()
    
    # change name for object_list and choses your opinion name
    context_object_name = 'posts'
    paginate_by = 2
    # if we added ordering must changing  structure
    ordering = '-id'
    
    # disable when ordering use
    # def get_queryset(self):
    #     posts = Post.objects.filter(status=True)
    #     return posts
 
 
class PostDetailView(LoginRequiredMixin, DetailView):
    '''
    a class  based DetailView to show post_detail page
    '''
    model = Post    
    

# class PostCreateView(FormView):
    '''
    a class  based FormView to show post_create page
    '''
    # template_name = 'blog/contact.html'
    # # f    # form_class = ContactForm
    # form_class = PostForm
    # success_url = '/blog/post/'
    
    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)   


class PostCreateView(LoginRequiredMixin, CreateView):
    '''
    a class  based CreateView to show post_form page
    '''
    model = Post 
    # form_class = PostForm
    fields = ['title','content','status','category','published_date']
    success_url = '/blog/post/'
    
    # get user login and filed author object
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    
class PostEditView(LoginRequiredMixin, UpdateView):
    '''
    a class  based UpdateView to show post_form page
    '''  
    model = Post 
    form_class = PostForm
    success_url = '/blog/post/'

class PostDeleteView(LoginRequiredMixin, DeleteView):
    '''
    a class  based DeleteView to show post_form page
    '''  
    model = Post 
    success_url = '/blog/post/'

    