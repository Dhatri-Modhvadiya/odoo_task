/* @odoo-module */
import { patch } from "@web/core/utils/patch";
import { ExpenseListController } from '@hr_expense/views/list';
patch(ExpenseListController.prototype, {

        setup() {
            super.setup();
        },
        async actionHrList() {
          var a = 10;
        let b = 20;
          try{

            alert("hiii")
            const records = this.model.root.selection;
            const recordIds = records.map((a) => a.resId);
            console.log(typeof records)
            for (let key in records){
            console.log("keys and val" + key+ ":" +records[key].data.name)
            console.log(a,b)

            }
            console.log(records)
            console.log(recordIds)
               const pqr = new Date();
          console.log(pqr);
          }
          catch(error){
            console.log("Catch Block>>>>>>>>>", error)
          }
            },

        // Outputs the current date and time

//              var date = new Date();
//        const easternTime = date.toLocaleString("en-US", {timeZone: "America/New_York"});
//        const londonTime = date.toLocaleString("en-GB", {timeZone: "Europe/London"});
//        console.log(easternTime)
//        console.log(londonTime)
//          console.log(date)

    });
