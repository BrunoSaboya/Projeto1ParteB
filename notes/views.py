from django.shortcuts import render, redirect
from django import forms
from .models import Note
from django.http import HttpResponse

class criaNota(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'

def index(request):
    notes = Note.objects.all()
    return render(request, 'notes/notes.html', {'notes': notes})


def uplaoadNota(request):
    upload = criaNota()

    if request.method() == 'POST':
        upload = criaNota(request.POST, request.FILES)

        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse(""" deu erro, reinicia com <a href = "{{ url : 'index'}}">aqui</a>""")

def atualizaNota(request, notaId):
    notaId = int(notaId)
    try:
        selecionaNota = Note.objects.get(id = notaId)
    except Note.DoesNotExist:
        return redirect('index')
    formaNota = criaNota(request.POST or None, instance = selecionaNota)

    if formaNota.is_valid():
        formaNota.save()
        return redirect('index')
    return render (request, 'notes/index.html', {'upload_form': formaNota})

def deletaNota(request, notaId):
    notaId = int(notaId)
    try:
        selecionaNota = Note.objects.get(id = notaId)
    except Note.DoesNotExist:
        return redirect('index')
    selecionaNota.delete()
    return redirect('index')