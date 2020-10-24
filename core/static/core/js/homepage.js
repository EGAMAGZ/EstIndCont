const scroll_arrow_element = document.getElementById('scroll-arrow');
const page_welcome = document.getElementById('page-welcome');
const page_container = document.getElementById('page-container');
const show_button = document.getElementById('showWelcome')

const hide_page_container = ()=>{
    if(page_container.classList.contains('hide')){
        page_container.classList.remove('hide');
        page_container.classList.add('show');
    }
    else{
        page_container.classList.remove('show')
        page_container.classList.add('hide');
    }
}

scroll_arrow_element.addEventListener('click', ()=>{
    hide_page_container();
});

show_button.addEventListener('click', () => hide_page_container())
