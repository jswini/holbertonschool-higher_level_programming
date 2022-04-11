$.get('https://swapi-api.hbtn.io/api/films/?format=json', function(data) {
  const title = data.results;
  for (const film in title) {
    $('#list_movies').append('<li>' + title[film].title + '</li>');
  }
});
