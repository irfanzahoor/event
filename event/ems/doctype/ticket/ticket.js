// Copyright (c) 2023, NexTash and contributors
// For license information, please see license.txt

frappe.ui.form.on('Ticket', {
	validate: function(frm) {
		frm.set_value("remaining_tickets", frm.doc.total_tickets - "" - frm.doc.sold_tickets)
	}
});
