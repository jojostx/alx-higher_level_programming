const $ = window.$;
$('div#add_item').on('click', function (e) {
  $('ul.my_list').append('<li>Item</li>');
});
