from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from users.models import Post
from django.contrib import messages











def home_page(request):
    form = Post.objects.all()
    dict = {
        'form':form
    }
    return render(request,'home.html',dict)


#create post

def createpage(request):
 
    return render(request,'create_post.html')

def create_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        date = request.POST['date']
        image = request.FILES.get('image')
        user = Post.objects.create(title=title,content=content,pub_date=date,profile_pic=image)
        user.save()
        messages.success(request,'Successfully Created a Post')
        return redirect('home')
    



def sign_up_page(request):
    if request.method == 'POST':
        username = request.POST.get('username') 
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('cpassword')
        if password1 != password2:
            return HttpResponse('Password and Confirm Password Does not Match')
        else:
            my_user = User.objects.create_user(username=username,email=email,password=password1)
            my_user.save()
            return redirect('login')        
    return render(request,'signup.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password')
        user = authenticate(request,username=username,password=password1)
        if user is not None:
            login(request,user)
            messages.success(request,'You have Successfully LoggedIn!')
            return redirect('home')
        else:
            return HttpResponse('Username and Password does not match')
    return render(request,'login.html')

@login_required
def Logout_page(request):
    logout(request)
    messages.warning(request,'You have Successfully LoggedOut!')
    return redirect('home')

def example(request):
    return HttpResponse('hello')