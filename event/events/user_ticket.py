import frappe

@frappe.whitelist()

def ticket(EventName , Date , vanue , Section , Quantity , username , Mobile , Email , PaymentMethod  ,OrderDate , TicketType ):
    doc = frappe.new_doc("Ticket User")
    # doc.ticket_id = TicketId
    doc.event_name = EventName
    doc.date_and_time = Date
    doc.venue = vanue
    doc.ticket_type = TicketType
    doc.seatsection = Section
    doc.quantity = Quantity
    doc.ticket_holder_name = username
    doc.email = Email
    doc.mobile = Mobile
    doc.payment_information = PaymentMethod
    # doc.order_number = OrderNumber
    doc.order_date = OrderDate
    # doc.access_control = Access
    doc.insert()
    frappe.msgprint("Thanks for Visit Us....")