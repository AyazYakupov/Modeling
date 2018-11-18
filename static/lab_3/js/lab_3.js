$(document).ready(function () {
    $('#form1').submit(function (event) {
        event.preventDefault();
        $('#loader').removeClass('d-none');
        $('#loader').addClass('d-flex');
        $.ajax({
            url: 'get_answer',
            method: 'POST',
            data: $('#form1').serialize(),
            success: function (data) {
                $('#answer').html('X = ' + data['result']);
                $('#loader').removeClass('d-flex');
                $('#loader').addClass('d-none');
            }
        })
    })
});
