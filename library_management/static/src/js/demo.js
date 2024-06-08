/* @odoo-module */
import publicWidget from "@web/legacy/js/public/public_widget";

export const MySalePortal = publicWidget.Widget.extend({

    selector: '.o_portal_details',
    init(){
        this._super(...arguments)
        console.log("hello nnudfh")
    },
    /**
     *
     * @override
     */
    start: function () {
        var def = this._super.apply(this, arguments);
        console.log("gregreegtryetre")
        return def;
    },
});
