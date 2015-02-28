$(function () {
    // @TODO: change styles (move to CSS), add close button
    function handleAjaxError(message) {
        var $errorMessage = $('<div>', {
            style: 'position: fixed; top: 0; left: 0; width: 100%; right: 100%; height: 50px; line-height: 50px; ' +
            'text-align: center; background-color: rgba(255, 0, 0, 0.7); font-weight: bold;',
            text: message && message.length ?
                message : 'Błąd podczas komunikacji z serwerem. Przepraszamy za utrudnienia i prosimy spróbować ponownie.'
        });

        $('body').append($errorMessage);

        setTimeout(function () {
            $errorMessage.remove();
        }, 10000);
    }

    $.ajaxSetup({
        beforeSend: function () {
            this.data += '&_xsrf=' + $('input[name="_xsrf"]').val();
        },
        success: function (response, status, xhr) {
            if (Object.prototype.toString.call(response) === '[object Object]') {
                if (response.hasOwnProperty('status') && response.status === 'error') {
                    return handleAjaxError(response.hasOwnProperty('message') ? response.message : null);
                }
            }

            if (this.hasOwnProperty('callback')) {
                this.callback(response);
            }
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