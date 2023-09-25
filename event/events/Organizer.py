import frappe

@frappe.whitelist()
def book_data(organizerid, organizername, 
            Phone, email, eventhistory , fromdate, todate, 
            organizertype, Budget, insurance, agreement,
            description , permission , custom
):
    doc = frappe.new_doc("Event Organizer")
    doc.organizer_id = organizerid
    doc.organizer_name = organizername
    doc.phone = Phone
    doc.email= email
    doc.event_history = eventhistory
    doc.from_date = fromdate
    doc.to_date = todate
    doc.type_of_organizer = organizertype
    doc.budgeting_information = Budget
    doc.insurance_information = insurance
    doc.agreement = agreement
    doc.description = description
    doc.permissions_and_access = permission
    doc.custom_fields = custom
    doc.insert()
    # doc.save()
    frappe.msgprint("Complete")