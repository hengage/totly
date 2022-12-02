"use strict"

console.log('seen')
$(document).ready(() =>{
     /**
      Hides header on scroll down, show on scroll up
      */
    var iScrollPos = 0;
    $(window).scroll(() => {
        var iCurScrollPos = $(this).scrollTop();
        if (iCurScrollPos > iScrollPos) {
            $('header').fadeOut(500);
        } else {
            $('header').fadeIn(500);
        }
        iScrollPos = iCurScrollPos;
    });
})