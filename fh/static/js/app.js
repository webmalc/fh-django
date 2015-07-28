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

    //Collapsible Panel
    (function () {
        $(document).on('click', '.panel-heading span.clickable', function () {
            var $this = $(this);
            if (!$this.hasClass('panel-collapsed')) {
                $this.parents('.panel').find('.panel-body').slideUp();
                $this.addClass('panel-collapsed');
                $this.find('i').removeClass('glyphicon-chevron-up').addClass('glyphicon-chevron-down');
            } else {
                $this.parents('.panel').find('.panel-body').slideDown();
                $this.removeClass('panel-collapsed');
                $this.find('i').removeClass('glyphicon-chevron-down').addClass('glyphicon-chevron-up');
            }
        });
    }());
});