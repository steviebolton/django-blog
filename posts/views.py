from django.shortcuts import render, get_object_or_404, HttpResponse, redirect, HttpResponse
from .models import Post
from .forms import BlogPostForm
from django.db.models import Q

# Create your views here.
def posts_list(request):
    posts = Post.objects.all()
    return render(request, "posts/posts_list.html" , {"posts": posts})
    
def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    post.views +=1
    post.save()
    can_edit = request.user == post.author or request.user.is_superuser
    does_like = request.user.profile in post.liked_by.all()
    
    return render(request, "posts/post_detail.html", {'post': post , 'can_edit': can_edit , 'does_like': does_like})
    
def add_post(request):
    if request.method=="POST":
        form = BlogPostForm(request.POST, request.FILES)
        
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect("posts_list")
        else:
            return render(request, "posts/post_form.html", {"form": form})
    
    else:
        form = BlogPostForm()
        return render(request, "posts/post_form.html", {"form": form})
        
def search_posts(request):
    query = request.GET['q']
    
    query_by_title = Q(title__contains=query)
    query_by_content = Q(content__contains=query)
    posts = Post.objects.filter(query_by_title | query_by_content)
    
    return render(request, "posts/posts_list.html", {'posts': posts})

def edit_post(request, id):
    # Load the post we're changing, from the DB
    post = get_object_or_404(Post, pk=id)

    if request.method == "POST":
        # Get the new values from the Form
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        
        # Update the DB with the differences
        if form.is_valid():
            form.save()
            return redirect("post_detail", id=id) 
        else:
             return render(request, "posts/post_form.html", {"form": form})
    else:
        form = BlogPostForm(instance=post)
        return render(request, "posts/post_form.html", {"form": form})


def like_post(request, id):
    post = get_object_or_404(Post, pk=id)
    request.user.profile.likes.add(post)
    return redirect("post_detail", id=post.id) 
    
    
def unlike_post(request, id):
    post = get_object_or_404(Post, pk=id)
    request.user.profile.likes.remove(post)
    return redirect("post_detail", id=post.id)
    
    # , {'post': post} , {'post': title} , {'post': content}
    
    
    
