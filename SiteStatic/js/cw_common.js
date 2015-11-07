//Cloud website variable namespace
//Root namespace
var CW = {};
//Hooks
CW.Hooks = {};

$(function()
{   //Check login status to show different content
    CW.Hooks.LoginStatusChecked = $.get("/Dynamic/Users/LoginStatus",function(data)
    {   
        //Create user credential namespace
        CW.Credential = {};
        //Set credentials
        CW.Credential.Logged = data.Logged;
        if (CW.Credential.Logged)
        {   CW.Credential.Email = data.Email;
            CW.Credential.Username = data.Username;
        }
    });
    
    //Hide or show regions according to login status
    CW.Hooks.LoginStatusChecked.then(function()
    {
        //Show log-in region
        if (CW.Credential.Logged)
        {   $("#logout_region").hide();
            $("#logged_user_name").text(CW.Credential.Username);
        }
        //Show log-out region
        else
            $("#login_region").hide();
    });
    
    //Set log-out link action
    $("#logout_link").on("click",function()
    {   $.post("/Dynamic/Users/Logout",{csrfmiddlewaretoken:$.cookie("csrftoken")},function()
        {   location.reload();
        });
    });
});
