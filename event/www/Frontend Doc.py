import frappe

# def get_context(context):
#  context.update({
#   "test" : "irfan"
#  })
#  return context

def get_context(context):
 doc = frappe.get_doc("Frontend Doc", "Frontend Doc")
#  
 print(doc.event_budget)
 print(doc.event_id)
 print(doc.event_date)



 context.update({
  "doc" : doc
 })