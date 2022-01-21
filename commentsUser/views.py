from django.shortcuts import render, redirect

# Create your views here.
from mainapp.models import NewsPost
from .models import CommentsPost
from .forms import CommentsPostForm
from accounts.models import CustomUser


from hitcount.models import HitCount
from hitcount.views import HitCountMixin


def post_details(request, pk):
    post = NewsPost.objects.get(id=pk)
    # comment_author = CustomUser.objects.get(id=slug)
    user = request.user
    # Counting number of comments
    qty_comment = CommentsPost.objects.filter(post=post.id).count()
    # Count number of views
    hit_count = HitCount.objects.get_for_object(post)
    hit_count_response = HitCountMixin.hit_count(request, hit_count)
    # Posting last three posts
    lastThreeNews = NewsPost.objects.order_by('-date')[:3]

    # Write comment
    new_comment=None
    comment_form = CommentsPostForm()
    if request.method == 'POST':
        comment_form = CommentsPostForm(request.POST)
        if comment_form.is_valid():
            parent_obj = None
            try:
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None
            if parent_id:
                parent_obj = CommentsPost.objects.get(id=parent_id)
                if parent_obj:
                    parent_comment = comment_form.save(commit=False)
                    parent_comment.parent = parent_obj
                    
            new_comment = comment_form.save(commit=False)
            # author = CustomUser.objects.filter(email=user.email).first()
            new_comment.post = post
            # new_comment.comment_author = author
            
            new_comment.save()
            # return redirect('post_details',id=slug)
            return redirect('post_details',post.id)
        else:
            comment_form = CommentsPostForm()

    context = {
        'comment_form':comment_form,
        'post':post,
        'qty_comment':qty_comment,
        'lastThreeNews':lastThreeNews,
        'hit_count':hit_count,
        'hit_count_response':hit_count_response,
        'new_comment':new_comment,

        # 'viewrCount':viewrCount
        # 'popular_posts':popular_posts
    }
    return render(request, 'post-details.html', context)