# Django libraries
from django.http import HttpResponse
# Models
from main.DZModels import DiscussionZoneBoard,DiscussionZonePost
# Python system libraries
import json,string
# CloudWebsite foundation
from CloudWebsite.CWFoundation import TimeStr

# Constants
POST_PER_PAGE = 20

# Get board information and post list
def GET(request):
    # Get board name
    BoardName = request.GET.get("Board","")
    # Get board meta information
    try:
        _Board = DiscussionZoneBoard.objects.get(Name=BoardName)
    except:
        return HttpResponse(json.dumps({"Status":"Failed","Reason":"BoardNotExist"}),content_type="application/json")
    
    # Get page number
    try:
        Page = string.atoi(request.GET.get("Page","0"))
    except:
        return HttpResponse(json.dumps({"Status":"Failed","Reason":"IllegalPageNumber"}),content_type="application/json")
    # Get board post list and post information
    BoardPosts = DiscussionZonePost.objects.filter(Board=BoardName,PostID__gte=Page*POST_PER_PAGE,PostID__lt=(Page+1)*POST_PER_PAGE)
    
    # Make result
    Result = {"Name":_Board.Name,"PostAmount":_Board.PostAmount,"Description":_Board.Description}
    Result["Posts"] = [{"PostID":Post.PostID, \
        "Title":Post.Title, \
        "Author":Post.Author, \
        "Time":TimeStr(Post.Time), \
        "LastReply":Post.LastReply, \
        "LastReplyTime":TimeStr(Post.LastReplyTime), \
        "ReplyAmount":Post.ReplyAmount} for Post in BoardPosts.all()]
    # Return result
    return HttpResponse(json.dumps({"Status":"Success","Result":Result}),content_type="application/json")