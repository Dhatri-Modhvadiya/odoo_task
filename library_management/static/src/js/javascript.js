/** @odoo-module **/
import { ListController } from "@web/views/list/list_controller";
import { listView } from "@web/views/list/list_view";
import { registry } from "@web/core/registry";


class SalesReport extends ListController {
    setup(){
        super.setup();
        console.log('js is loaded');
    }

    async demo(){
     alert("DEMO");
   }
}
SalesReport.template = 'library_management.salenewbutton';

export const SalesReportListView = {
    ...listView,
    Controller: SalesReport,
}

registry.category("views").add('sale_list_button',SalesReportListView);