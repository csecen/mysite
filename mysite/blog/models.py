from django.db import models

# Create the blog model. This will contain all the field required for a post
class Post(models.Model):

    # All required fields for a post
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    text = models.TextField()
    auth = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)
    cover_image = models.ImageField(upload_to='cover', blank=True)
    read_time = models.CharField(max_length=15)

# Create the comment model. Comment relate to posts. There can be multiple comments per post
class Comment(models.Model):

    # All required fields for a comment on a post
    comment_text = models.TextField()
    comment_time = models.DateTimeField(auto_now_add=True)
    comment_auth = models.CharField(max_length=50, blank=True)
    comment_authorized = models.BooleanField(default=False)
    related_post = models.ForeignKey(Post, on_delete=models.CASCADE)
