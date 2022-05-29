from django.shortcuts import render
from exhibitions.models import *
from pieces.models import *
from users.models import *
#from datetime import *
from datetime import date, timedelta
from extra_data.models import * 
import time
import random


def index(request):
    follows = Follows.objects.filter(follower_id=request.user.id)

    result_list = []
    now = date.today()
    
    for i in follows:
        account = Account.objects.get(id=i.followed_id)
        pieces = Pieces.objects.filter(owner_id=account.id)
        exhibitions = Exhibitions.objects.filter(owner_id=account.id)
        for j in pieces:
            likes = Likes.objects.filter(piece_id=j.id).count()
            thisdict = {
                'id': j.id,
                'name': account.first_name + account.last_name,
                'object_name': j.name,
                'owner_id': j.owner_id,
                'owner_picture': account.picture,
                'picture': j.picture_url,
                'description': j.description,
                'release_date': j.release_date,
                'likes': likes,
                'type': 'piece',
                'is_vip':False
            }
            result_list.append(thisdict)
        for k in exhibitions:
            thisdict = {
                'id': k.id,
                'name': account.first_name + account.last_name,
                'object_name': k.name,
                'owner_picture': account.picture,
                'picture': account.picture,
                'description': k.description,
                'release_date': k.release_date,
                'type': 'exhibition',
                'thumbnail':k.thumbnail,
                'is_vip':False
            }
            result_list.append(thisdict) 
    vips=[]    
    vip_accounts = Account.objects.filter(is_vip = True)
    if len(vip_accounts)>0:
        for v in vip_accounts:
            vips.append(v.id)
        chosen_id = random.choice(vips)
        chosen_artist = Account.objects.get(id = chosen_id)
        chosen_piece = Pieces.objects.filter(owner_id = chosen_id).last()
        likes2 = Likes.objects.filter(piece_id=chosen_piece.id).count()
        print(chosen_piece)
        thisdict = {
                    'id': chosen_piece.id,
                    'name': chosen_artist.first_name + chosen_artist.last_name,
                    'object_name': chosen_piece.name,
                    'owner_picture': chosen_artist.picture,
                    'picture': chosen_piece.picture_url,
                    'description': chosen_piece.description,
                    'release_date': chosen_piece.release_date,
                    'type': 'piece',
                    'owner_id': chosen_piece.owner_id,
                    'likes': likes2,
                    'is_vip':True
                }
        result_list.append(thisdict) 
    pieces_all = Pieces.objects.all()
    tops = []
    for j in pieces_all:
        top_likes = Likes.objects.filter(piece_id=j.id).count()
        thisdict3 = {
            'p_name' : j.name,
            'p_id' : j.id,
            'p_likes' : top_likes,
            'p_url': j.picture_url,
            'p_date' : j.release_date,
            'p_desc' : j.description
        }
        tops.append(thisdict3)
    context = {
        'results': result_list,
        'now': now,
        'tops':tops
    }


    return render(request, 'anasayfa.html', context)
    
    
def SearchView(request):
    
    if request.method=='POST':
        
        searched = request.POST['search_input']
        searched2 = searched.split()
        if len(searched2) >=2:
            results_users = Account.objects.filter(first_name__contains=searched2[0],last_name__contains=searched2[1])
        else:
            results_users = Account.objects.filter(first_name__contains=searched2[0])

        results_pieces = Pieces.objects.filter(name__contains=searched)
        
        results_exhibitions = []
        exhs = Exhibitions.objects.filter(name__contains=searched)
        for exh in exhs:
            user = Account.objects.get(id=exh.owner_id)
            dict2 = {
                'id':exh.id,
                'name': exh.name,
                'description':exh.description,
                'owner_id':exh.owner_id,
                'thumbnail':exh.thumbnail,
                'release_date':exh.release_date,
                'user_picture':user.picture
            }
            results_exhibitions.append(dict2)

        context = {
            'searched':searched,
            'results_users':results_users,
            'results_pieces':results_pieces,
            'results_exhibitions':results_exhibitions
        }
        return render(request, 'search_results.html', context)
    else:

        return render(request, 'search_results.html', {})


def UserView(request, id):
    profil = Account.objects.get(id = id)

    try:
        Follows.objects.get(followed_id=id, follower_id=request.user.id)
        followed = 1
    except:
        followed = 0
        
    pieces = Pieces.objects.filter(owner_id = id)
    followers = Follows.objects.filter(followed_id=id).count()
    exh = Exhibitions.objects.filter(owner_id = id)
    now = date.today()
    session_user_id = request.user.id
    context={
        'profil':profil,
        'pieces':pieces,
        'exh':exh,
        'followed': followed,
        'now':now,
        'session_user_id':session_user_id,
        'followers':followers
    }

    return render(request, 'users/profil.html',context )



