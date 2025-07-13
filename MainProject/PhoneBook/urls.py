from django.urls import path
from . import views

urlpatterns = [    
    #-----------------------------------------------------------------------------------------#
    
    path('', views.mainPage, name="mainPage"),    
    path('signUp', views.signUp, name ="signUp"),
    path('signIn', views.signIn, name = "signIn"),
    path('signOut', views.signOut, name = "signOut"),
    path('dashBoard', views.dashBoard, name = "dashBoard"),
    path('contactDetails/<int:id>', views.contactDetails, name = "contactDetails"),
    path('addContact', views.addContact, name = "addContact"),
    path('updateContact/<int:id>/', views.updateContact, name = "updateContact"),
    path('deleteContact/<int:id>/', views.deleteContact, name = "deleteContact"),
    path('myProfile', views.viewProfile, name = "viewProfile"),
    path('updateProfile', views.updateProfile, name = "updateProfile"),
    path('deleteAccount', views.deleteProfile, name = "deleteProfile"),
    path('searchContact', views.searchContact, name = "searchContact")
<<<<<<< HEAD
    
=======
>>>>>>> 91a0ae930281f50ab242869514e094f75a0e5a97
]
# This code defines the URL patterns for the PhoneBook application in a Django project.
