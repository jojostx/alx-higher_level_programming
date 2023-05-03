window.addEventListener('DOMContentLoaded', function () {
  const $ = window.$;
  const ul = $('ul.my_list');

  $('div#add_item').on('click', function () {
    ul.append('<li>item</li>');
  });

  $('div#remove_item').on('click', function () {
    $('ul.my_list li:last-child').remove();
  });

  $('div#clear_list').on('click', function () {
    ul.empty();
  });
});
