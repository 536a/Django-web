from django.shortcuts import render
from users.models import Account
from django.http import request
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .forms import *
from .models import *
from pieces.models import *
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.shortcuts import HttpResponseRedirect
# Create your views here.

class addNewExhibitionView(SuccessMessageMixin, CreateView):
    model = Exhibitions
    template_name = 'exhibitions/add_new_exhibition.html'
    form_class = AddNewExhibitionForm
    success_url = '/profil'
    success_message = 'Sergi Başarıyla Eklendi'
    def form_valid(self, form):
        user = Account.objects.get(id=self.request.user.id)
        if user.is_vip == 0:
            if Exhibitions.objects.filter(owner_id=self.request.user.id).count()>=1:
                return redirect('/profil')
        exh = form.save(commit=False)
        exh.owner_id = self.request.user.id
        exh.save()
        return super(addNewExhibitionView, self).form_valid(form)

def ExhDetail(request, id):
    exh=Exhibitions.objects.get(id = id)
    owner = Account.objects.get(id = exh.owner_id)
    pieces = Pieces.objects.filter(exhibition_id = id)
    session_user_id = request.user.id
 
    context = {
        'exh' : exh,
        'owner' : owner,
        'pieces' : pieces,
        'session_user_id' : session_user_id
    }
    return render(request, 'exhibitions/exhibition_details.html',context)


def ExhUpdate(request, id):
    exh=Exhibitions.objects.get(id = id)   
    form = AddNewExhibitionForm(request.POST or None, instance = exh)

    context = {
        'exh' : exh,
        'form' : form
    }

    if form.is_valid():
        form.save()
        return redirect('/exhibition_details/' + str(id) + "/")
        
    return render(request, 'exhibitions/exhibition_update.html',context)



