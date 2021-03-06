from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Pessoa
from .forms import PersonFrom

# Create your views here.
@login_required()
def cliente(request):
    return render(request,'index.html')

@login_required()
def listar_pessoas(request):
    first_name = request.POST.get('first_name', None)
    last_name = request.POST.get('last_name', None)
    if first_name or last_name:
        persons = Pessoa.objects.filter(first_name__icontains=first_name) or Pessoa.objects.filter(last_name__icontains=last_name)
    else:
        persons = Pessoa.objects.all() # lista todos
    return render(request,'lista_pessoas.html',{'persons':persons})

@login_required()
def new_person(request):
    form = PersonFrom(request.POST or request.FILES or None) # alem de enviar o form,
        # se o estiver preenchido, ao atualizar vai permanecer
    if form.is_valid():
        form.save()
        return  redirect('url_personlist')
    return render(request, 'form_person.html', {'form':form})

@login_required()
def person_update(request, id):
    person = Pessoa.objects.get(pk=id)
    form = PersonFrom(request.POST or None, instance=person) # recebe o form

    if form.is_valid():
        form.save()
        return redirect('url_personlist')
    return render(request, 'form_person.html', {'form':form})

@login_required()
def person_delete(request, id):
    person = Pessoa.objects.get(pk=id)
    Pessoa.delete(person)
    return redirect('url_personlist')

def seach_client(request, id):
    person = Pessoa.objects.get(pk=id)
    return render(request, 'form_person.html',{'seachperson': person})