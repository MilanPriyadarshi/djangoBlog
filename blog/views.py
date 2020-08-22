from django.shortcuts import render,HttpResponse,redirect
from .models import Post,BlogComment
from django.contrib import messages
# Create your views here.
def blog(request):
    allPosts=Post.objects.all()
    context={'allPosts':allPosts}
    return render(request,'blog/blogHome.html', context)

def blogPost(request,slug):
    post=Post.objects.filter(slug=slug).first()
    post.views=post.views + 1
    post.save()
    comments= BlogComment.objects.filter(post=post)
    context={'post':post , 'comments':comments, 'user': request.user}
    return render(request,'blog/blogPost.html',context)


def postComment(request):
    if request.method == 'POST':
        comment=request.POST.get("comment")
        user=request.user
        postSno=request.POST.get("postSno")
        post=Post.objects.get(sno=postSno)
        comment= BlogComment(comment=comment,user=user,post=post)
        comment.save()
        messages.success(request,"Your Comment posted Successfully")
    return redirect(f"/blog/{post.slug}")

