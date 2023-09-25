import frappe

def get_context(data):
 ticket = frappe.get_doc("Ticket")
#  print(ticket)

 return data.update({
  "ticket" : ticket
 })