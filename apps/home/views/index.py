from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from users.models import User

# def index(request):
#     posts = Post.objects.select_related('author').all().order_by('-create_at')

#     paginator = Paginator(posts, 8)
#     page_number = request.GET.get('page')
#     page_posts = paginator.get_page(page_number)

#     context = {
#         'page_posts': page_posts
#     }

#     return render(request, "home/index.html", context)

@login_required
def index(request):
    users = User.objects.all()

    # list_salas = SalaVotacao.objects.select_related('admin').prefetch_related('usuarios').filter(usuarios=request.user).order_by("-data_registrado")
    # list_votacoes = Votacao.objects.select_related('sala').filter(sala__in=list_salas)

    # list_salas_vinculadas = []

    # if not list_salas:
    #     messages.info(request,"Não existem salas registradas!")

    # list_salas_vinculadas = Votacao.get_qtd_votacoes(request, list_salas, list_votacoes)

    context = {
        # "salas": list_salas_vinculadas,
        "users", users
    }

    return render(request, "home/index.html")