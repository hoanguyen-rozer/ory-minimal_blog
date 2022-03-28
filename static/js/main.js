$("button.bar-menu").on('click', function () {
    $(".canvas-menu").toggleClass('open');
})

$(".btn-close").on('click', function () {
    $(".canvas-menu").removeClass("open");
})