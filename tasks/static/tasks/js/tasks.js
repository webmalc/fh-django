/*jslint browser: true*/
/*global $*/
$(document).ready(function () {
    'use strict';

    function formatPriority(state) {
        var classText = {
            1: 'text-green',
            2: 'text-aqua',
            3: '',
            4: 'text-yellow',
            5: 'text-red'
        };
        if (!state.id) {
            return state.text;
        }
        return $(
            '<span class="' + classText[state.id] + '">' + state.text + '</span>'
        );
    }

    $('#id_priority').select2({
        templateResult: formatPriority,
        templateSelection: formatPriority
    });
});