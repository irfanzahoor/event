import frappe

def get_context(context):

    # "Test User" doctype se "User Test-00005" naam ka document retrieve karein

    doc = frappe.get_doc("Test User", "User Test-00005")
    
    # Context dictionary mein yeh document update karein, "doc" key ke neeche
    
    context.update({
       "doc": doc 
    })
