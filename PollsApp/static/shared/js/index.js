function resizeHeightContent(selector) {
    const remainHeight = $(window).innerHeight() - $('#top-navbar').height();
    $(selector).height(remainHeight);
}

window.addEventListener('DOMContentLoaded', () => resizeHeightContent('#wrapper-content'));
$(window).resize(() => resizeHeightContent('#wrapper-content'));

$('#toggle-sidebar').on('click', () => $('aside:first').toggleClass('show'));
