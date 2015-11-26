//===== Register form validation =====
//Validation record
var validation_passed = {"email":false,"name":false,"password":false,"password2":false};

//Check Email
function checkemail(){
	var email = $("#r_inputEmail").val();
	var reg = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
	var ismail= reg.test(email);
	
	if (!ismail)
	{
		$("#checkEmail").text("邮箱格式不正确，请重新填写");
        validation_passed.email = false;
	}
	else
	{
		$("#checkEmail").text("邮箱格式正确");
        validation_passed.email = true;
	}
}

//Check Confirmed Password
function confirmpassword(){
	var password = $("#r_inputPassword").val();
	var password_again = $("#confirmPassword").val();
	
	if(password == password_again){
		$("#samePassword").text("密码相同");
        validation_passed.password2 = true;
	}
	else
	{
		$("#samePassword").text("密码不同");
        validation_passed.password2 = false;
	}
}

//Chech password strength
function passwordstrength(){
	var password = $("#r_inputPassword").val();
	var strongRegex = new RegExp("^(?=.{8,})(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*\W).*$", "g");
	var mediumRegex = new RegExp("^(?=.{7,})(((?=.*[A-Z])(?=.*[a-z]))|((?=.*[A-Z])(?=.*[0-9]))|((?=.*[a-z])(?=.*[0-9]))).*$", "g");
	var enoughRegex = new RegExp("(?=.{6,}).*", "g");
	
	if (password.length==0){
		$("#strength").text("密码为空！");
        validation_passed.password = false;
	}
	else if(strongRegex.test(password)){
		$("#strength").text("密码强度：强");
        validation_passed.password = true;
	}
	else if(mediumRegex.test(password)){
		$("#strength").text("密码强度：中");
        validation_passed.password = true;
	}
	else {
		$("#strength").text("密码强度：弱");
        validation_passed.password = true;
	}
}

//Check if name is written
function check_name()
{   if ($("#r_username").val()=="")
    {   $("#checkName").text("名字为空");
        validation_passed.name = false;
    }
    else
    {   $("#checkName").text("名字正确");
        validation_passed.name = true;
    }
}

//===== Registration Process =====
//Submit register form
function SubmitRegForm()
{   //Check if validations passed
    for (item in validation_passed)
        if (validation_passed[item]==false)
        {   //Prompt validation not passed
            $("#RegStatus").text("您的账户信息输入有误，请重新输入！");
            $("#RegStatusPanel").attr("class","panel panel-danger");
            //Exit
            return;
        }
    
    //Disable register button for 8 seconds
	$("#RegisterBtn").addClass("disabled");
	setTimeout(function()
	{	$("#RegisterBtn").removeClass("disabled");
	},8000);
    
    //Send AJAX request
	$.post("/Dynamic/Users/UserReg1",
        {Email:$("#r_inputEmail").val(),
		Password:$("#r_inputPassword").val(),
		Username:$("#r_username").val(),
        MoreInfo:$("#moreInfo").val(),
        csrfmiddlewaretoken:$.cookie("csrftoken")},
		//Callback function
		function(Data,Status)
		{	//Successfully receives data
			if (Status=="success")
			{	//Failed to send email
				if (Data.Status=="Failed")
				{	var Desceription = {
				        "UserAlreadyLogged":"用户已经登录！",
				        "DuplicatedUserNameOrEmail":"用户名或邮箱已被使用！",
				        "FailedToSendMail":"邮件发送失败。"
				    }[Data.Reason];
				    
				    //Show failed reason
					$("#RegStatus").text("注册失败。原因："+Desceription);
					$("#RegStatusPanel").attr("class","panel panel-danger")
				}
				//Succeed
				else
				{	//Show success text
					$("#RegStatus").html("注册成功。激活邮件已经发送到您的邮箱，请激活您的账户。");
					$("#RegStatusPanel").attr("class","panel panel-success");
				}
			}
			//Failed to get data
			else
			{	//Show failed reason
				$("#RegStatus").text("注册失败。原因：连接异常。");
				$("#RegStatusPanel").attr("class","panel panel-danger")
			}
		},"json");
}

//===== Initialization =====
$(function()
{
    //Check if the user is already logged or not
    CW.Hooks.LoginStatusChecked.then(function()
    {   //Not logged
        if (!CW.Credential.Logged)
            $("#LoggedUserPrompt").hide();
        //Logged
        else
        {   $("#RegStatusPanel").hide();
            $("#RegForm").hide();
            
            //Redirect to main page after ten seconds
            setTimeout(function()
            {   location.href = "/";
            },10000);
        }
    });
});