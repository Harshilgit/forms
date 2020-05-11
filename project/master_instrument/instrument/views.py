from django.shortcuts import render, redirect
from .forms import masterform
from .models import master

# Create your views here.


def master_list(request):
    context = {'master_list': master.objects.all()}
    return render(request, "instrument/master_list.html", context)


def master_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = masterform()
        else:
            Master = master.objects.get(pk=id)
            form = masterform(instance=Master)
        return render(request, "instrument/master_form.html", {'form': form})
    else:
        if id == 0:
            form = masterform(request.POST)
        else:
            Master = master.objects.get(pk=id)
            form = masterform(request.POST,instance= Master)
        if form.is_valid():
            form.save()
        return redirect('/master/list')


def master_delete(request,id):
    Master = master.objects.get(pk=id)
    Master.delete()
    return redirect('/master/list')