$.ajaxSetup({
    data: {csrfmiddlewaretoken: '{{ csrf_token }}' },
    timeout: 5000,
});
$(document).ready(function () {
    $(".btn-modal").on('click', function () {
        $('.modal-list').removeClass('mask-hidden');
        $(document.body).css('');
    })
    $(".mask-modal").on('click', function () {
        $('.modal-list').addClass('mask-hidden');
    })
    $(".search-form input").bind('keypress', function (event) {
        if(event.keyCode == "13") {
            searchbtn();
        }
    });
    // $('#users-btn').on('click', function () {
    //
    // })
    // $('.users-sign .input-group input').addClass('form-control');
    // $(".search-btn").click(function () {
    //     $.get("{% url 'search' %}", function (data) {
    //         $(".results").append(data.book_name)
    //     })
    // })
});

$(function () {
    $('.dropDown ul>li:even').addClass('alt');
    $('.dropDown ul>li:even a').css('color','#00c59e');
    $('.dropDown .dropBtn').click(function () {
        $('.dropDown ul').slideToggle('fast');
    });
})

// $(function () {
//     $('.login-nav a').click(function() {
//         $('.login-nav a').removeClass("active");
//         $(this).addClass("active");
//     });
// })

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function searchbtn(){
    var kw = $(".search-kw").val();
    if (kw == "") {
        $(".search-form input").text("不能为空")
    }else {
        $(".novel_horizontal").html(
            '<i class="fa fa-spinner fa-spin fa-4x fa-fw"></i>'
        )
        $.ajax({
        url:"/all/",
        type:"get",
        data:{search: kw},
        success:function (res) {
            var str = "";
            if (res.content.length == 0){
                str = "对不起没有该内容，请重新输入关键词"
            }
            else{
                $.each(res.content,function (index, obj) {
                    str += '<div class="border-set">';
                    str += '<ul class="container">';
                    str += '<li class="novel_horizontal">';
                    str += '<div class="image">';
                    str += '<a href='+obj.book_identify+'"/apps/novel/info/">';
                    str += '<img class="img-responsive lazy" data-original="';
                    str += obj.book_image;
                    str += '" alt=""></a>';
                    str += '</div>';
                    str += '<div class="bk_info">';
                    str += '<div>';
                    str += '<a href=""><span>'+obj.book_name+'</span></a>';
                    str += '</div>';
                    str += '<div>';
                    str += '<a href="">';
                    str += '<span>'+obj.book_author+'</span>';
                    str += '<span> |</span>';
                    str += '</a>';
                    str += '<a href=""><span>'+obj.book_category+'</span></a>';
                    str += '</div>';
                    str += '<p>最新：'+obj.book_latest+'</p>';
                    str += '<p>简介：'+obj.book_desc+'</p>';
                    str += '</div>';
                    str += '</li>';
                    str += '</ul>';
                    str += '</div>';
                })
            }
            $(".novel_horizontal").html(str)
            $(".lazy").lazyload();
        },
        error:function (XMLhttpRequest, extStatus, errorThrown) {
            $(".novel_horizontal").html(
            "请求出错，请稍后再试"
        )
        }
    });
    }
}

function collectbtn() {
    var id=$('.top_right input').val();
    var is_collect=$('.novel-collect-btn').attr('is_collect');
    if (is_collect == 'True'){
        $.get("/users/collect/", {'novel_identify':id, 'is_collect': is_collect}, function (data) {
            $('.novel-collect-btn')
                .text("加入书架")
                .attr('is_collect','False')
                .parent()
                .css({'background-color':'#00c59e', 'border-color': '#00c59e'});
        })
    }else {
        $.get("/users/collect/",
            {'novel_identify':id, 'is_collect': is_collect},
            function (data) {
                if (data == '200 ok') {
                    $('.novel-collect-btn').text("取消收藏").attr('is_collect','True')
                    .parent()
                    .css({'background-color':'#999', 'border-color': '#999'});
                }
        })
    }
}

