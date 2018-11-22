from bson import ObjectId


class InvoiceService():
    def __init__(self, database):
        self.database = database
    
    # Returns all invoices in database as array.
    # Object form is {'invoice': {'item': [{'unit_price': float, 'name': string, 'quantity': integer}]}, '_id': ObjectId}
    def get_all_invoices(self):
        invoices = self.database.find({})
        return invoices

    # Returns the invoice associated to the specified id if it exists.
    def get_invoice(self, invoice_id):
        invoice = self.database.find_one({"_id": ObjectId(invoice_id)})
        if invoice is not None:
            invoice["_id"] = str(invoice["_id"])
        return invoice

    # Inserts the invoice in the mongo database and returns the generated id.
    def insert_invoice(self, invoice_dto):
        result = self.database.insert_one(invoice_dto)
        return {"_id": str(result.inserted_id)}

    def update_invoice(self, invoice_id, invoice_dto):
        result = self.database.update_one({"_id": ObjectId(invoice_id)}, { "$set": invoice_dto})
        return {"modified_count": result.modified_count}

    def delete_invoice(self, invoice_id):
        result = self.database.delete_one({"_id": ObjectId(invoice_id)})
        return {"deleted_count": result.deleted_count}
