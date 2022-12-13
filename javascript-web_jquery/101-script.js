$(document).ready(() => {
    $('#add_item').click(() => {
        $('.my_list').append('<li>item</li>')
    })
    
    $('#remove_item').click(() => {
        $('ul.my_list>li').last().remove('li')
    })
    
    $('#clear_list').click(() => {
        $('.my_list').empty()
    })
})