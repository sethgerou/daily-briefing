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

  $(document).on('click', '#CNN_link', function (event) {
    event.preventDefault();
    $('#CNN').html('<p class="loading">( loading CNN... )</p>')
    $.ajax({
      url: '/headlines/CNN',
      method: 'get'
    }).done(function (response) {
      $('#CNN').html(response)
    })
  });

  $(document).on('click', '#ENG_link', function (event) {
    event.preventDefault();
    $('#ENG').html('<p class="loading">( loading engadget... )</p>')
    $.ajax({
      url: '/headlines/engadget',
      method: 'get'
    }).done(function (response) {
      $('#ENG').html(response)
    })
  });

  $(document).on('click', '#NYT_link', function (event) {
    event.preventDefault();
    $('#NYT').html('<p class="loading">( loading New York Times... )</p>')
    $.ajax({
      url: '/headlines/the-new-york-times',
      method: 'get'
    }).done(function (response) {
      $('#NYT').html(response)
    })
  });

  $(document).on('click', '#WSJ_link', function (event) {
    event.preventDefault();
    $('#WSJ').html('<p class="loading">(loading Wall Street Journal... )</p>')
    $.ajax({
      url: '/headlines/the-wall-street-journal',
      method: 'get'
    }).done(function (response) {
      $('#WSJ').html(response)
    })
  });

  $(document).on('click', '#about_link', function (event) {
    event.preventDefault();
    $.ajax({
      url: '/about',
      method: 'get'
    }).done(function (response) {
      $('#about').html(response)
    })
  });

  if($('#weather').children()[0].textContent === '( loading weather... )') {
    $.ajax({
      async: "true",
      url: '/weather',
      method: 'get'
    }).done(function (response) {
      $('#weather').html(response);
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

  if($('#CNN').children()[0].textContent === '( loading CNN... )') {
    $.ajax({
      url: '/headlines/CNN',
      method: 'get'
    }).done(function (response) {
      $('#CNN').html(response)
    })
  }

  if($('#ENG').children()[0].textContent === '( loading engadget... )') {
    $.ajax({
      url: '/headlines/engadget',
      method: 'get'
    }).done(function (response) {
      $('#ENG').html(response)
    })
  }

  if($('#NYT').children()[0].textContent === '( loading New York Times... )') {
    $.ajax({
      url: '/headlines/the-new-york-times',
      method: 'get'
    }).done(function (response) {
      $('#NYT').html(response)
    })
  }

  if($('#WSJ').children()[0].textContent === '(loading Wall Street Journal... )') {
    $.ajax({
      url: '/headlines/the-wall-street-journal',
      method: 'get'
    }).done(function (response) {
      $('#WSJ').html(response)
    })
  }

});
