from django.shortcuts import render, redirect
from .models import Elemen1, Lokasi 

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def lokasi(request):
    if request.method == 'POST':
        listloc = request.POST.get('list_lokasi')
        if listloc:
            Lokasi.objects.create(list_lokasi=listloc)
            return redirect('lokasi')
    data = Lokasi.objects.all()
    return render(request, 'lokasi.html', {'data': data})

def delete_lokasi(request, lid):
    Lokasi.objects.filter(lid=lid).delete()
    return redirect('lokasi')

def e1(request):
    data = Elemen1.objects.all()
    return render(request, 'e1.html', {'data': data})