/*! Lazy Load 1.9.7 - MIT license - Copyright 2010-2015 Mika Tuupola */
!function(a,b,c,d){var e=a(b);a.fn.lazyload=function(f){function g(){var b=0;i.each(function(){var c=a(this);if(!j.skip_invisible||c.is(":visible"))if(a.abovethetop(this,j)||a.leftofbegin(this,j));else if(a.belowthefold(this,j)||a.rightoffold(this,j)){if(++b>j.failure_limit)return!1}else c.trigger("appear"),b=0})}var h,i=this,j={threshold:0,failure_limit:0,event:"scroll",effect:"show",container:b,data_attribute:"original",skip_invisible:!1,appear:null,load:null,placeholder:"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAANSURBVBhXYzh8+PB/AAffA0nNPuCLAAAAAElFTkSuQmCC"};return f&&(d!==f.failurelimit&&(f.failure_limit=f.failurelimit,delete f.failurelimit),d!==f.effectspeed&&(f.effect_speed=f.effectspeed,delete f.effectspeed),a.extend(j,f)),h=j.container===d||j.container===b?e:a(j.container),0===j.event.indexOf("scroll")&&h.bind(j.event,function(){return g()}),this.each(function(){var b=this,c=a(b);b.loaded=!1,(c.attr("src")===d||c.attr("src")===!1)&&c.is("img")&&c.attr("src",j.placeholder),c.one("appear",function(){if(!this.loaded){if(j.appear){var d=i.length;j.appear.call(b,d,j)}a("<img />").bind("load",function(){var d=c.attr("data-"+j.data_attribute);c.hide(),c.is("img")?c.attr("src",d):c.css("background-image","url('"+d+"')"),c[j.effect](j.effect_speed),b.loaded=!0;var e=a.grep(i,function(a){return!a.loaded});if(i=a(e),j.load){var f=i.length;j.load.call(b,f,j)}}).attr("src",c.attr("data-"+j.data_attribute))}}),0!==j.event.indexOf("scroll")&&c.bind(j.event,function(){b.loaded||c.trigger("appear")})}),e.bind("resize",function(){g()}),/(?:iphone|ipod|ipad).*os 5/gi.test(navigator.appVersion)&&e.bind("pageshow",function(b){b.originalEvent&&b.originalEvent.persisted&&i.each(function(){a(this).trigger("appear")})}),a(c).ready(function(){g()}),this},a.belowthefold=function(c,f){var g;return g=f.container===d||f.container===b?(b.innerHeight?b.innerHeight:e.height())+e.scrollTop():a(f.container).offset().top+a(f.container).height(),g<=a(c).offset().top-f.threshold},a.rightoffold=function(c,f){var g;return g=f.container===d||f.container===b?e.width()+e.scrollLeft():a(f.container).offset().left+a(f.container).width(),g<=a(c).offset().left-f.threshold},a.abovethetop=function(c,f){var g;return g=f.container===d||f.container===b?e.scrollTop():a(f.container).offset().top,g>=a(c).offset().top+f.threshold+a(c).height()},a.leftofbegin=function(c,f){var g;return g=f.container===d||f.container===b?e.scrollLeft():a(f.container).offset().left,g>=a(c).offset().left+f.threshold+a(c).width()},a.inviewport=function(b,c){return!(a.rightoffold(b,c)||a.leftofbegin(b,c)||a.belowthefold(b,c)||a.abovethetop(b,c))},a.extend(a.expr[":"],{"below-the-fold":function(b){return a.belowthefold(b,{threshold:0})},"above-the-top":function(b){return!a.belowthefold(b,{threshold:0})},"right-of-screen":function(b){return a.rightoffold(b,{threshold:0})},"left-of-screen":function(b){return!a.rightoffold(b,{threshold:0})},"in-viewport":function(b){return a.inviewport(b,{threshold:0})},"above-the-fold":function(b){return!a.belowthefold(b,{threshold:0})},"right-of-fold":function(b){return a.rightoffold(b,{threshold:0})},"left-of-fold":function(b){return!a.rightoffold(b,{threshold:0})}})}(jQuery,window,document);