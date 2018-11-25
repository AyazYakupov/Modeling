$('#reverse').on('click', function () {
    var n = $('input#N').val();
    if (n) {
        $.ajax({
            url: 'reverse',
            method: 'post',
            data: {'N': n}
        }).done(function (data) {
            $('.reverse').html('Корень по обратной интерполяции: ' + data['result'] + '\n Поиск по функции: ' + data['f'])
        })
    }
});
