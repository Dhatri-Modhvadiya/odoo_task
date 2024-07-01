/** @odoo-module **/

import { _t } from "@web/core/l10n/translation";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { useService } from "@web/core/utils/hooks";
import { TextAreaPopup } from "@point_of_sale/app/utils/input_popups/textarea_popup";
import { Component } from "@odoo/owl";
import { usePos } from "@point_of_sale/app/store/pos_hook";

export class MyOrderlineDiscount extends Component {
    static template = "point_of_sale.MyOrderlineDiscount";

    setup() {
        this.pos = usePos();
        this.popup = useService("popup")
        this.orm = useService("orm");
    }
    async onClickDiscountDefault(){
        const Orderlines = this.pos.get_order().get_orderlines();
        const result = await this.orm.call('pos.order', 'get_discount', ['true']);
         for (let orderLine of Orderlines){
            orderLine.set_discount(result);
           }
    }

//
//          if (confirmed) {
//                if (values){
//                    if (values < 100 && values >= 0) {
//                        for (const orderline of orderLines) {
//                            orderline.set_discount(values);
//                        }
//                        status = false;
//                    } else {
//                        await this.popup.add(ErrorPopup, {
//                            title: _t("Invalid Discount"),
//                            body: _t("You can't add a discount of %s%. Please enter a value between 0% and 100%.", values),
//                            cancelKey: true,
//                        });
//                    }
//
//                }else{
//                    await this.popup.add(ErrorPopup, {
//                        title: _t("Invalid input"),
//                        body: _t("You can't add a discount because you enter incorrect data."),
//                        cancelKey: true,
//                    });
//                }
//            }else{
//                break;
//            }

//        if (confirmed) {
//            for (var orderline of selectedOrders){
//                orderline.set_discount(inputNote)
//            }
//        }
//    }
}

ProductScreen.addControlButton({
    component: MyOrderlineDiscount,
});
