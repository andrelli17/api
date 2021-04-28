from product import productos
from flask import Flask, jsonify


app1=Flask(__name__)

@app1.route('/ping')
def ping():
    return jsonify({"message":"pong"})

@app1.route('/product')
def getProduct():
    return jsonify(productos)
"""
@app1.route('/product/<>/string:product_nombre')
def getProducts(product_nombre):
   productFound= [product for product in productos['nombre']==product_nombre]
    return "recibido"
"""
if __name__=='__main__':
    app1.run(debug=True, port=4000)