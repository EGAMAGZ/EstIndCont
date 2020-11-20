const menu_button = document.getElementById('menuToogle');
const close_nav_button = document.getElementById('closeNav');
const scroll_arrow_element = document.getElementById('scroll-arrow');
const page_welcome = document.getElementById('page-welcome');
const page_container = document.getElementById('page-container');
const show_button = document.getElementById('showWelcome');
const side_bar = document.getElementById("sideBar");

const display_page_container = () => {
    if (page_container.classList.contains('hide')) {
        page_container.classList.remove('hide');
        page_container.classList.add('show');
    }
    else {
        page_container.classList.remove('show');
        page_container.classList.add('hide');
        hide_sidenav();
    }
}

const show_sidenav = () => {
    if (side_bar.classList.contains('sidenav-hide')) {
        side_bar.classList.remove('sidenav-hide');
        side_bar.classList.add('sidenav-show');
    }
}

const hide_sidenav = () => {
    if (side_bar.classList.contains('sidenav-show')) {
        side_bar.classList.remove('sidenav-show');
        side_bar.classList.add('sidenav-hide');
    }
}

scroll_arrow_element.addEventListener('click', () => display_page_container());

show_button.addEventListener('click', () => display_page_container());

close_nav_button.addEventListener('click', () => hide_sidenav());

menu_button.addEventListener('click', () => show_sidenav());
