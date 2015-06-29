/*global window, $, services, document, datepicker, deleteLink, Routing */
$(document).ready(function () {
    'use strict';

    $('#id_tags').on('change, keydown, focus, blur', function () {
        $(this).val($(this).val().toLowerCase());
    });
})