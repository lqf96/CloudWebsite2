//===== Basic functions & constants =====
//Time formatter
function FmtTime(time_str)
{   //Make time object
    var time = new Date(time_str);
    
    //Create time string
    return ""+(1900+time.getYear())+"-"+time.getMonth()+"-"+time.getDay()
        +" "+time.getHours()+":"+time.getMinutes()+":"+time.getSeconds();
}

//Post entry per page
var EntryPerPage = 20;

//===== Page Rendering =====
//Main program
$(function()
{   //Get boards list
    $.get("/Dynamic/DZ/GetBoardList",function(Resp)
    {   //Set global variable
        CWShare.Boards = Resp.Result;
        //Save all search parameters
        var SearchArray = location.search.substr(1).split("&");
        CWShare.Search = {};
        for (SearchSubStr in SearchArray)
            {   var SubStrResult = SearchSubStr.match(/^(.*)=(.*)$/);
                if (SubStrResult)
                    CWShare.Search[SubStrResult[1]] = SubStrResult[2];
            }
        
        //No board available
        if (CWShare.Boards.length==0)
            CWShare.Boards.push({
                "Name":"（无板块）",
                "PostAmount":0,
                "Description":"并没有什么介绍... (~_~')",
                "NoBoard":true
            });
        
        //Select the board according to parameter
        var BoardFound = false;
        var BoardName = CWShare.Search["Board"]||CWShare.Boards[0];
        for (BoardObj in CWShare.Boards)
            if (BoardObj.Name==BoardName)
            {   BoardFound = true;
                break;
            }
        CWShare.Search.Board = BoardFound?BoardName:CWShare.Boards[0];
        
        //Render board list
        for (BoardObj in CWShare.Boards)
        {   var BoardLabel = $("<li />").append(
                $("<a />").attr("href","/forum.html?Board="+BoardObj.Name)
                    .text(BoardObj.Name));
            if (BoardObj.Name==CWShare.Search.Board)
                BoardLabel.addClass("active");
            BoardLabel.appendTo($("#FBoardList"));
        }
    //Get post list
    }).then(function()
    {   //No boards available
        if ("NoBoard" in CWShare.Boards[0])
        {   $("#FPostList").append($("<tr />")
                .append($("<td />")
                    .attr("colspan","5")
                    .attr("align","center")
                    .text("目前还没有任何板块！('_')")));
            return;
        }
        
        //Get page number
        var PageNumber = parseInt(CWShare.Search["Page"]||"0");
        CWShare.Search.Page = (PageNumber.toString()=="NaN")?0:PageNumber;
        
        //Get posts in range
        $.get("/Dynamic/DZ/GetBoard",
        {
            "Board":CWShare.Search.Board,
            "Page":CWShare.Search.Page
        },function(Resp)
        {   //Get result
            var Data = Resp.Result;
            //Calculate page amount
            CWShare.PageAmount = Math.ceil(Data.PostAmount/CWShare.EntryPerPage);
        
            //Show post list
            if (Data.Posts.length!=0)
                for (Post in Data.Posts)
                    $("#FPostList").append($("<tr />")
                        .append($("<td />")
                            .text(Post.Title))
                        .append($("<td />")
                            .text(Post.Author))
                        .append($("<td />")
                            .text(FmtTime(Post.Time)))
                        .append($("<td />")
                            .text(Post.ReplyAmount-1))
                        .append($("<td />")
                            .text(Post.LastReply)));
            //No post available
            else
                $("#FPostList").append($("<tr />")
                    .append($("<td />")
                        .attr("colspan","5")
                        .attr("align","center")
                        .text("该页面/板块还没有帖子哦。")));
        //Page switching
        }).then(function()
        {   //Show current page number and total page number
            $("#FTPageNumber").val(CWShare.Search.Page+1);
            $("#FPageAmount").val(CWShare.PageAmount);
        });
    //New post form
    }).then(function()
    {   //Non-logged user
        if (!CWShare.Logged)
        {   $("#FNewPost").css("display","none");
            return;
        }
        //Logged user
        else
            $("#FNewPostNonLogged").css("display","none");
        
        //No boards available
        if ("NoBoard" in CWShare.Boards[0])
            $("#FNewPostSubmit").addClass("disabled");
        
        //Post data when submitted
        $("#FNewPostSubmit").on("click",function()
        {   $.post("/Dynamic/DZ/NewPost",
            {
                "Title":$("#FNewPostTitle").val(),
                "Content":$("#FNewPostContent").val(),
                "Board":CWShare.Search.Board,
                "csrfmiddlewaretoken":$.cookie("csrftoken")
            },function()
            {   location.reload();
            });
        });
    });
});

//Go to page function
function GoToPage(Page)
{   //Extra processing for string
    if (typeof(Page)=="string")
    {   Page = parseInt(Page); 
        if (Page.toString()=="NaN")
        {   window.alert("输入的页数非法，请重新输入！");
            return;
        }
    }
    
    //Restrict page number in a range
    if (Page<0)
        Page = 0;
    else if (Page>=CWShare.PageAmount)
        Page = (CWShare.PageAmount==0)?0:CWShare.PageAmount-1;
    
    //Go to page
    window.location.href = "/forum.html?Board="+CWShare.Search.Board+"&Page="+Page;
}