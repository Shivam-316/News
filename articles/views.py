from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,CreateView,DetailView
from django.views.generic.edit import UpdateView,DeleteView
from .models import Article
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied



class ArticleCreateView(LoginRequiredMixin,CreateView):
    model= Article
    template_name= 'article_create.html'
    fields=('title','body')
    login_url= 'login'

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    
class ArticleListView(LoginRequiredMixin,ListView):
    model= Article
    template_name= 'article_list.html'
    login_url= 'login'

class ArticleUpdateView(LoginRequiredMixin,UpdateView): # new
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_update.html'
    login_url= 'login'

    def dispatch(self,request,*args,**kwargs):
        abj=self.get_object()
        if abj.author!=self.request.user:
            raise PermissionDenied
        return super().dispatch(request,*args,**kwargs)
    
    
class ArticleDeleteView(LoginRequiredMixin,DeleteView): # new
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url= 'login'

    def dispatch(self,request,*args,**kwargs):
        abj=self.get_object()
        if abj.author!=self.request.user:
            raise PermissionDenied
        return super().dispatch(request,*args,**kwargs)

class ArticleDetailView(LoginRequiredMixin,DetailView):
    model= Article
    fields='__all__'
    template_name='article_detail.html'
    login_url= 'login'
