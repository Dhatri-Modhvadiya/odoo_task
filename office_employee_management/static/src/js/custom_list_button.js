/* @odoo-module */
import { ListController } from "@web/views/list/list_controller";
import { listView } from "@web/views/list/list_view";
import { registry } from "@web/core/registry";

class jsClassModelInfo extends ListController {
action_hrList() {
                const res = "Hi"
    }
}
jsClassModelInfo.template = "hr_expense.modelHrBtn";

export const modelInfoView = {
    ...listView,
    Controller: jsClassModelInfo,
};

registry.category("views").add("model_hr", modelInfoView);