$.ajax({
  url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
  success: (data, status) => { $('DIV#character').text(data.name); }
});
