from pieces.models import Pieces
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import *
from extra_data.models import *
from .models import Account
from exhibitions.views import *
from django.views.generic.list import ListView
from datetime import datetime
from extra_data.models import *





class UserRegisterView(SuccessMessageMixin,CreateView):
    template_name = 'users/register.html'
    form_class = AccountRegisterForm
    success_url = '/'
    success_message = "Hesabınız Oluşturuldu!"

    def form_valid(self, form):
        print("selam")
        user = form.save(commit=False)
        user.save()
        Interests.objects.create(user_id=user.id)
        return redirect(self.success_url)

class UserLoginView(LoginView):
    template_name = "users/login.html"

class UserLogoutView(LogoutView):
    template_name = "users/login.html"


def ProfilView(request):
    profil = Account.objects.get(id= request.user.id)
    pieces = Pieces.objects.filter(owner_id = request.user.id)
    followers = Follows.objects.filter(followed_id=request.user.id).count()
    exh = Exhibitions.objects.filter(owner_id = request.user.id)
    session_user_id = request.user.id
    context = {
        'profil': profil,
        'pieces': pieces,
        'exh': exh,
        'followers': followers,
        'session_user_id': session_user_id
    }
    return render(request, 'users/profil.html',context)


def UpdateProfilView(request):
    profil = Account.objects.get(id= request.user.id)
    form = AccountUpdateForm(request.POST,request.FILES,instance=profil)
    if request.method == 'POST':

        if form.is_valid():
            form.save()
            return redirect('Profil')

    context = {
        'form':form,
        'profil':profil
    }
    return render(request,'users/update_account.html',context)




def UpdateAccountToVipView(request):
    Account.objects.filter(id = request.user.id).update(is_vip = 1)

    return redirect('Profil')