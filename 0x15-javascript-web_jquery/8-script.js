const $ = window.$;
const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.getJSON(url, function (data) {
  const moviesUl = $('ul#list_movies');
  data.results.forEach(film => moviesUl.append(`<li>${film.title}</li>`));
});
