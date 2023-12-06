from django.shortcuts import render
from blog.models import Post, Comentario
from django.http import HttpResponseRedirect
from blog.forms import ComentarioForm

# Create your views here.


#Vizualização para a pagina inicial
def blog_index(request):
    posts = Post.objects.all().order_by('-criado_em')
    context = {
        'posts': posts,
    }

    return render(request, 'blog/index.html', context)

# Vizualização para a página de detalhe de um post
def blog_detalhe(request, pk):
    post = Post.objects.get(pk=pk)
    form = ComentarioForm()
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = Comentario(
                autor = form.cleaned_data['autor'],
                corpo = form.cleaned_data['corpo'],
                post = post,
            )
            comentario.save()
            return HttpResponseRedirect(request.path_info)


    comentarios = Comentario.objects.filter(post=post)

    context = {
        'post': post,
        'comentarios': comentarios,
        'form' : ComentarioForm(),

    }


    return render( request, "blog/detalhe.html",context)


#Visualização para as categorias

def blog_categoria(request, categoria):
    posts = Post.objects.filter(
        categorias__nome__contains = categoria
    ).order_by(
        '-criado_em'
    )

    context = {
        'categoria': categoria,
        'posts': posts
    }

    return render(request, 'blog/categoria.html', context)