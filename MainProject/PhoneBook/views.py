from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Users, savedContacts
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

#---------------------------------------------------------------------------------------------------------------#

def mainPage(request):
    if request.method == 'GET':
        return HttpResponse(render(request, 'main.html'))
    
    
    

def signUp(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        
        if Users.objects.filter(username=username).exists():
            return render(request, 'signUp', {'error': 'User already exists, please use other name'})
        
        if Users.objects.filter(email=email).exists():
            return render(request, 'signUp', {'error': 'This email has been taken.'})
        
        if Users.objects.filter(phone=phone).exists():
            return render(request, 'signUp', {'error': 'This number is already registered'})
        
        newuser = Users.objects.create_user(username=username, email=email, password=password)
        newuser.phone = phone
        newuser.address = address
        newuser.save()
        return redirect('signIn')

    return HttpResponse(render(request, 'signUp.html'))




def signIn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        myuser = authenticate(request, username=username, password=password)
        if myuser is not None:
            login(request, myuser)
            return redirect('dashBoard')
        
        else:
            return render(request, 'signIn.html', {'error': 'Wrong Credentials.'})
        
    return HttpResponse(render(request, 'signIn.html'))


#Does not work
@login_required(login_url='signIn')
@require_POST
def signOut(request):
    logout(request)
    return redirect('signIn')
    


@login_required(login_url='signIn')
def dashBoard(request):
    owner = request.user
    mycontacts = savedContacts.objects.filter(owner=owner)
    template = loader.get_template('dashBoard.html') 
    context = {
        'mycontacts' : mycontacts,
    }
    return HttpResponse(template.render(context, request))




@login_required(login_url='signIn')
def contactDetails(request, id):
    if request.method == 'GET':
        owner = request.user        
        mycontacts = savedContacts.objects.get(id = id, owner=owner)
        template = loader.get_template('contactDetails.html')
        context = {
            'mycontacts' : mycontacts,
        }
    return HttpResponse(template.render(context, request))




@login_required(login_url='signIn')
def addContact(request):
    if request.method == 'POST':
        owner = request.user
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        
        if not all([username, phone, email, address]):
            return render(request, 'addContact.html')
        
        if savedContacts.objects.filter(username=username).exists():
            return render(request, 'addContact.html', {'error': 'This Contact already exists'})
        
        if savedContacts.objects.filter(phone=phone).exists():
            return render(request, 'addContact.html', {'error': 'This Number is already saved'}) 
        
        newContact = savedContacts.objects.create(owner=owner, username=username, phone=phone, email=email, address=address)
        newContact.save()
        return redirect('dashBoard')
   
    return HttpResponse(render(request, 'addContact.html'))




@login_required(login_url='signIn')
def updateContact(request, id):
    
    mycontacts = savedContacts.objects.get(id=id)
    
    if request.method == 'POST':
        mycontacts.owner = request.user
        mycontacts.username = request.POST.get('username') or mycontacts.username
        mycontacts.phone = request.POST.get('phone') or mycontacts.phone
        mycontacts.email = request.POST.get('email') or mycontacts.email
        mycontacts.address = request.POST.get('address') or mycontacts.address
        
        if not any([mycontacts.username, mycontacts.phone, mycontacts.email, mycontacts.address]):
            return render(request,'updateContact.html', {'error': 'All fields are required'})
        
        mycontacts.save()
        return redirect('contactDetails', id=mycontacts.id)        
    
    return render(request, 'updateContact.html', {'mycontacts': mycontacts})




@login_required(login_url='signIn')
def deleteContact(request, id):
    
    mycontacts = get_object_or_404(savedContacts, id=id, owner = request.user)
    
    if request.method == 'POST':         
        
        mycontacts.delete()
        return redirect('dashBoard')
        
    return HttpResponse(render(request, 'contactDetails.html', {'mycontacts': mycontacts}))




@login_required(login_url='signIn')
def viewProfile(request):
    owner = request.user
    if request.method == 'GET':
        id = request.user.id
        
        Users.objects.filter(id=id)
        
    context = {
        'owner' : owner
    }
    
    return HttpResponse(render(request, 'viewProfile.html', context))


       


@login_required(login_url='signIn')
def updateProfile(request):
    owner = request.user
    myaccount = Users.objects.get(id=owner.id)
    
    if request.method == 'POST':
        myaccount.username = request.POST.get('username') or myaccount.username
        myaccount.phone = request.POST.get('phone') or myaccount.phone
        myaccount.email = request.POST.get('email') or myaccount.email 
        myaccount.address = request.POST.get('address') or myaccount.address
        
        if not any([myaccount.username, myaccount.phone, myaccount.email, myaccount.address]):
            return render(request, 'updateProfile.html', {'error': 'Some fields are required', 'myaccount': myaccount})
        
        myaccount.save()
        return redirect('viewProfile')
    
    context = {
        'myaccount': myaccount
    }
    return render(request, 'updateProfile.html', context)




@login_required(login_url='signIn')
def deleteProfile(request):
    if request.method == 'POST':
        owner = request.user
        logout(request)
        owner.delete()
        return render(request, 'signUp.html', {'message': 'Account successfully deleted'})
    return render(request, 'viewProfile.html')



@login_required(login_url='signIn')
def searchContact(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        if search:
            mycontacts = savedContacts.objects.filter(username__icontains=search, owner=request.user)
        else:
            mycontacts = savedContacts.objects.filter(owner=request.user)

<<<<<<< HEAD
        return render(request, 'dashBoard.html', {'mycontacts': mycontacts})
=======
        return render(request, 'dashBoard.html', {'mycontacts': mycontacts})
>>>>>>> 91a0ae930281f50ab242869514e094f75a0e5a97
