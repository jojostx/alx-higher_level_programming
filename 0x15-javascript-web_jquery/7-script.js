const $ = window.$;
const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$.getJSON(url, function (data) {
  $('div#character').text(data.name);
});
