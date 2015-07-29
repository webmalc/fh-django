/*jslint browser: true*/
/*global $*/
$(document).ready(function () {
    'use strict'

    //tagsinput
    $('input#id_tags').tagsinput({
        maxTags: 5,
        maxChars: 20,
        trimValue: true,
        freeInput: true,
        confirmKeys: [13, 188, 32],
        typeahead: {
            minLength: 1    ,
            afterSelect: function () {
                this.$element.val(null);
            },
            source: function (query) {
                return $.get('/finances/tags/' + query);
            }
        }
    });
});