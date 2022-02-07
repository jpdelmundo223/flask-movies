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
  $(".owl-carousel-showcase").owlCarousel({
    loop: false,
    margin: 10,
    innerWidth: 120,
    lazyLoad: true,
    items: 1,
  });
});

$(document).ready(function () {
  $(".owl-carousel-trending").owlCarousel({
    loop: false,
    margin: 10,
    dots: false,
    responsiveClass: true,
    responsive: {
      0: {
        items: 1,
      },
      600: {
        items: 3,
      },
      1000: {
        items: 6,
        loop: false,
      },
    },
  });
});
