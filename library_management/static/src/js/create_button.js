/** @odoo-module **/
//import { _t } from "@web/core/l10n/translation";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { Component } from "@odoo/owl";
//import { usePos } from "@point_of_sale/app/store/pos_hook";
//import { CustomAlertPopup } from "@pos_buttons/js/PopUp/pos_pop_up";
export class CreateButton extends Component {

static template = "point_of_sale.CreateButton";

/**
* Setup function to initialize the component.

*/

setup() {
//this.pos = usePos();
//
//this.popup = useService("popup");

}

/**
* Click event handler for the create button.

*/

async custom() {
  console.log("Clicked.......")
}

}

ProductScreen.addControlButton({
    component: CreateButton,
    condition: function () {
        return true;
    },
});