$(function () {
    $.ajaxSetup({
        beforeSend: function () {
            this.data += '&_xsrf=' + $('input[name="_xsrf"]').val();
        }
    });


    $(document).on('click', function (e) {
        // If not clicked in user area then close user popover.
        if (!$(e.target).closest('.user').length) {
            $('.user').removeClass('popover-open');
            $('.user-popover').hide();
        }
    });

    $('.user').on('click', function () {
        $('.user').toggleClass('popover-open');
        $('.user-popover').toggle();
    });
});