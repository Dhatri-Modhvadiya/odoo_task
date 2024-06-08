odoo.define('library_management.custom_widget', ['require', 'web.public.widget', 'library_management.custom_classes'], function (require) {
    'use strict';

    var publicWidget = require('web.public.widget');
    var CustomClasses = require('library_management.custom_classes');
    var ClassB = CustomClasses.ClassB;

    publicWidget.registry.CustomWidget = publicWidget.Widget.extend({
        selector: '.custom_widget_selector',
        start: function () {
            this._super.apply(this, arguments);

            var instanceB = new ClassB();
            instanceB.method1();
            instanceB.method2();
            instanceB.method3();
        },
    });

    return publicWidget.registry.CustomWidget;
});


















//odoo.define('library_management.custom_widget',[], function (require) {
//    'use strict';
//
//    // Import dependencies
//    var publicWidget = require('web.public.widget');
//    var CustomClasses = require('library_management.custom_classes');
//    var ClassB = CustomClasses.ClassB;
//
//    // Define your module
//    return publicWidget.registry.CustomWidget = publicWidget.Widget.extend({
//        selector: '.custom_widget_selector',
//        start: function () {
//            this._super.apply(this, arguments);
//
//            // Use the imported classes or methods
//            var instanceB = new ClassB();
//            instanceB.method1();
//            instanceB.method2();
//            instanceB.method3();
//        },
//    });
//});
//
//
//
//
//















//// static/src/js/custom_widget.js
//
//odoo.define('library_management.custom_widget', function (require) {
//    'use strict';
//
//    const publicWidget = require('web.public.widget');
//    var CustomClasses = require('library_management.custom_classes');
//    var ClassB = CustomClasses.ClassB;
//
//    publicWidget.registry.CustomWidget = publicWidget.Widget.extend({
//        selector: '.custom_widget_selector',
//
//        start: function () {
//            this._super.apply(this, arguments);
//
//            // Create an instance of Class B and call its methods
//            var instanceB = new ClassB();
//            instanceB.method1(); // Inherited from Class A
//            instanceB.method2(); // Inherited from Class A
//            instanceB.method3(); // Defined in Class B
//        },
//    });
//});
