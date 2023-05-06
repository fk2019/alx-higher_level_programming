$(function () {
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  $.get(url, (data) => {
    const results = data.results;
    $.each(results, (i, obj) => {
      const li = $('<li>' + obj.title + '</li>');
      $('#list_movies').append(li);
    });
  });
});
