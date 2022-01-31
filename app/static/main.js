$(".special.cards .image").dimmer({
  on: "hover",
});

$(document).ready(function () {
  $(".ui.menu .ui.dropdown").dropdown({
    on: "hover",
  });
  $(".ui.menu a.item").on("click", function () {
    $(this).addClass("active").siblings().removeClass("active");
  });
});

$(document).ready(function () {
  $(".owl-carousel").owlCarousel({
    loop: false,
    margin: 10,
    nav: true,
    innerWidth: 120,
    dots: true,
    lazyLoad: true,
    items: 1,
  });
});
