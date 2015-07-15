/*jslint browser: true*/
/*global $*/
$(document).ready(function () {
    'use strict'

    //tagsinput
    $('#id_tags').tagsinput({
        maxTags: 5,
        maxChars: 20,
        trimValue: true,
        freeInput: true,
        typeahead: {
            minLength: 2,
            afterSelect: function () {
                this.$element.val(null);
            },
            source: function (query) {
                return $.get('/finances/tags/' + query);
            }
        }
    });
});