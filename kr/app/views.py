from flask import render_template, flash , redirect, url_for, request
from app import app, db
from app.forms import CreateProductForm, UpdateProductForm
from .models import Product, Category
import os


@app.route('/add', methods=['GET', 'POST'])
def add_product():
    cat = Category.query.all()
    categories=[(i.id, i.category) for i in cat]
    form = CreateProductForm()
    form.category.choices = categories
    if form.validate_on_submit():
        product = Product(code=form.code.data, name=form.name.data, instock=form.instock.data,
         number=form.number.data, cost=form.cost.data, 
         description=form.description.data, category_id=form.category.data)
        db.session.add(product)
        db.session.commit()
        flash("Product was created", category="info")
        return redirect(url_for('products'))

    return render_template('add.html', form=form)


@app.route('/products', methods=['GET', 'POST'])
def products():
    q = request.args.get('q')
    if q:
        products = Product.query.filter(Product.name.contains(q) | Product.description.contains(q))
    else:
        products = Product.query.order_by(Product.code.desc())
    
    return render_template('products.html', products=products)


@app.route('/product/<int:product_id>', methods=['GET', 'POST'])
def product(product_id):
    cat = Category.query.all()
    categories=[(i.id, i.category) for i in cat]
    form = UpdateProductForm()
    form.category.choices = categories
    product = Product.query.filter_by(id=product_id).first()
    if form.validate_on_submit():
        product.code = form.code.data
        product.name = form.name.data
        product.instock = form.instock.data
        product.number = form.number.data
        product.cost = form.cost.data
        product.description = form.description.data
        product.category_id = form.category.data
        db.session.commit()
        flash("Product was updated", category="info")
        return redirect(url_for('product', product_id=product.id))

    return render_template('product.html', product=product, form=form)


@app.route('/products/<int:product_id>/delete', methods=['GET', 'POST'])
def delete_product(product_id):
    product = Product.query.get(product_id)
    db.session.delete(product)
    db.session.commit()
    flash("Product was deleted", category="info")
    return redirect(url_for('products'))