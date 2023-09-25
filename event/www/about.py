import frappe

# def get_context(context):
#  context.update({
#   "test" : "irfan"
#  })
#  return context

def get_context(data):
 about = frappe.get_doc("About Event")
#  print(about)

 return data.update({
  "test" : about
 })


