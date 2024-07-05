const toggleMenu = document.querySelector('.toggle-menu');
const menu = document.querySelector('.navbar');
const header = document.querySelector('.navbar');

toggleMenu.addEventListener('click', () => {
  menu.classList.toggle('active');
  if (menu.classList.contains('active')) {
    header.classList.remove('fixed');
  } else {
    if (window.scrollY > 500) {
      header.classList.add('fixed');
    }
  }
});


window.addEventListener('scroll', function() {
  if (!menu.classList.contains('active')) {
    if (window.scrollY > 500) {
      header.classList.add('fixed');
    } else {
      header.classList.remove('fixed');
    }
  }
});
