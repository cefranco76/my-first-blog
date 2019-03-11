from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

#from .models import TabUsuario
#from .models import TabImagens


# Create your views here.

def usuarios_list(request):
    usuarios = TabUsuario.objects.all().order_by('nome_completo')
    return render(request, 'blog/usuarios.html', {'usuarios': usuarios})
     
def post_list(request): 
    posts = Post.objects.order_by('published_date') 
    return render(request, 'blog/post_list.html', {'posts':posts})     
     
def post_draft_list(request): 
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date') 
    return render(request, 'blog/post_draft_list.html', {'posts':posts})     
 
def post_detail(request,pk): 
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})     

#def post_edit(request,pk): 
#    post = Post.objects.get(pk=pk)
#    return render(request, 'blog/post_edit.html', {'post':post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_list')

@login_required
def post_remove(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.delete()
    return redirect('post_list')
	


	
     

