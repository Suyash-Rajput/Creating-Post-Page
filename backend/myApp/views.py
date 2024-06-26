from rest_framework import generics, permissions
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly
from django.shortcuts import render, redirect
from .templates import *
from .form import * 
from django.contrib.auth import logout        
        
def logout_view(request):
    logout(request)
    return redirect('/')


def index(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'home.html', context)


def login_view(request):
    return render(request, 'login.html')


def post_detail(request, slug):
    context = {}
    try:
        post_obj = Post.objects.get(slug=slug)
        context['post_obj'] = post_obj
        comments_objs = Comment.objects.filter(post=post_obj)
        if comments_objs.count() == 1:
            comments_objs = [comments_objs.first()]
        context['comments_objs'] = comments_objs
        print(comments_objs)
    except Exception as e:
        print(e)
    return render(request, 'post_detail.html', context)


def see_post(request):
    context = {}

    try:
        post_objs = Post.objects.filter(author=request.user)
        context['post_objs'] = post_objs
    except Exception as e:
        print(e)

    print(context)
    return render(request, 'see_post.html', context)


def add_post(request):
    context = {'form': postForm}
    try:
        if request.method == 'POST':
            form = postForm(request.POST)
            print(request.FILES)
            image = request.FILES.get('image', '')
            title = request.POST.get('title')
            user = request.user

            if form.is_valid():
                print('Valid')
                content = form.cleaned_data['content']

            post_obj = Post.objects.create(
                author=user, title=title,
                content=content, image=image
            )
            print(post_obj)
            return redirect('/add-post/')
    except Exception as e:
        print(e)

    return render(request, 'add_post.html', context)


def post_update(request, slug):
    context = {}
    try:

        post_obj = Post.objects.get(slug=slug)

        if post_obj.author != request.user:
            return redirect('/')

        initial_dict = {'content': post_obj.content}
        form = postForm(initial=initial_dict)
        if request.method == 'POST':
            form = postForm(request.POST)
            print(request.FILES)
            image = request.FILES['image']
            title = request.POST.get('title')
            user = request.user

            if form.is_valid():
                content = form.cleaned_data['content']

            post_obj = Post.objects.create(
                author=user, title=title,
                content=content, image=image
            )

        context['post_obj'] = post_obj
        context['form'] = form
    except Exception as e:
        print(e)

    return render(request, 'update_post.html', context)


def comment_details(request, slug):
    context = {}
    try:
        comment_obj = Comment.objects.get(slug=slug)
        context['comment_obj'] = comment_obj
    except Exception as e:
        print(e)
    return render(request, 'post_detail.html', context)

def add_comment(request, slug):
    post = Post.objects.get(slug=slug)
    initial_data = {'title': post.title, 'content': ''}
    context = {'form': CommentForm(initial=initial_data), 'post_obj': post}
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            author = request.user
            text = form.cleaned_data['content']
            new_comment = Comment.objects.create(post=post, author=author, text=text)
            print(new_comment)
            return redirect('post_detail', slug=slug)
        else:
            context['form'] = form
    
    return render(request, 'add_comment.html', context)

def post_delete(request, id):
    try:
        post_obj = Post.objects.get(id=id)

        if post_obj.author == request.user:
            post_obj.delete()

    except Exception as e:
        print(e)

    return redirect('/see-post/')

def comment_delete(request, id, slug):
    try:
        comment_obj = Comment.objects.get(id=id)
        
        if comment_obj.author == request.user:
            comment_obj.delete()

    except Exception as e:
        print(e)

    return redirect('post_detail', slug=slug)

def register_view(request):
    return render(request, 'register.html')


def verify(request, token):
    try:
        profile_obj = Profile.objects.filter(token=token).first()

        if profile_obj:
            profile_obj.is_verified = True
            profile_obj.save()
        return redirect('/login/')

    except Exception as e:
        print(e)

    return redirect('/')