document.addEventListener('DOMContentLoaded', () => {
  const li = '<li>Item</li>';
  $('#add_item').on('click', (event) => {
    $('ul.my_list').append(li);
  });
  $('#remove_item').on('click', (event) => {
    $('ul.my_list li').last().remove();
  });
  $('#clear_list').on('click', (event) => {
    $('ul.my_list').empty();
  });
});
