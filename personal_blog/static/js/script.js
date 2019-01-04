$( document ).ready(function() {

  window.onscroll = function() {
    // removeFixed();
  };

  const bodyRow = $("#home-body .row");
  const leftSideDiv = $("#home-body .left-side");
  const lastImgDiv = $("#home-body .content-block:last-of-type");
  const footer = $("footer");

  let offset = footer.offset().top;

  // function removeFixed() {
  //   if (window.pageYOffset >= offset) {
  //     leftSideDiv.css("position", "initial");
  //     leftSideDiv.fadeOut();
  //   }
  //   else {
  //     leftSideDiv.css("position", "fixed");
  //     leftSideDiv.fadeIn();
  //   }
  // }
});
