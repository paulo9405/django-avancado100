from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from clientes.models import Person
from produtos.models import Produto
from vendas.models import Venda
from .forms import PersonForm
from django.views.generic.list import ListView
from django.views.generic.list import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required



@login_required
def persons_list(request):
    persons = Person.objects.all()

    return render(request, 'person.html', {'persons': persons})


@login_required
def persons_new(request):
    if not request.user.has_perm('clientes.change_person'):
        return HttpResponse('Não autorizado')
    elif not request.user.is_superuser:
        return HttpResponse('Não é super usuário')
    form = PersonForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form})


@login_required
def persons_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect('person_list')

    return render(request, 'person_form.html', {'form': form})


@login_required
def persons_delete(request, id):
    person = get_object_or_404(Person, pk=id)

    if request.method == 'POST':
        person.delete()
        return redirect('person_list')

    return render(request, 'person_delete_confirm.html', {'person': person})


#ListViews

class PersonList(LoginRequiredMixin, ListView):
    model = Person

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        primeiro_acesso = self.request.session.get('primeiro_acesso', False)

        if not primeiro_acesso:
            context['message'] = 'Seja bem vindo ao seu primeiro acesso hoje'
            self.request.session['primeiro_acesso'] = True
        else:
            context['message'] = 'Você ja acessou hoje'
        return context

#Cria uma person DetailView que recebe os detalhes do objeto.

class PersonDetail(LoginRequiredMixin, DetailView):
    model = Person

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        return Person.objects.select_related('doc').get(id=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['vendas'] = Venda.objects.filter(
            pessoa_id=self.object.id)
        return context


# Class para criar o objeto, buscando o model e os seus campos 'fields'
class PersonCreate(LoginRequiredMixin, CreateView):
    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo', 'doc']
    success_url = '/clientes/person_list' #essa varivel vai redirecinar para essa url dps q criar o obj


#class para atualizar 'update'
class PersonUpdate(LoginRequiredMixin, UpdateView):
    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo', 'doc']
    success_url = reverse_lazy('person_list_cbv') # em vez de usar a url eu uso o 'reverse_lazy' para que ele mesmo descubra qual é a url de acordo com nome dela


#class para deletar
class PersonDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ('clientes.deletar_clientes')
    model = Person
    #success_url = reverse_lazy('person_list_cbv')

    def get_success_url(self): # esse metodo vai executar no caso da ausencia da varivel sucsses url e vai redirecionar a pessoa para a url setada
        return reverse_lazy('person_list_cbv')


class ProdutoBulk(View):
    def get(self, request):
        produtos = ['Banana', 'Maçã', 'Limão', 'Laranja', 'Pera', 'Melancia']
        list_produtos = []

        for produto in produtos:
            p = Produto(descricao=produto, preco=10)
            list_produtos.append(p)

        Produto.objects.bulk_create(list_produtos)

        return HttpResponse('Funcionou')


def api(request):
    a = {'Nome': 'Paulo', 'Idade': 27, 'Salario': 500}
    mensagem = {'mensagem': 'erro x y z'}
    lista = [1, 2, 3]

    produto = Produto.objects.last()

    b = model_to_dict(produto)

    l = []

    produtos = Produto.objects.all()

    for produto in produtos:
        l.append(model_to_dict(produto))

    return JsonResponse(l, status=200, safe=False)
