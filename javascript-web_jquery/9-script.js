$.get('https://stefanbohacek.com/hellosalut/?lang=fr', (data) => {
    $('#hello').text(data.hello)
})