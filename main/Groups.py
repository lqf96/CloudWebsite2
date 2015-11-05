# Models
from UserModels import User,Group
# Django libraries
from django.http import HttpResponse
# Python system libraries
import re,json

# [Helper Functions]
# InGroup function initialization
# Condition type dictionary and condition handler (For string and regular expression)
__CondTypeDict = {}
__CondTypeDict["str"] = lambda user,cond,group: cond==group
__CondTypeDict["SRE_Pattern"] = lambda user,cond,group: cond.match(group)!=None
__CondTypeDict["tuple"] = lambda user,cond,group: apply(__CalcOrCond,[user,]+cond)
__CondTypeDict["list"] = lambda user,cond,group: apply(__CalcAndCond,[user,]+cond)

# Calculate and conditions
def __CalcAndCond(user,*and_cond):
    for cond in and_cond:
        for group in user.Group_set.all():
            if __CondTypeDict[type(cond).__name__](user,cond,group.Name):
                break
        else:
            return False
    return True

# Calculate or conditions
def __CalcOrCond(user,*or_cond):
    result = False
    for cond in or_cond:
        for group in user.Group_set.all():
            if __CondTypeDict[type(cond).__name__](user,cond,group.Name):
                result = True
                break
        if result:
            return True
    return False

# Check if user matches given group conditions
# (Wrapper function, call __CalcOrCond)
def InGroup(*cond):
    current_user = User.objects.get(Email=request.session["Email"])
    apply(__CalcOrCond,[current_user,]+cond)

# Group-specific view docorator
def GroupSpecific(*cond):
    def Decorator(view):
        def NewView(request):
            # Group condition satisfied
            if apply(InGroup,cond):
                return view(request)
            # Not satisfied, return error
            else:
                return HttpResponse(json.dumps({"Status":"Failed","Reason":"UserNotInGivenGroup"}),content_type="application/json")
        return NewView
    return Decorator

# Create a new group
def CreateGroup(name):
    if GetGroup(name)==None:
        new_group = Group()
        new_group.Name = name
        new_group.save()

# Remove an existing group
def RemoveGroup(name):
    remove_group = GetGroup(name)
    remove_group.delete()

# Get group by name
def GetGroup(name):
    try:
        result_group = Group.objects.get(name)
        return result_group
    except:
        return None

# Check if a group exists (Alias for get group function)
GroupExists = GetGroup

# Add user to group
def AddUserToGroup(group_name,user_email):
    pass

# Remove user from group
def RemoveUserFromGroup(group_name,user_email):
    pass
