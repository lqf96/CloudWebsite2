# Django libraries
from django.http import HttpResponse
# Models
from main.DZModels import DiscussionZoneBoard
# Python system libraries
import json

# Get board list (Restful API)
def GET(request):
    result = [{"Name":Board.Name,"PostAmount":Board.PostAmount,"Description":Board.Description} for Board in DiscussionZoneBoard.objects.all()]
    return HttpResponse(json.dumps({"Status":"Success","Result":result}),content_type="application/json")
