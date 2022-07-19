let slides = document.getElementById("imgSlide");
let image = new Array(`{% static 'Images/background1.jpg' %}`,
    `{% static 'Images/background2.jpg' %}`,
    `{% static 'Images/background3.jpg' %}`
)
let flag = 0;
function slideshow() {
    if (flag > image.length - 1) {
        flag = 0;
    }
    slides.src = image[flag];
    flag++;
    setTimeout('slideshow()', 3000)
}