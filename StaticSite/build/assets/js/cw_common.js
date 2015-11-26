//Cloud website variable namespace
//Root namespace
var CW = {};

//Hooks namespace
CW.Hooks = {
    //* Log-in
    //Check login status to show different content
    "LoginStatusChecked":$.get("/Dynamic/Users/LoginStatus",function(data)
    {   
        //Create user credential namespace
        CW.Credential = {};
        //Set credentials
        CW.Credential.Logged = data.Logged;
        if (CW.Credential.Logged)
        {   CW.Credential.Email = data.Email;
            CW.Credential.Username = data.Username;
        }
    })
};

//Site configurations
CW.Conf = {
    //* Relative links
    "RootDomain":"thcloud.org",
    "RelativePathElements":["a","link"],
    "RelativePathProps":["href","src"]
};

$(function()
{   
    //* Log-in
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
    
    //* Relative links
    //Generate absolute addresses from configurations
    for (i in CW.Conf.RelativePathElements)
    {   var ElementName = CW.Conf.RelativePathElements[i];
        $(ElementName+".cw-relative-url").each(function()
        {   for (j in CW.Conf.RelativePathProps)
            {   var PropName = CW.Conf.RelativePathProps[j];
                if (!$(this).attr("cw-"+PropName+"-domain"))
                    continue;
                
                var AbsoluteURL = "https://"+$(this).attr("cw-"+PropName+"-domain")+"."+CW.Conf.RootDomain;
                if ($(this).attr("cw-"+PropName+"-path"))
                    AbsoluteURL += $(this).attr("cw-"+PropName+"-path");
                $(this).attr(PropName,AbsoluteURL);
            }
        });
    }
});
