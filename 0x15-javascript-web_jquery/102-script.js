document.addEventListener('DOMContentLoaded', () => {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=';

  $('#btn_translate').on('click', (event) => {
    const code = $('#language_code').val();
    $.get(url + code, (data) => {
      $('#hello').text(data.hello);
    });
  });
});
