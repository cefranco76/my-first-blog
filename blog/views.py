from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
#from .models import TabUsuario
#from .models import TabImagens


# Create your views here.

def usuarios_list(request):
    usuarios = TabUsuario.objects.all().order_by('nome_completo')
    return render(request, 'blog/usuarios.html', {'usuarios': usuarios})
	
def post_list(request): 
    posts = Post.objects.order_by('published_date') 
    return render(request, 'blog/post_list.html', {'posts':posts})	
	
def post_detail(request,pk): 
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})



     
     

