$.ajax({
  url: 'https://fourtonfish.com/hellosalut/?lang=fr',
  success: (data, status) => { $('#hello').text(data.hello); }
});
