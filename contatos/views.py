from .models import Contato
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    contatos = Contato.objects.all()
    paginator = Paginator(contatos, 5)

    page_number = request.GET.get('page')
    contatos = paginator.get_page(page_number)

    return render(request, 'contatos/index.html',{
        'contatos': contatos
    })

def visualizar_contato(request, contato_id):
    contato = get_object_or_404(Contato, id=contato_id)

    return render(request, 'contatos/visualizar_contato.html',{
        'contato': contato
    })


