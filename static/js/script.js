var typed = new Typed('.element', {

      strings: ['Web Developer ','Data Scientist '],
      typeSpeed: 60,

    });
 
    document.getElementById("btn btn2").addEventListener("click", () => {
  window.location.href = "/download-cv";
});
document.addEventListener('DOMContentLoaded', () => {
    setTimeout(() => {
        const flashMessages = document.querySelectorAll('.flash-message');
        flashMessages.forEach(msg => {
            msg.style.opacity = '0';
            setTimeout(() => msg.remove(), 500);
        });
    }, 3000);
});
