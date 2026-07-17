import os
from flask import Flask, render_template, jsonify
from inventory import inventory

app = Flask(__name__)

@app.route('/inventory', methods=['GET'])
def inventory_list():
    return jsonify(inventory)

@app.route('/inventory/<productid>', methods=['GET'])
def inventory_item(productid):
    for item in inventory:
        if item['productid'] == productid:
            return jsonify(item)
    return jsonify({'error': 'Product not found'}), 404

@app.route('/')
def hello():
    message = "It's running!"
    service = os.environ.get('K_SERVICE', 'Unknown service')
    revision = os.environ.get('K_REVISION', 'Unknown revision')
    return render_template('index.html', message=message, Service=service, Revision=revision)

if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')
