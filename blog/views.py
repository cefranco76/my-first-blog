from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .models import TabUsuario
import pyodbc

# Create your views here.



def post_list(request):

    usuarios = TabUsuario.objects.all().order_by('nome_completo')
    return render(request, 'blog/post_list.html', {'usuarios': usuarios})



     
     

