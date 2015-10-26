/*jslint browser: true*/
/*global $, Cookies*/
$(document).ready(function () {
    'use strict';

    (function () {
        var inputs = $("#avatar-choose-form input[type='radio']"),
            images = $("#avatar-choose-form img"),
            select = function () {
                images.removeClass('avatar-selected');
                $("#avatar-choose-form input:checked").next('img').addClass('avatar-selected');
            };
        images.addClass('img-rounded')
        select();
        inputs.change(select);
    }());
});