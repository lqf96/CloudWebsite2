#encoding=utf-8
# Django libraries
from django.http import HttpResponse
# Models
from main.DZModels import DiscussionZoneBoard,DiscussionZonePost,DiscussionZoneContent
# Python system libraries
import json
from datetime import datetime

# Make new post
def POST(request):
    # Check if the user is logged
    if ("Logged" not in request.session) or (request.session["Logged"]==False):
        return HttpResponse(json.dumps({"Status":"Failed","Reason":"NotLogged"}),content_type="application/json")
    
    # Get board name
    BoardName = request.POST.get("Board","")
    # Try to get board from name
    try:
        _Board = DiscussionZoneBoard.objects.get(Name=BoardName)
    except:
        return HttpResponse(json.dumps({"Status":"Failed","Reason":"BoardNotExist"}),content_type="application/json")
    
    # Make a post
    NewPost = DiscussionZonePost()
    NewPost.PostID = _Board.PostAmount
    NewPost.Board = _Board.Name
    NewPost.Title = request.POST.get("Title","[无标题]")
    NewPost.Author = NewPost.LastReply = request.session["Username"]
    NewPost.Time = NewPost.LastReplyTime = datetime.now()
    NewPost.ReplyAmount = 1
    # Save the post
    NewPost.save()
    
    # Modify and save board information
    _Board.PostAmount += 1
    _Board.save()
    
    # Create a post content record
    NewPostContent = DiscussionZoneContent()
    NewPostContent.PostID = NewPost.PostID
    NewPostContent.Board = BoardName
    NewPostContent.ContentID = 0
    NewPostContent.Author = NewPost.Author
    NewPostContent.Time = NewPost.Time
    NewPostContent.Content = request.POST.get("Content","[无内容]")
    # Save the post content
    NewPostContent.save()
    
    # Return success message
    return HttpResponse(json.dumps({"Status":"Success"}),content_type="application/json")