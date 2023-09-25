import frappe

@frappe.whitelist()
def book_data(name,address,city,state,fromdate,todate,eventname,ticket,upload,email,password):
    doc = frappe.new_doc("Book Event")
    doc.user_name = name
    doc.address = address
    doc.city = city
    doc.state = state
    doc.from_date = fromdate
    doc.to_date = todate
    doc.event_name = eventname
    doc.choose_file = upload
    doc.total_tickets = ticket
    doc.email= email
    doc.password = password
    doc.insert()
    # doc.save()
    frappe.msgprint("Complete")