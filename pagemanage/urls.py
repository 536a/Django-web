from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from exhibitions.views import *
from pieces.views import *
from users.views import *
from extra_data.views import *

urlpatterns = [
    path('', index,name='index'),
    path('register/', UserRegisterView.as_view(), name='Register'), 
    path('login/', UserLoginView.as_view(),name='Login'), 
    path('logout/', UserLogoutView.as_view() ,name='Logout'),
    path('profil/',ProfilView, name='Profil'),
    path('search_results/',SearchView, name='Search-Results'),
    path('add_new_piece/',addNewPieceView.as_view(), name='Add_New_Piece'),
    path('exhibition_details/<int:id>/',ExhDetail, name='Exhibition_Details'),
    path('add_new_piece_to_exh/<int:id>',addNewPieceToExhView, name='Add_New_Piece_To_Exh'),
    path('add_new_piece_to_others_exh/<int:id>/<int:notify_id>',addNewPieceToOthersExhView, name='Add_New_Piece_To_Others_Exh'),
    path('exhibition_update/<int:id>/',ExhUpdate, name='Exhibition_Update'),
    path('add_new_exhibition/',addNewExhibitionView.as_view(), name='Add_New_Exhibition'),
    path('piece_details/<int:id>/',PieceDetail, name='Piece_Details'),
    path('user/<int:id>',UserView, name='User'),
    path('follow/<int:followed>/',FollowView, name='Follow'),
    path('unfollow/<int:followed>/',UnfollowView, name='Unfollow'),
    path('like/<int:id>',LikeView, name='Like'),
    path('unlike/<int:id>',UnlikeView, name='Unlike'),
    path('explore/',ExploreView, name='Explore'),
    path('update_user_profile',UpdateProfilView,name='Update_Profile'),
    path('add_new_piece_to_exh_search_user/<int:exh>',addNewPieceToExhSearchUserView, name='Add_New_Piece_To_Exh_Search_User'),
    path('piece_to_exh/<int:receiver>/<int:exh>',CreatePiecePermissionView, name='Piece_to_exh'),
    path('Notifications/',NotificationsView,name='Notifications'),
    path('notification_delete/<int:notify_id>',NotificationDeleteView,name='Notification_Delete'),
    path('updateToVip',UpdateAccountToVipView,name='Update_To_Vip'),
    path('add_comment/<int:id>/',addCommentView,name='Add_Comment')
]
