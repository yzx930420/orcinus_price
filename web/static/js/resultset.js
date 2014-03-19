$(function () {
    $(".search_option").each(function () {
        $(this).click(function () {
            var option = $(this).html() + "<span class='caret'></span>";
            $("#action").val($(this).attr("action"));
            $("#search_type").html(option);
        });
    });


    var animate_time = 300;//动画时间：0.3秒
    var picnumber = $(".scrollpic li").size() - 1;//计算广告的数量
    var slideclick = 0;//初始化
    var slideWidth = $("#focus").width() * (-1);
    var smallSlideWidth = $(".scrollbox .scrollpic li").eq(0).width() * (-1);
    $(".scrollbox .scrollpic li").eq(0).addClass("current");

    //小图点击时，开始动画
    $(".scrollpic li").click(function () {

        slideclick = $(".scrollpic li").index($(this));

        $(".scrollpic li").removeClass("current");
        $(this).addClass("current");

        //大图上移
        $("#focus #focuspic").animate({"marginLeft": slideclick * slideWidth}, {duration: animate_time, queue: false});

        //控制缩略图显示个数
        if (slideclick <= picnumber && slideclick >= 0) {
            if (slideclick <= 2) {
                $(".scrollpic ul").animate({"marginLeft": "0px"}, {duration: animate_time, queue: false});
            } else if (slideclick < (picnumber - 2)) {
                $(".scrollpic ul").animate({"marginLeft": (slideclick - 2) * smallSlideWidth}, {duration: animate_time, queue: false});
            }
        }

        //判断上下按钮是否可点击
        if (slideclick == 0) {
            $(".scrollbox #prev").addClass("disabled");
            $(".scrollbox #next").removeClass("disabled");
        } else if (slideclick == picnumber) {
            $(".scrollbox #prev").removeClass("disabled");
            $(".scrollbox #next").addClass("disabled");
        } else {
            $(".scrollbox #prev").removeClass("disabled");
            $(".scrollbox #next").removeClass("disabled");
        }
    });

    //点击向上按钮时
    $(".scrollbox #prev").click(function () {
        slideclick = slideclick - 1;
        if (slideclick < 0) {
            slideclick = 0;
        }
        $(".scrollpic li").eq(slideclick).trigger("click");
    });

    //点击向下按钮时
    $(".scrollbox #next").click(function () {
        slideclick = slideclick + 1;
        if (slideclick > picnumber) {
            slideclick = picnumber;
        }
        $(".scrollpic li").eq(slideclick).trigger("click");
    });

    $("#back_to_search").click(function () {
        var w = $("#book_info").width();
        $("#book_info").animate({ right: '-=' + w + 'px' }, 'slow', function () {
        });
    });
});

function lookInfo(isbn) {
    $.get("/bookdetail/" + isbn, {
        },
        function (ret) {
            $("#book_cover").attr("src", ret.cover);
            $("#book_author").html(ret.author);
            $("#book_press").html(ret.press);
            $("#book_price").html(ret.price);
            $("#book_isbn").html(ret.isbn);
            $("#book_description").html(ret.decription);
            $("#book_title").html(ret.title);
            var w = $("#book_info").width();
            $("#book_info").animate({ right: '+=' + w + 'px' }, 'slow', function () {
            });
        }
    );
}
