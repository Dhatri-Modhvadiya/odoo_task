// my_custom_module/static/src/js/my_custom_script.js

odoo.define('office_employee_management.department', function (require) {
    "use strict";

    var publicWidget = require('web.public.widget');

    publicWidget.registry.MyCustomWidget = publicWidget.Widget.extend({
        selector: '#my_button', // The button ID

        events: {
            'click': '_onClickButton'
        },

        /**
         * @private
         */
        _onClickButton: function (event) {
            event.preventDefault();
            alert('Button was clicked!');
        },
    });

    publicWidget.registry.MyCustomWidget.include({
        start: function () {
            this._super.apply(this, arguments);
            console.log('MyCustomWidget loaded');
        },
    });
});
