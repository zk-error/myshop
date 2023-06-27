from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserCreationForm,editarperrfilform

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shop:product_list')
    else:
        form = UserCreationForm()
    return render(request,'registration/registro.html',{'form':form})

@login_required
def editarperfil(request):
    user = request.user
    if request.method == 'POST':
        form = editarperrfilform(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('shop:product_list')
    else:
        form = editarperrfilform(instance=user)
    return render(request, 'registration/editar_perfil.html', {'form': form})
