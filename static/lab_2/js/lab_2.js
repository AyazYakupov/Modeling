$(document).ready(function () {
    $('#create_table').on('click', function () {
        if ($('input#points').val()) {
            $.ajax({
                url: 'create_table',
                method: 'POST',
                data: {'points': $('input#points').val()},
                success: function (data) {
                    window.location.href = './'
                }
            })
        } else {
            alert('Введите количество точек!')
        }
    });
    $('#show_plot').on('click', function () {
        if ($('input#degree').val()) {
            var objs = '';
            $('#data tr').each(function () {
                var input = $(this).find('input').val();
                objs += input + ' ';
            });
            $.ajax({
                url: 'polyfit',
                method: 'POST',
                data: {'degree': $('input#degree').val(), 'weight': objs},
                success: function (data) {
                    $('img#plot_image').attr('src', '/static/lab_2/images/plot.png' + '?' + Math.random());
                    $('img#plot_image').addClass('d-block')
                }
            })
        } else {
            alert('Введите степень полинома')
        }
    })
});
