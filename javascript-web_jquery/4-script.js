$('#toggle_header').on('click', () => {
    if($('header').hasClass('green'))
        $('header').removeClass('green').addClass('red')
    else
        $('header').removeClass('red').addClass('green')
})