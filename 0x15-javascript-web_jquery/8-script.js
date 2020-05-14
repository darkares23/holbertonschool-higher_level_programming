$.ajax({
  url: 'https://swapi-api.hbtn.io/api/films/?format=json',
  success: (data, status) => {
    data.results.forEach(movie => {
      $('#list_movies').append(`<li>${movie.title}</li>`);
    });
  }
});
