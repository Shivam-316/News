from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy

class SignUp(CreateView):
    form_class= CustomUserCreationForm
    success_url= reverse_lazy('home')
    template_name= 'signup.html'
    
