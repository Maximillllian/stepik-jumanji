let userMenu = document.querySelector('.user-menu');
let userMenuNav = document.querySelector('.user-menu nav');

function toggleMenu(event) {
    if (event.target.closest('.user-menu')) {
        console.log(event.target.closest('.user-menu'))
        userMenuNav.classList.toggle('active');
    } 
    if (!event.target.closest('.user-menu')) {
        console.log(event.target.closest('.user'))
        userMenuNav.classList.remove('active');
    }
}

document.addEventListener('click', toggleMenu);