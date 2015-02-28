$(function () {
    var $typeSelect = $('select[name="type"]'),
        selectedType = $typeSelect.val(),
        initialTypeChange = !selectedType.length,
        $contentTypeSpecificForm = $('#content-type-specific-form');

    function changeType(newType) {
        selectedType = newType;

        $.ajax({
            type: 'GET',
            url: '/content/type/form',
            data: {
                type: selectedType
            },
            callback: function (response) {
                $contentTypeSpecificForm.html(response);
            }
        });
    }

    $typeSelect.on('change', function () {
        var value = $typeSelect.val();

        if (initialTypeChange && selectedType !== value) {
            initialTypeChange = false;
            changeType(value);
        } else if (value !== selectedType) {
            if (confirm('Czy jesteś pewien, że chcesz zmienić typ treści? ' +
                        'Dotychczasowe zmiany wprowadzone dla aktualnie wybranego typu zostaną utracone.')) {
                changeType(value);
            } else {
                $typeSelect.val(selectedType);
            }
        }
    });
});