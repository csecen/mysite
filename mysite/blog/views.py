from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import CommentForm

# Display the homepage of the site. This is where users will be directed when they
# first visit the site
def showMainPage(request):
    # Get set of all posts
    posts = Post.objects.all()

    return render(request, 'home.html', {'posts':posts})

# Display the about page. This functions just renders the html file holding the
# about information
def showAboutPage(request):

    return render(request, 'about.html', {})

# Display the individual blog post to its own page. This takes the id of the post
# as well as all comments relating to the post and passes them to the html file
def showIndividualPost(request, id):
    # Get specific post matching the id passed to the function
    post = Post.objects.get(id=id)
    comments = Comment.objects.filter(related_post=id)

    return render(request, 'individualPost.html', {'post':post, 'comments':comments})

# Display the contact page. This function just renders the html file holding the
# contact information
def showContactPage(request):

    return render(request, 'contact.html', {})

# Displays the comment form. This function allows users to add a comment that relates to
# a specific post on the site. If the user fills out the form properly, they will be redirected
# back to the page containing just the information about the specific post
def addCommentPage(request, id):
    post = Post.objects.get(id=id)
    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.related_post = post
            comment.save()
            return redirect('showIndividualPost', id)
    else:
        form = CommentForm()

    return render(request, 'comment.html', {'post':post, 'form':form})
