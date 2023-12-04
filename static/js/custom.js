
  (function ($) {
  
  "use strict";

    // NAVBAR
    $('.navbar-nav .nav-link').click(function(){
        $(".navbar-collapse").collapse('hide');
    });

    // TEAMS CAROUSEL
    $('.teams-carousel').owlCarousel({
        center: true,
        loop: true,
        nav: true,
        dots: false,
        autoplay: true,
        autoplaySpeed: 300,
        smartSpeed: 500,
        responsive:{
          0:{
            items:1,
          },
          768:{
            items:2,
            margin: 100,
          },
          1280:{
            items:2,
            margin: 100,
          }
        }
    });

    // Banner Carousel
    var myCarousel = document.querySelector('#myCarousel')
    var carousel = new bootstrap.Carousel(myCarousel, {
      interval: 1500,
    })

    // TEAMS NAVIGATION
    function teamsNavResize(){
      $(".navbar").scrollspy({ offset: -94 });

      var teamsOwlItem = $('.teams-carousel .owl-item').width();

      $('.teams-carousel .owl-nav').css({'width' : (teamsOwlItem) + 'px'});
    }

    $(window).on("resize", teamsNavResize);
    $(document).on("ready", teamsNavResize);

    // HREF LINKS
    $('a[href*="#"]').click(function (event) {
      if (
        location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
        var target = $(this.hash);
        target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
        if (target.length) {
          event.preventDefault();
          $('html, body').animate({
            scrollTop: target.offset().top - 74
          }, 1000);
        }
      }
    });
    
  })(window.jQuery);
