from django.shortcuts import render, redirect
from .forms import inserviceform
from .models import inservice


# Create your views here.


def inservice_list(request):
    context = {'inservice_list':inservice.objects.all()}
    return render(request, "insform/inservice_list.html", context)


def inservice_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = inserviceform()
        else:
            Inservice = inservice.objects.get(pk=id)
            form = inserviceform(instance=Inservice)
        return render(request, "insform/inservice_form.html", {'form': form})
    else:
        if id == 0:
            form = inserviceform(request.POST)
        else:
            Inservice = inservice.objects.get(pk=id)
            form = inserviceform(request.POST,instance= Inservice)
        if form.is_valid():
            form.save()
        return redirect('/inservice/list')


def inservice_delete(request,id):
    Inservice = inservice.objects.get(pk=id)
    Inservice.delete()
    return redirect('/inservice/list')





# Create your views here.


# Create your views here.
