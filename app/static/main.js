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
    dots: true,
    responsiveClass: true,
    responsive: {
      0: {
        items: 2,
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

$(document).ready(function () {
  $(".owl-carousel-video").owlCarousel({
    loop: false,
    dots: true,
    autoWidth: true,
    responsiveClass: true,
    responsive: {
      0: {
        items: 2,
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

$(document).ready(function () {
  $(".owl-carousel-cast").owlCarousel({
    loop: false,
    dots: false,
    nav: true,
    autoWidth: true,
    responsiveClass: true,
    responsive: {
      0: {
        items: 2,
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

$(".message .close").on("click", function () {
  $(this).closest(".message").transition("fade");
});

$(".ui.sidebar").sidebar("attach events", ".toggle");
