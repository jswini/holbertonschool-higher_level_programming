$.get('https://fourtonfish.com/hellosalut/?lang=fr', function(item) {
  $('#hello').text(item.hello);
});
