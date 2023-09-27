import frappe

def get_context(context):
    doc = frappe.get_all("Event Schedule", fields="*")
    context.update({
        "doc": doc
    })


    doc2 = frappe.get_all("Event Schedule2", fields="*")
    print(doc2)
    context.update({
        "doc2": doc2
    })

    doc1 = frappe.get_all("Event Schedule1", fields="*")
    print(doc1)
    context.update({
        "doc1": doc1
    })