//Cloud Website shared variables
var CWShare = {};

$(function()
{   //Check login status to show different content
    $.get("/Dynamic/Users/LoginStatus",function(_data,status)
    {   //Parse JSON
        var data = JSON.parse(_data);
        
        //Prompt when failed to fetch data
        if (status!="success")
        {   window.alert("检测到网站数据未能正确加载，部分功能不能使用。\n" +
                "* 您使用的浏览器或操作系统过于老旧，请更换浏览器或系统再浏览。\n" +
                "* 您的网络或服务器端不稳定或存在问题。");
            return;
        }
        
        //Show log-in region
        if (data.Logged==true)
        {   $("#login_form").hide();
            $("#logged_user_email").text(data.Email);
        }
        //Show log-in form
        else
        {   $("#login_region").hide();
        }
        
        //Share variables with the whole page
        CWShare.Logged = data.Logged;
        if (CWShare.Logged)
        {   CWShare.Email = data.Email;
            CWShare.Username = data.Username;
        }
    });
    
    //Log-in action
    $("#login_submit").on("click",function()
    {   //Get email and password
        var email = $("#inputEmail").val();
        var pswd = $("#inputPassword").val();
        
        //Email or password is empty
        if ((email=="")||(pswd==""))
            window.alert("用户名或密码为空！");
        else
        {   $.post("/Dynamic/Users/Login",{Email:email,Password:pswd,csrfmiddlewaretoken:$.cookie("csrftoken")},function(data)
            {   if (data.Status=="Success")
                    location.reload(false);
                else
                    window.alert({
                        "CredentialNotCorrect":"用户名或密码错误！",
                        "AlreadyLogged":"用户已经登录！"
                    }[data.Reason]);
            },"json");
        }
    });
    
    //Log-out action
    $("#logout_link").on("click",function()
    {   $.post("/Dynamic/Users/Logout",{csrfmiddlewaretoken:$.cookie("csrftoken")},function()
        {   location.reload();
        });
    });
});
