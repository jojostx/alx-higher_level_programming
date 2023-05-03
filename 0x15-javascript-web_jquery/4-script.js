const $ = window.$;
$('div#toggle_header').on('click', function (e) {
  $('header').toggleClass('red');
  $('header').toggleClass('green');
});
