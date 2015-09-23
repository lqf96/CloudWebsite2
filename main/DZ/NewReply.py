#encoding=utf-8
# Django libraries
from django.http import HttpResponse
# Models
from main.DZModels import DiscussionZonePost,DiscussionZoneContent
# Python system libraries
import json,string
from datetime import datetime

# Make a new reply
def POST(request):
    # Check if the user is logged
    if ("Logged" not in request.session) or (request.session["Logged"]==False):
        return HttpResponse(json.dumps({"Status":"Failed","Reason":"NotLogged"}),content_type="application/json")
    
    # Get post ID
    try:
        _PostID = string.atoi(request.POST.get("PostID","0"))
    except ValueError:
        return HttpResponse(json.dumps({"Status":"Failed","Reason":"InvaildPostID"}),content_type="application/json")
    # Get board name
    _Board = request.POST.get("Board","")
    
    # Try to get post from post ID and board name
    try:
        Post = DiscussionZonePost.objects.get(Board=_Board,PostID=_PostID)
    except:
        return HttpResponse(json.dumps({"Status":"Failed","Reason":"PostNotExist"}),content_type="application/json")
    
    # Create new post content object
    NewPostContent = DiscussionZoneContent()
    NewPostContent.Board = _Board
    NewPostContent.PostID = Post.PostID
    NewPostContent.ContentID = Post.ReplyAmount
    NewPostContent.Author = request.session["Username"]
    NewPostContent.Content = request.POST.get("Content","[无内容]")
    NewPostContent.Time = datetime.now()
    # Save new post content object
    NewPostContent.save()
    
    # Update post reply amount
    Post.ReplyAmount += 1
    Post.save()
    
    # Return success message
    return HttpResponse(json.dumps({"Status":"Success"}),content_type="application/json")