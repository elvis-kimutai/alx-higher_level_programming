// displays the value of hello from that fetch in the HTML tag
$.get('https://fourtonfish.com/hellosalut/?lang=fr',
  function (data) {
    $('DIV#hello').text(data.hello);
  });
