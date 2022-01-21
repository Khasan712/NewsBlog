from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# DJANGO PACKET FOR AUTHENTICATING
from .forms import UserProfileForm, CreatUserPostForm, UserEditProfileForm
from .models import CustomUser
from mainapp.models import NewsPost
from commentsUser.models import CommentsPost
# Create your views here.


def user_register(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            form = UserProfileForm(request.POST)
            if form.is_valid():
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was creatd for ' + user)
                form.user = user
                user.save()
                return redirect('user_login')
            else:
                messages.error(request, "Error")
        else:
            form = UserProfileForm()
    
    context = {
        'form':form,
    }
    return render(request, 'accounts/user_register.html', context)



def user_login(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            elif user is None:
                messages.warning(request, 'Not found that acoount')
            else:
                messages.error(request, 'Username or password did not match')
    return render(request, 'accounts/user_login.html')



def user_logout(request):
    logout(request)
    return redirect('index')



def user_profile(request, pk):
    userProfile = CustomUser.objects.get(id=pk)
    moreViews = NewsPost.objects.filter(author_id=pk)[::-1]
    userComment = CommentsPost.objects.filter(post_id=pk)
    post = NewsPost.objects.all()
    # qty_moreViews = NewsPost.objects.filter(author_id=pk).count()

    post_image = NewsPost.objects.all()
    user = request.user
    form = CreatUserPostForm()
    if request.method == 'POST':
        form = CreatUserPostForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            author = CustomUser.objects.filter(username=user.username).first()
            # tags = NewsPost.objects.get(tags=post.tags)
            obj.author = author
            # obj.tags = tags
            obj.save()
            form.save_m2m()
	        # form.save_m2m()
            return redirect('user_profile', user.id)

    context = {
        'userProfile':userProfile,
        'form':form,
        'moreViews':moreViews,
        'userComment':userComment,
        'user':user,
        # 'qty_moreViews':qty_moreViews,
    }
    return render(request, 'accounts/user_profile.html', context)

def delete_user_post(request, pk):
    user = request.user
    userPost = NewsPost.objects.get(id=pk)
    userPost.delete()
    return redirect('user_profile', user.id)
    





def edit_user_profile(request, pk):
    userProfile = CustomUser.objects.get(id=pk)
    form = UserEditProfileForm(request.POST or None, request.FILES or None, instance=userProfile)
    if request.method == 'POST':
        form = UserEditProfileForm(request.POST, request.FILES, instance=userProfile)
        if form.is_valid():
            form.save()
            return redirect('user_profile', userProfile.id)
    
    context = {
        'form':form,
        'userProfile':userProfile
    }

    return render(request, 'accounts/edit_user_profile.html', context)



def update_user_post(request, pk):
    userPost = NewsPost.objects.get(id=pk)
    form = CreatUserPostForm()
    user = request.user
    if request.method == 'POST':
        form = CreatUserPostForm(request.POST, request.FILES, instance=userPost)
        if form.is_valid():
            obj = form.save(commit=False)
            author = CustomUser.objects.filter(username=user.username).first()
            obj.author = author
            obj.save()
            return redirect('user_profile', user.id)
    else:
        print('Xato!!!')

    context = {
        'form':form,
    }

    return render(request, 'accounts/update_user_post.html', context)


