from exhibitions.models import Exhibitions
from users.models import Account
from django.http import request
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .forms import *
from .models import *
from extra_data.models import *
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView
import time
from datetime import *





class addNewPieceView(SuccessMessageMixin,CreateView):
    model = Pieces
    template_name = 'pieces/add_new_piece.html'
    form_class = AddNewPieceForm
    success_url = '/profil'
    success_message = 'Eser Başarıyla Eklendi'
    def form_valid(self, form):
        user = Account.objects.get(id=self.request.user.id)
        if user.is_vip == 0:
            if Pieces.objects.filter(owner_id=self.request.user.id).count()>=10:
                return redirect('/profil')
        piece = form.save(commit=False)
        piece.owner_id = self.request.user.id
        piece.release_date = date.today()
        piece.save()
        return super(addNewPieceView, self).form_valid(form)


def PieceDetail(request, id):
    piece=Pieces.objects.get(id = id)
    owner = Account.objects.get(id = piece.owner_id)
    comments = Comments.objects.filter(piece_id= id)
    comment = []
    for i in comments:
        commentator = Account.objects.get(id=i.commentator_id)
        thisdict = {
            'id': i.id,
            'commentator_id': i.commentator_id,
            'piece_id': i.piece_id,
            'comment': i.comment,
            'date': i.date,
            'commentator': commentator.first_name + " " + commentator.last_name
        }
        comment.append(thisdict)

    try:
        Likes.objects.get(liker_id=request.user.id, piece_id=id)
        liked = 1
    except:
        liked = 0
    
    print(liked)
    context = {
        'piece' : piece,
        'owner' : owner,
        'liked' : liked,
        'comments': comment
    }
    return render(request, 'pieces/piece_details.html',context)


def addNewPieceToExhView(request, id):
    form = AddNewPieceForm(request.POST,request.FILES)
    if request.method == 'POST':
        

        if form.is_valid():
            piece = form.save(commit=False)
            piece.owner_id = request.user.id
            piece.exhibition_id = id
            exh = Exhibitions.objects.get(id = id)
            piece.release_date = exh.release_date
            form.save()
            return redirect('Profil')
    
    context={
        'form':form
    }

    return render(request, 'pieces/add_new_piece.html',context)

def addNewPieceToOthersExhView(request, id, notify_id):
    form = AddNewPieceForm(request.POST,request.FILES)
    if request.method == 'POST':
        

        if form.is_valid():
            piece = form.save(commit=False)
            piece.owner_id = request.user.id
            piece.exhibition_id = id
            exh = Exhibitions.objects.get(id = id)
            piece.release_date = exh.release_date
            form.save()

            PiecePermissions.objects.filter(id = notify_id).update(is_active = 0)
            return redirect('Profil')
    
    context={
        'form':form
    }

    return render(request, 'pieces/add_new_piece.html',context)

