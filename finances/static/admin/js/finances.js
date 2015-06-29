/*global window, $, services, document, datepicker, deleteLink, Routing */
$(document).ready(function () {
    'use strict';

    // Tags input
    $('#id_tags').tagsinput({
      itemText: function(item) {
        return item.toLowerCase();
      }
    });
    $('#id_tags').change(function() {
        $(this).val($(this).val().toLowerCase());
    });
})