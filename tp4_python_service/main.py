# To run this project, first install python3, apache spark and pip.
# Then using pip, install the following packages: flask, flask_restful, flask_cors, pyspark, numpy and pymongo
# Finally, make sure the environment variable is correct export PYSPARK_PYTHON=/usr/bin/python3.5 or 'which python3.5'

from flask import (
    Flask,
    abort,
    request,
    render_template
)
from flask_restful import (Api, Resource, reqparse)
from flask_cors import CORS
from Invoice import InvoiceService
from mongo import CustomMongoClient
from pyspark.sql import SparkSession

# Create the mongo client
mongo_client = CustomMongoClient("mongodb://localhost:27017", "log8430-tp4")
invoice_service = InvoiceService(mongo_client.getCollection("invoices"))

# Create the application instance
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app)

# Create the Spark connector
invoice_spark = SparkSession.builder.appName("myInvoiceApp") \
    .config("spark.mongodb.input.uri", "mongodb://127.0.0.1/log8430-tp4.invoices") \
    .config("spark.mongodb.output.uri", "mongodb://127.0.0.1/log8430-tp4.invoices") \
    .config("spark.jars.packages", "org.mongodb.spark:mongo-spark-connector_2.11:2.2.5") \
    .getOrCreate()

# Create a URL route in our application for "/"
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/invoice/item/frequency')
def getInvoiceItemFrequency():
    pipeline = """[
                    { $sortByCount: "$invoice.items.name" },
                    { $unwind: { path: "$_id"} },
                    { $group:
                        {
                            _id: "$_id",
                            total: {
                                $sum: "$count"
                            }
                        }
                    },
                    { $sort: { total: -1} },
                    { $limit: 3 }
               ]"""
    df = invoice_spark.read.format('com.mongodb.spark.sql.DefaultSource').option('pipeline', pipeline).load()
    d = []
    for row in df.rdd.map(lambda x: (x._id, x.total)).collect():
        d.append({"name": row[0], "freq": row[1]})
    return str(d)
    

class InvoiceAPI(Resource):
    @staticmethod
    def isValidInvoice(data):
        if 'invoice' in data:
            if 'items' in data['invoice']:
                for item in data['invoice']['items']:
                    if 'name' not in item:
                        return False
                    if 'unit_price' not in item:
                        return False
                    if 'quantity' not in item:
                        return False
                return True
            return False
        return False

    # Get an invoice
    def get(self, invoice_id):
        invoice = invoice_service.get_invoice(invoice_id)
        if invoice is None:
            abort(404)
        print(invoice)
        return invoice

    # Create a new invoice
    def post(self):
        data = request.get_json(force=True)
        if InvoiceAPI.isValidInvoice(data):
            return invoice_service.insert_invoice(data)
        abort(400)

    # Update an existing invoice
    def put(self, invoice_id):
        data = request.get_json(force=True)
        if InvoiceAPI.isValidInvoice(data):
            return invoice_service.update_invoice(invoice_id, data)
        abort(400)

    # Remove an invoice
    def delete(self, invoice_id):
        return invoice_service.delete_invoice(invoice_id)

api.add_resource(InvoiceAPI, '/invoice/<string:invoice_id>', '/invoice')

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)
