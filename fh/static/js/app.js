/*jslint browser: true*/
/*global $, Cookies*/
$(document).ready(function () {
    'use strict';

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
        var panel = $('.panel-collapsible'),
            cookie = Cookies.get(panel.attr('id')),
            hide = function (slide) {
                if (slide) {
                    panel.parents('.panel').find('.panel-body').slideUp();
                } else {
                    panel.parents('.panel').find('.panel-body').hide();
                }

                panel.addClass('panel-collapsed');
                panel.find('i').removeClass('glyphicon-chevron-up').addClass('glyphicon-chevron-down');
                Cookies.set(panel.attr('id'), 'collapsed', { expires: 7, path: '' });
            },
            show = function () {
                panel.parents('.panel').find('.panel-body').slideDown();
                panel.removeClass('panel-collapsed');
                panel.find('i').removeClass('glyphicon-chevron-down').addClass('glyphicon-chevron-up');
                Cookies.set(panel.attr('id'), 'open', { expires: 7, path: '' });
            };
        if (cookie === 'collapsed' || ($(window).width() <= 980 && cookie === undefined)) {
            hide(false);
        }
        panel.click(function () {
            if (panel.hasClass('panel-collapsed')) {
                show();
            } else {
                hide(true);
            }
        });
    }());

    //Bootstrap select
    $('select.form-control').selectpicker();

    //Datepickers & period select
    (function () {
        $('.datepicker').datepicker({
            format: "yyyy-mm-dd",
            autoclose: true,
            todayHighlight: true
        });

        var period = $('select#id_period'),
            begin = $('input#id_begin'),
            end = $('input#id_end'),
            select = function () {
                var dates = period.val();
                if (dates) {
                    dates = dates.split("_");
                    begin.datepicker('setDate', dates[0]);
                    end.datepicker('setDate', dates[1]);
                }
            },
            periodSet = function () {
                var val = begin.val() + '_' + end.val();
                period.val(val);
                period.selectpicker('refresh');
            };
        period.change(select);
        begin.change(periodSet);
        end.change(periodSet);
        select();
    }());
});