/*jslint browser: true*/
/*global $*/
$(document).ready(function () {
    'use strict';
    $('.admin-filter-select').change(function () {
        window.location = window.location.pathname + this.options[this.selectedIndex].value;
    });

    $('#id_tags').on('change, keydown, focus, blur', function () {
        $(this).val($(this).val().toLowerCase());
    });
});