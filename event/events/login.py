import frappe
@frappe.whitelist()
def receive_data(email,name,passwd):
   data = frappe.new_doc("User")
   data.email = email
   data.first_name=name
   data.password = passwd
#    data.insert()
   data.save()
   frappe.msgprint("User Created")