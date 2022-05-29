from django.dispatch.dispatcher import receiver
from django.shortcuts import render, redirect
from .models import *
from datetime import *
from users.models import *
from pieces.models import *
import itertools


def CreatePiecePermissionView(request, receiver, exh):
    PiecePermissions.objects.create(sender=request.user.id, receiver=receiver, exh_id=exh, date=date.today())
    return redirect("/")



def NotificationsView(request):
    notifications = PiecePermissions.objects.filter(receiver = request.user.id, is_active = 1)

    


    ust_list = []
    
    for i in notifications:
        x = Account.objects.get(id = i.sender)
        thisdict = {
            'notify_id':i.id,
            'sender':i.sender,
            'receiver':i.receiver,
            'date':i.date,
            'exh_id':i.exh_id,
            'sender_name':x.first_name + " " + x.last_name
        }
        ust_list.append(thisdict)
         
        print(ust_list)


    context={
        'notifications':notifications,
        'results':ust_list
    }

    return render(request, 'data/notifications.html',context)


def NotificationDeleteView(request, notify_id):
    PiecePermissions.objects.filter(id = notify_id).update(is_active = 0)
    return redirect('Notifications')


def FollowView(request, followed):
    Follows.objects.create(followed_id=followed, follower_id=request.user.id)
    return redirect('/user/'+str(followed))


def UnfollowView(request, followed):
    Follows.objects.filter(followed_id=followed, follower_id=request.user.id).delete()
    return redirect('/user/'+str(followed))

def LikeView(request, id):
    Likes.objects.create(liker_id=request.user.id, piece_id=id)
    piece = Pieces.objects.get(id=id)
    interest = Interests.objects.get(user_id=request.user.id)
    
    if piece.category == 'resim':
        a = interest.painting + 1                
        Interests.objects.filter(id=request.user.id).update(painting=a)
    elif piece.category == 'heykel':
        a = interest.sculpture + 1                
        Interests.objects.filter(id=request.user.id).update(sculpture=a)
    elif piece.category == 'fotograf':
        a = interest.photograph + 1                
        Interests.objects.filter(id=request.user.id).update(photograph=a)
    elif piece.category == 'cini':
        a = interest.tile + 1                
        Interests.objects.filter(id=request.user.id).update(tile=a)
    elif piece.category == 'deri':
        a = interest.leather + 1                
        Interests.objects.filter(id=request.user.id).update(leather=a)
    elif piece.category == 'seramik':
        a = interest.ceramic + 1                
        Interests.objects.filter(id=request.user.id).update(ceramic=a)
    elif piece.category == 'oymacılık':
        a = interest.carving + 1                
        Interests.objects.filter(id=request.user.id).update(carving=a)
    elif piece.category == 'cam':
        a = interest.glass + 1                
        Interests.objects.filter(id=request.user.id).update(glass=a)
    elif piece.category == 'ebru':
        a = interest.marbling + 1                
        Interests.objects.filter(id=request.user.id).update(marbling=a)

    return redirect('/piece_details/'+str(id))


def UnlikeView(request, id):
    Likes.objects.filter(liker_id=request.user.id, piece_id=id).delete()
    piece = Pieces.objects.get(id=id)
    interest = Interests.objects.get(user_id=request.user.id)
    
    if piece.category == 'resim':
        a = interest.painting - 1                
        Interests.objects.filter(id=request.user.id).update(painting=a)
    elif piece.category == 'heykel':
        a = interest.sculpture - 1                
        Interests.objects.filter(id=request.user.id).update(sculpture=a)
    elif piece.category == 'fotograf':
        a = interest.photograph - 1                
        Interests.objects.filter(id=request.user.id).update(photograph=a)
    elif piece.category == 'cini':
        a = interest.tile - 1                
        Interests.objects.filter(id=request.user.id).update(tile=a)
    elif piece.category == 'deri':
        a = interest.leather - 1                
        Interests.objects.filter(id=request.user.id).update(leather=a)
    elif piece.category == 'seramik':
        a = interest.ceramic - 1                
        Interests.objects.filter(id=request.user.id).update(ceramic=a)
    elif piece.category == 'oymacılık':
        a = interest.carving - 1                
        Interests.objects.filter(id=request.user.id).update(carving=a)
    elif piece.category == 'cam':
        a = interest.glass - 1                
        Interests.objects.filter(id=request.user.id).update(glass=a)
    elif piece.category == 'ebru':
        a = interest.marbling - 1                
        Interests.objects.filter(id=request.user.id).update(marbling=a)
    return redirect('/piece_details/'+str(id))





def addCommentView(request,id):
    if request.method=='POST':
        comment = request.POST['comment']
        if not comment == None:
            Comments.objects.create(commentator_id=request.user.id, piece_id=id, comment=comment)
            return redirect("/piece_details/"+str(id))
        else:
            return redirect("/piece_details/"+str(id))