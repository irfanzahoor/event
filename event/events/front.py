import frappe

@frappe.whitelist()
def front_data(fname,lname,fullname,phone):
  # frappe.msgprint(f'{father_name} and {phone}')
  doc = frappe.new_doc("Front Test")
  doc.first_name = fname 
  doc.last_name = lname
  doc.full_name = fullname
  doc.phone = phone
  doc.insert()
  # doc.save()
  frappe.msgprint("Complete")