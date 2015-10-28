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

    //tabs remember
    $(function () {
        $('a[data-toggle="tab"]').on('shown.bs.tab', function () {
            localStorage.setItem('last_tab', $(this).attr('href'));
        });
        var lastTab = localStorage.getItem('last_tab');
        if (lastTab) {
            $('[href="' + lastTab + '"]').tab('show');
        }
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

    //sidebar
    (function () {
        if ($(window).width() <= 1100) {
            localStorage.setItem('sidebar-collapse', 1);
            $('body').addClass('sidebar-collapse');
        }

        $('.sidebar-toggle').click(function () {
            if ($('body').hasClass('sidebar-collapse')) {
                localStorage.removeItem('sidebar-collapse');
            } else {
                localStorage.setItem('sidebar-collapse', 1);
            }
        });
    }());

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

    //Box widget
    (function () {
        var links = $('.form-group-collapse');

        links.each(function () {
            if (localStorage.getItem($(this).prop('id'))) {
                var box = $(this).closest('.box'),
                    boxBody = box.find('.box-body'),
                    icon = $(this).find('i');

                box.addClass('collapsed-box');
                boxBody.hide();
                icon.removeClass('fa-minus').addClass('fa-plus');
            }
        });
        links.click(function () {
            if ($(this).closest('.box').find('.box-body').is(':visible')) {
                localStorage.setItem($(this).prop('id'), 1);
            } else {
                localStorage.removeItem($(this).prop('id'));
            }
        });
    }());
});