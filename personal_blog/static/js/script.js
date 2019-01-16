$(document).ready(function () {
    const $hamburger = $(".hamburger");
    const $mainHomePageDiv = $(".fade-in");
    navToggle();

    //hamburger
    $hamburger.click(function () {
        $(this).toggleClass("is-active");

    });

    //fade-in
    $mainHomePageDiv.show().animate({opacity: 1, top: 0}, 1400);
});

function navToggle() {
    const $nav = $("nav");
    const $main = $("#main");
    const $menu = $(".menuitems");
    const $links = $(".portfolio-links");

    //to close
    if ($nav.height() > 50) {
        $nav.height(50);
        $main.css("marginTop", "50px");

        $menu.each(function (index) {
                $(this).css({
                    opacity: "0.0",
                    marginTop: "100px"
                });
            }
        );
        $links.css("marginTop", "40%");
    } else {
        $nav.height(300);
        $main.css("marginTop", "300px");
        $menu.each(function (index) {
                $(this).css({
                    opacity: "1.0",
                    marginTop: "0px"
                });
            }
        );
        $links.css("marginTop", "25%");
    }
}
