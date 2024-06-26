/ @odoo-module /

import {WebsiteSale} from "@website_sale/js/website_sale";

WebsiteSale.include({
    events: Object.assign({}, WebsiteSale.prototype.events, {
        "change select[name='state_id']": "_onChangeState",
        "change select[name='city_id']": "_onChangeCity",
    }),
    start: function () {
        this.autoStreetTwo = document.querySelector(".div_street2");

        return this._super.apply(this, arguments);
    },
    _onChangeState: function () {
        console.log("Hi")
        this.autoStreetTwo.querySelectorAll("input").forEach((input) => {
                                input.value = "HI Dhatri";
                            });
    },
});