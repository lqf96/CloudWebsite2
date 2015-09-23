# Django libraries
from django.http import HttpResponse
# Models
from main.DZModels import DiscussionZonePost,DiscussionZoneContent
# Python system libraries
import json,string
# CloudWebsite foundation
from CloudWebsite.CWFoundation import TimeStr

# Constants
POST_PER_PAGE = 20

# Get post, post content and replys
def GET(request):
    # Get post ID
    try:
        _PostID = string.atoi(request.GET.get("PostID","0"))
    except ValueError:
        return HttpResponse(json.dumps({"Status":"Failed","Reason":"InvaildPostID"}),content_type="application/json")
    # Get board name
    BoardName = request.GET.get("Board","")
    # Get page number
    try:
        Page = string.atoi(request.GET.get("Page","0"))
    except:
        return HttpResponse(json.dumps({"Status":"Failed","Reason":"IllegalPageNumber"}),content_type="application/json")
    
    # Try to get post from post ID and board name
    try:
        Post = DiscussionZonePost.objects.get(Board=BoardName,PostID=_PostID)
    except:
        return HttpResponse(json.dumps({"Status":"Failed","Reason":"PostNotExist"}),content_type="application/json")
    
    # Get all post content
    PostContentQuerySet = DiscussionZoneContent.objects.filter(Board=BoardName,PostID=_PostID, \
        ContentID__gte=Page*POST_PER_PAGE,ContentID__lt=(Page+1)*POST_PER_PAGE)
    
    # Create result object
    result = {"Title":Post.Title, \
        "Author":Post.Author, \
        "Time":TimeStr(Post.Time), \
        "LastReply":Post.LastReply, \
        "LastReplyTime":TimeStr(Post.LastReplyTime), \
        "ReplyAmount":Post.ReplyAmount}
    # Attach post content to result
    result["Content"] = [{"ContentID":PostContent.ContentID, \
        "Author":PostContent.Author, \
        "Content":PostContent.Content, \
        "Time":TimeStr(PostContent.Time)} for PostContent in PostContentQuerySet.all()]
    
    # Return result
    return HttpResponse(json.dumps({"Status":"Success","Result":result}),content_type="application/json")