def addNewPieceToExhSearchUserView(request,exh):
    
    if request.method=='POST':
        owner = request.user
        searched = request.POST['search_input']
        searched2 = searched.split()
        if len(searched2) >=2:
            results_users = Account.objects.filter(first_name__contains=searched2[0],last_name__contains=searched2[1])
        else:
            results_users = Account.objects.filter(first_name__contains=searched2[0])

        results_pieces = Pieces.objects.filter(name__contains=searched)
        context = {
            'results_users':results_users,
            'owner':owner,
            'exh':exh
        }
        return render(request, 'exhibitions/add_new_piece_to_exh_search_user.html', context)
    else:

        return render(request, 'search_results.html', {})


def ExploreView(request):
    now = date.today()
    ##en çok beğenilen eserleri slider'da gösterme
    pieces_all = Pieces.objects.all()
    tops = []
    for j in pieces_all:
        top_likes = Likes.objects.filter(piece_id=j.id).count()
        thisdict3 = {
            'p_name' : j.name,
            'p_id' : j.id,
            'p_likes' : top_likes,
            'p_url': j.picture_url,
            'p_date' : j.release_date,
            'p_desc' : j.description
        }
        tops.append(thisdict3)
    
    ##kullanıcının en çok beğendiği kategoriyi bulma işlemleri
    interests = Interests.objects.get(user_id = request.user.id)
    thisdict = {
        'resim': interests.painting,
        'heykel': interests.sculpture,
        'fotograf': interests.photograph,
        'cini': interests.tile,
        'deri': interests.leather,
        'seramik': interests.ceramic,
        'oymacılık': interests.carving,
        'cam': interests.glass,
        'ebru': interests.marbling,
    }
    maximum = max(thisdict, key=thisdict.get)
    ## Kullanıcının en beğendiği tür için, o türden son 1 günde paylaşılmış ve en çok beğeni almış olanlar keşfette listelenir.
    ## mevcut türdeki son 1 günde en çok beğeni almış eserleri bulma
    pieces_list = []
    pieces = Pieces.objects.filter(category=maximum)
    exhibitions_list = []
    for i in pieces:
        if not i.exhibition_id == None:
            exh = Exhibitions.objects.get(id=i.exhibition_id) 
            thisdict2 = {
                'e_name' : exh.name,
                'e_thumbnail': exh.thumbnail            
            }
            exhibitions_list.append(thisdict2)

        p = Likes.objects.filter(piece_id = i.id).count()

        thisdict = {
            'p_name' : i.name,
            'p_id' : i.id,
            'p_likes' : p,
            'p_url': i.picture_url,
            'p_date' : i.release_date,
            'p_desc' : i.description
        }

        pieces_list.append(thisdict)
    

    # hype = (çıkış yaptıktan sonra geçen gün sayısı / beğeni sayısı)
    # hype büyüklüğüne göre sıralanacak

    p_dict_list=[]
    now = date.today()
    for i in range(3):
        day = date.today() - timedelta(days=i)
        pieces = Pieces.objects.filter(release_date = day)
        for piece in pieces:
            likes = Likes.objects.filter(piece_id = piece.id).count()
            user = Account.objects.get(id=piece.owner_id)
            if i > 0:
                hype = likes/i
            elif i ==0:
                hype = likes
            dict = {
                'id':piece.id,
                'name': piece.name,
                'description':piece.description,
                'exhibition_name' :piece.exhibition_id,
                'owner_id':piece.owner_id,
                'category':piece.category,
                'picture_url':piece.picture_url,
                'price':piece.price,
                'owner_name':user.first_name + user.last_name,
                'release_date':piece.release_date,
                'likes': likes,
                'hype':hype
            }
            p_dict_list.append(dict)
            #print(piece.name + " hype: "+ str(hype))
    e_dict_list=[]
    for i in range(3):
        day = date.today() - timedelta(days=i)
        exhs = Exhibitions.objects.filter(release_date = day)
        for exh in exhs:
            user = Account.objects.get(id=exh.owner_id)
            dict2 = {
                'id':exh.id,
                'name': exh.name,
                'description':exh.description,
                'owner_id':exh.owner_id,
                'thumbnail':exh.thumbnail,
                'release_date':exh.release_date,
                'user_picture':user.picture
            }
            e_dict_list.append(dict2)
    print(e_dict_list)
    context = {
        'pieces_list': pieces_list,
        'exhibitions_list': exhibitions_list,
        'tops': tops,
        'p_dict_list':p_dict_list,
        'e_dict_list':e_dict_list
    }
    return render(request, 'explore.html', context)