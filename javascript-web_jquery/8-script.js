$.get('https://swapi-api.hbtn.io/api/films/?format=json', (data, status) => {
    $.each(data.results, (index) => {
        $('#list_movies').append(`<LI>${data.results[index].title}</LI>`)
    })
})