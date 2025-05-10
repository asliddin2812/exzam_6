from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect

from .forms import NatoMemberForm,UserUpdateForm
from .models import NatoMember


def home(request):
    return render(request,'base.html')
def index(request):
    obj_list = NatoMember.objects.all()
    return render(request, 'nato/view.html', {'obj_list': obj_list})

def nato_list(request):
    member_list = NatoMember.objects.all()
    return render(request, 'nato/list.html', {'member_list': member_list})

def member_create(request):
    if request.method == 'POST':
        form = NatoMemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base')
    else:
        form = NatoMemberForm()
    return render(request, 'nato/add.html', {'form': form})

def member_edit(request, country_name):
    member = NatoMember.objects.get(country_name=country_name)
    if request.method == 'POST':
        form = NatoMemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = NatoMemberForm(instance=member)
    return render(request, 'nato/edit.html', {'form': form})

def member_delete(request, country_name):
    member = NatoMember.objects.get(country_name=country_name)
    if request.method == 'POST':
        member.delete()
        return redirect('base')
    return render(request, 'nato/delete.html', {'member': member})


def search(request):
    query = request.GET.get('q')

    if query:
        results  = NatoMember.objects.filter(Q(country_name__icontains=query))

    else:
        results = NatoMember.objects.all()
    return render(request, 'nato/list.html', {'results': results, 'query': query})

@login_required
def profile_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, "Your profile has been updated successfully!")
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
    return render(request, 'account/profile_update.html', {'u_form': u_form})
