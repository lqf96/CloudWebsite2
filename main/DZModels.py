# Django libraries
from django.db import models

# Discussion zone boards
class DiscussionZoneBoard(models.Model):
    Name = models.CharField(max_length=24)
    PostAmount = models.BigIntegerField()
    Description = models.TextField()
    
    class Meta:
        app_label = "main"

# Discussion zone posts
class DiscussionZonePost(models.Model):
    PostID = models.BigIntegerField()
    Board = models.CharField(max_length=24)
    Title = models.CharField(max_length=64)
    Author = models.CharField(max_length=32)
    Time = models.DateTimeField()
    LastReply = models.CharField(max_length=32)
    LastReplyTime = models.DateTimeField()
    ReplyAmount = models.BigIntegerField()
    
    class Meta:
        app_label = "main"

# Discussion zone post content and reply
class DiscussionZoneContent(models.Model):
    Board = models.CharField(max_length=24)
    PostID = models.BigIntegerField()
    ContentID = models.BigIntegerField()
    Author = models.CharField(max_length=24)
    Content = models.TextField()
    Time = models.DateTimeField()
    
    class Meta:
        app_label = "main"