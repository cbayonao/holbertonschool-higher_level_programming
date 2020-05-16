window.addEventListener('DOMContentLoaded', () => {
  $('INPUT#btn_translate').click( () => {
    const lang = $('INPUT#language_code').val();
    $.get('https://fourtonfish.com/hellosalut/?lang=' + lang, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
