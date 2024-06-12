/* @odoo-module */

import { patch } from "@web/core/utils/patch";
import { FormController } from "@web/views/form/form_controller";

//addons/web/static/src/views/form/form_controller.js

patch(FormController.prototype,{
   demo(){
     alert("DEMO");
   },

});

