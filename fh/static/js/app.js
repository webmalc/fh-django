/*jslint browser: true*/
/*global $*/
$(document).ready(function () {
    'use strict'

    //bootstrap switch
    $('input[type="checkbox"]').bootstrapSwitch({
        size: 'small',
        onText: 'yes',
        offText: 'no'
    });

    //tooltip
    $('[data-toggle="tooltip"]').tooltip();
});