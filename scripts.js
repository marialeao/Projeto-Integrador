$(document).ready(function () {
    $('a.scrollSuave').on('click', function (e) {
        e.preventDefault();
        $('#togglemenu').collapse('hide');
        var id = $(this).attr('href').replace('/', ''),
            targetOffset = $(id).offset().top;

        $('html, body').animate({
            scrollTop: targetOffset - 50
        }, 500);
    });

    var stickyOffset = $('header').height();

    $(window).scroll(function () {
        var sticky = $('body'),
            scroll = $(window).scrollTop();
        if (scroll >= stickyOffset) sticky.addClass('sticky-top');
        else sticky.removeClass('sticky-top');
    });
});