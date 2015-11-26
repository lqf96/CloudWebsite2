//Initialization
$(function()
{
    //Log-in action
    $("#LoginBtn").on("click",function()
    {   //Get email and password
        var email = $("#r_inputEmail").val();
        var pswd = $("#r_inputPassword").val();
        
        //Disable log-in button for 1 second
        $("#LoginBtn").addClass("disabled");
        setTimeout(function()
        {   $("#LoginBtn").removeClass("disabled");
        },1000);
        
        //Email or password is empty
        if ((email=="")||(pswd==""))
        {   $("#LoginStatusPanel").attr("class","panel panel-danger");
            $("#LoginStatus").text("登录失败：用户名或密码为空！");
        }
        else
        {   $.post("/Dynamic/Users/Login",{Email:email,Password:pswd,csrfmiddlewaretoken:$.cookie("csrftoken")},function(data)
            {   if (data.Status=="Success")
                {   var _next_url = $.url().param("Next");
                    if (_next_url)
                        location.href = atob(_next_url);
                    else
                        location.href = "/";
                }
                else
                {   $("#LoginStatusPanel").attr("class","panel panel-danger");
                    $("#LoginStatus").text("登录失败："+{
                        "CredentialNotCorrect":"用户名或密码错误！",
                        "UserAlreadyLogged":"用户已经登录！"
                    }[data.Reason]);
                }
            },"json");
        }
    });
    
    //Check if the user is already logged or not
    CW.Hooks.LoginStatusChecked.then(function()
    {   //Not logged
        if (!CW.Credential.Logged)
        {   $("#LoggedUserPrompt").hide();
        }
        //Logged
        else
        {   $("#LoginStatusPanel").hide();
            $("#LoginForm").hide();
            
            //Redirect to main page after ten seconds
            setTimeout(function()
            {   location.href = "/";
            },10000);
        }
    });
});