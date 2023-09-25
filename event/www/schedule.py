import frappe

def get_context(context):
    doc = frappe.get_all("Event Schedule",fields = "*")


    context.update({
        "doc" : doc
    })
    