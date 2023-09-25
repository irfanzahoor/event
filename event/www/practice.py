import frappe

def get_context(context):
    # "Practice" records ke data ko retrieve karein
    doc = frappe.get_doc("Practice")

    print(doc)

    # Har "Practice" record ke liye loop karein
    for record in doc.practice_child:
        
        print("Sawal", record.idx, record.question)
        print("Jawab", record.idx, record.answer)

    # Context dictionary ko tayyar karein
    context = {
        'q': doc 
    }
    return context