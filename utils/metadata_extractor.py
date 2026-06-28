import re


def extract_metadata(text):

    metadata = {}

    invoice = re.search(r"Invoice\s*No\.?\s*(\d+)", text, re.I)
    if invoice:
        metadata["invoice_no"] = invoice.group(1)

    credit_note = re.search(r"Credit\s*Note\s*No\.?\s*(CN\d+)", text, re.I)
    if credit_note:
        metadata["credit_note_no"] = credit_note.group(1)

    grn = re.search(r"GRN\s*No\.?\s*([A-Za-z0-9/-]+)", text, re.I)
    if grn:
        metadata["grn_no"] = grn.group(1)

    po = re.search(r"PO\s*No\.?\s*([A-Za-z0-9/-]+)", text, re.I)
    if po:
        metadata["po_no"] = po.group(1)

    return metadata