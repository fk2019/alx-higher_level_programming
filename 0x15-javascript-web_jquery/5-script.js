$('#add_item').on('click', (event) => {
  const item = '<li>Item</li>';
  $('ul.my_list').append(item);
});
