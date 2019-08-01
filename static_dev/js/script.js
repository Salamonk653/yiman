$(function(){

    $('.slider__inner, .news__slider-inner').slick({
      nextArrow: '<button type="button" class="slick-btn slick-next"></button>',
      prevArrow: '<button type="button" class="slick-btn slick-prev"></button>',
      infinite: false
    });
  
    $('select').styler();
  
    $('.header__btn-menu').on('click', function(){
      $('.menu ul').slideToggle();
    });
  
  });

  $(document).ready(function(){
    $("a.scrolllink").click(function (event) {
        console.log(event);

        event.preventDefault();
        $("html, body").animate({ scrollTop: $($(this).attr("href")).offset().top }, 2000);
    });
});