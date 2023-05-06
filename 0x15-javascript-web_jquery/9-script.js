document.addEventListener('DOMContentLoaded', () => {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  $.get(url, (data) => {
    $('#hello').text(data.hello);
  });
});
