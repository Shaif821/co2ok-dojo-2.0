from django.urls import path
from django.conf.urls import url
from accounts import views

app_name = "accounts"
urlpatterns = [
    # path('profile/', view=views.profile, name="profile"),
    url(r"^profile/$", views.profile, name="profile"),
    path('updateAccount/', views.updateAccount, name='updateAccount'),
    path('updatePassword/', views.updatePassword, name='updatePassword'), 
    path('deleteAccount/', views.deleteAccount, name='deleteAccount'),
    path('sendMail/', views.sendMail, name='sendMail'),
]
