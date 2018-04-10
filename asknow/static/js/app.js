$(function () {
    $('.navbar-burger').each(function () {
      $(this).click(function () {
        var target = $(this).data("target");
        console.log(target);
        $(this).toggleClass('is-active');
        $('#' + target).toggleClass('is-active');
      });
    });
});
