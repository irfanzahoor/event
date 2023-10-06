import frappe
import time

@frappe.whitelist()
def message(name,email,subject,message):
    doc = frappe.new_doc("User Message")
    doc.user_name = name
    doc.email= email
    doc.subject = subject
    doc.message = message
    doc.insert()
    # doc.save()
    time.sleep(3)
    frappe.msgprint("Your message has been sent. Thank you!")
