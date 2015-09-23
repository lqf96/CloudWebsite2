//Angular app
var cwf = angular.module("cw_forum",[]);

//===== Basic functions & constants =====
//Time formatter
CWShare.FmtTime = function(time_str)
{   //Make time object
    var time = new Date(time_str);
    
    //Create time string
    return ""+(1900+time.getYear())+"-"+time.getMonth()+"-"+time.getDay()
        +" "+time.getHours()+":"+time.getMinutes()+":"+time.getSeconds();
}

//Post entry per page
CWShare.EntryPerPage = 20;

//===== App controllers =====
//Forum boards controller
cwf.controller("BoardsController",function($scope,$http,$location)
{   $http.get("/Dynamic/DZ/GetBoardList").success(function(Resp)
    {   //Set global variable
        CWShare.Boards = Resp.Result;
        //Save all address parameters
        CWShare.Search = $location.search();
        
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
        CWShare.Search.Board = $scope.CurrentBoard = BoardFound?BoardName:CWShare.Boards[0];
    });
});

//Post list controller
cwf.controller("PostListController",function($scope,$http)
{   //No boards
    if ("NoBoard" in CWShare.Boards[0])
    {   $scope.NoPost = true;
        return;
    }
    
    //Get page number
    var PageNumber = parseInt(CWShare.Search["Page"]||"0");
    CWShare.Search.Page = (PageNumber.toString()=="NaN")?0:PageNumber;
    
    //Get posts in range
    $http.get("/Dynamic/DZ/GetBoard",
    {params:{
        "Board":CWShare.Search.Board,
        "Page":CWShare.Search.Page
    }}).success(function(Resp)
    {   var Data = Resp.Result;
        //Calculate page amount
        CWShare.PageAmount = Math.ceil(Data.PostAmount/CWShare.EntryPerPage);
        
        //Copy post list
        if (Data.Posts.length!=0)
        {   $scope.PostList = Data.Posts;
            $scope.NoPost = false;
        }
        //No post available
        else
            $scope.NoPost = true;
    });
});

//Page switch controller
cwf.controller("PageController",function($scope,$window)
{   //Show current page number
    $scope.PageNumberText = ""+(CWShare.Search.Page+1);
    //Go to page
    $scope.GoToPage = function(Page)
    {   //Extra processing for string
        if (typeof(Page)=="string")
        {   Page = parseInt(Page); 
            if (Page.toString()=="NaN")
            {   $window.alert("输入的页数非法，请重新输入！");
                return;
            }
        }
        
        //Restrict page number in a range
        if (Page<0)
            Page = 0;
        else if (Page>=CWShare.PageAmount)
            Page = (CWShare.PageAmount==0)?0:CWShare.PageAmount-1;
        
        //Go to page
        $window.location.href = "/forum.html?Board="+CWShare.Search.Board+"&Page="+Page;
    }
});

//Forum new post controller
cwf.controller("NewPostController",function($scope,$http,$window)
{   //No boards
    $scope.DisableNewPost = ("NoBoard" in CWShare.Boards[0]);
    
    //Submit form
    $scope.Submit = function()
    {   $http.post("/Dynamic/DZ/NewPost",
        {
            "Title":$scope.Title,
            "Content":$scope.Content,
            "Board":CWShare.Search.Board,
            "csrfmiddlewaretoken":$.cookie("csrftoken")
        }).success(function()
        {   $window.location.reload();
        });
    };
});
