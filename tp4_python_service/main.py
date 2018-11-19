# inspiration
#https://gist.github.com/leon-sleepinglion/97bfd34132394e23ca5905ec730f776a
# install python3
# pip install flask, flast_restful, pyspark and numpy using pip3
from flask import (
    Flask,
    request,
    render_template
)
from flask_restful import (Api, Resource, reqparse)
from Invoice import Invoice, Item
import json

# Create the application instance
app = Flask(__name__, template_folder="templates")
api = Api(app)

invoices = list()


# Create a URL route in our application for "/"
@app.route('/')
def home():
    return render_template('home.html')


class InvoiceAPI(Resource):

    # Get the invoice at invoice_id
    # TODO: Return the actual invoice
    # TODO: return error when invoice ID not found
    def get(self, invoice_id):
        print(invoice_id)
        return "Invoice ID, " + invoice_id

    # Add a new item in an invoice
    # TODO: If invoice ID not found create a new invoice
    # TODO: If item is already present add to quantity?
    def post(self):
        data = request.get_json(force=True)
        inv = Invoice(data)
        # inv.add_item(Item(name=name, unit_price=unit_price, quantity=quantity))
        # invoices.append(inv)
        return 200

    # Replaces an invoice with an other
    # TODO: everything
    def put(self, invoice_id):
        return 200

    # Removes an invoice from the DB
    # TODO: everything
    def delete(self, invoice_id):
        return 200

api.add_resource(InvoiceAPI, '/invoice/<string:invoice_id>', '/invoice')

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)
