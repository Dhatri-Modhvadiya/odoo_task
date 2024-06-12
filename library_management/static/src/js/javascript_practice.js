/* @odoo-module */
import { FormController } from "@web/views/form/form_controller";
import { formView } from "@web/views/form/form_view";
import { registry } from "@web/core/registry";

class jsClassModelInfos extends FormController {
    actionInfoForm() {
                alert("HI")
                let a = [11,12,13,15,16]
                for(let i =0;i<=6;i++){
                    console.log(a[i])
                }
                console.log("Dhatri Modhvadiya")
                const b = 20 ;
                c = 30
                var c ;
                console.log(c)
                console.log("HI hello")
    }
}
jsClassModelInfos.template = "library_management.modelInfoBtn";

export const modelInfoView = {
    ...formView,
    Controller: jsClassModelInfos,
};
registry.category("views").add("model_info", modelInfoView);
