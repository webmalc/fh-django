/*jslint browser: true*/
/*global $, Cookies*/
$(document).ready(function () {
    'use strict';

    //bootstrap-wysihtml5
    $('textarea').wysihtml5({toolbar: {
        "fa": true
    }});

    //bootstrap switch
    $('input[type="checkbox"]').not('#avatar-delete-form input').bootstrapSwitch({
        size: 'small',
        onText: 'yes',
        offText: 'no'
    });

    //tagsinput
    (function () {

        $('input#id_tags').tagsinput({
            maxTags: 5,
            maxChars: 20,
            trimValue: true,
            freeInput: true,
            confirmKeys: [13, 188, 32],
            typeahead: {
                minLength: 1,
                afterSelect: function () {
                    this.$element.val(null);
                },
                source: function (query) {
                    return $.get('/tags/' + query);
                }
            }
        });
        $('div.bootstrap-tagsinput > input').keyup(function () {
            $(this).val($(this).val().toLowerCase());
        });
    }());

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

    //select2
    $('select.form-control').not('.not-select2').select2();

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
        $('.datetimepicker').datetimepicker({
            format: "YYYY-MM-DD HH:ss"
        });

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