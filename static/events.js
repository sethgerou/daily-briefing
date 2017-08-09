$(function() {

  $(document).on('click', '#weather_link', function (event) {
    event.preventDefault();
    $('#weather').html('<p class="loading">( loading weather... )</p>')
    $.ajax({
      url: '/weather',
      method: 'get'
    }).done(function (response) {
      $('#weather').html(response)
    })
  });

  $(document).on('click', '#forecast_link', function (event) {
    event.preventDefault();
    $('#forecast').html('<p class="loading">( loading forecast... )</p>')
    $.ajax({
      url: '/forecast',
      method: 'get'
    }).done(function (response) {
      $('#forecast').html(response)
    })
  });

  $(document).on('click', '#headlines_link', function (event) {
    event.preventDefault();
    $('#headlines').html('<p class="loading">( loading headlines... )</p>')
    $.ajax({
      url: '/headlines',
      method: 'get'
    }).done(function (response) {
      $('#headlines').html(response)
    })
  });

  if($('#weather').children()[0].textContent === '( loading weather... )') {
    $.ajax({
      async: "true",
      url: '/weather',
      method: 'get'
    }).done(function (response) {
      $('#weather').html(response)
    })
  }

  if($('#forecast').children()[0].textContent === '( loading forecast... )') {
    $.ajax({
      url: '/forecast',
      method: 'get'
    }).done(function (response) {
      $('#forecast').html(response)
    })
  }

  if($('#headlines').children()[0].textContent === '( loading headlines... )') {
    $.ajax({
      url: '/headlines',
      method: 'get'
    }).done(function (response) {
      $('#headlines').html(response)
    })
  }

});
