from flask import render_template, flash , redirect, url_for, request, jsonify
from app import app, db
from app.forms import CreateProductForm, UpdateProductForm
from .models import Product, Category
import os


@app.route('/api/add', methods=['GET', 'POST'])
def add_product():
    req = request.json
    if not req :
        abort(400)
    
    product = Product(code=req.get('code'), name=req.get('name'), instock=req.get('instock'), number=req.get('number'), cost=req.get('cost'), description=req.get('description'), category_id=req.get('category_id'))
    
    db.session.add(product)
    db.session.commit()

    return jsonify({'message' : 'The product has been created!'})


@app.route('/api/products', methods=['GET', 'POST'])
def products():
    products = Product.query.all()
    output = []
    for product in products:
        product_data = {}
        product_data['id'] = product.id
        product_data['code'] = product.code
        product_data['name'] = product.name
        product_data['instock'] = product.instock
        product_data['number'] = product.number
        product_data['cost'] = product.cost
        product_data['description'] = product.description
        product_data['category_id'] = product.category_id
        output.append(product_data)
    
    return jsonify({'products' : output})


@app.route('/api/product/<int:product_id>', methods=['GET', 'POST'])
def product(product_id):
    product = Product.query.filter_by(id=product_id).first()
    
    if not product:
        return jsonify({'message' : 'No found!'})
    
    product_data = {}
    product_data['id'] = product.id
    product_data['code'] = product.code
    product_data['name'] = product.name
    product_data['instok'] = product.instock
    product_data['number'] = product.number
    product_data['cost'] = product.cost
    product_data['description'] = product.description
    product_data['category_id'] = product.category_id
    
    return jsonify({'products' : product_data})


@app.route('/api/update/<int:product_id>', methods=['GET', 'POST'])
def update_product(product_id):
    product = Product.query.filter_by(id=product_id).first()
    
    if not product:
        return jsonify({'message' : 'No found!'})
    
    req = request.json
    if not req :
        abort(400)
    
    product.code=req.get('code')
    product.name=req.get('name')
    product.instock=req.get('instock')
    product.number=req.get('number')
    product.cost=req.get('cost')
    product.description=req.get('description')
    product.category_id=req.get('category_id')
    
    db.session.commit()

    return jsonify({'message' : 'The product has been updated!'})


@app.route('/api/products/<int:product_id>/delete', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'message' : 'No post found!'})
    db.session.delete(product)
    db.session.commit()

    return jsonify({'message' : 'The product has been deleted!'})