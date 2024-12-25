from flask import Blueprint, render_template, flash , redirect
from flask_login import login_required, current_user
from .forms import ShopItemsForm, OrderUpdateForm
from werkzeug.utils import secure_filename
from .models import Product, Wishlist, Order, Customer
from . import db
admin_id = [1]
admin = Blueprint('admin', __name__)

@admin.route('/add-shop-items', methods=['GET','POST'])
@login_required
def add_shop_items():
    if current_user.id in admin_id:#if admin is the current user e.g. for admin, customer.id is 1
        form = ShopItemsForm()
        
        if form.validate_on_submit():
            product_name = form.product_name.data
            previous_price = form.previous_price.data
            current_price = form.current_price.data
            in_stock = form.in_stock.data
            flash_sale = form.flash_sale.data
            
            """Getting file, validating filename, saving to media directory"""
            file = form.product_picture.data
            file_name = secure_filename(file.filename) # Toyota Corolla.jpeg --> toyota_corolla.jpeg
            file_path = f'./media/{file_name}'
            file.save(file_path)
            
            """Pushing data in DB"""
            new_product = Product()
            new_product.product_name = product_name
            new_product.previous_price = previous_price
            new_product.current_price = current_price
            new_product.in_stock = in_stock
            new_product.flash_sale = flash_sale
            
            new_product.product_picture = file_path
            
            try:
                db.session.add(new_product)
                db.session.commit()
                flash(f'{product_name} Added for Sale Successfully!')
                return render_template('add-shop-items.html', form=form)
            
            except Exception as e:
                print(e)
                flash(f'{product_name} Failed to Add for Sale!')
            
        else:
            pass
        return render_template('add-shop-items.html', form=form)
    

    return render_template('404.html')

@admin.route('/remove-product/<int:item_id>', methods=['GET','POST'])
@login_required
def remove_product(item_id):
    if current_user.id in admin_id:
        try:
            target = Product.query.get(item_id)
            target_exists = Wishlist.query.filter_by(product_id=item_id).all()
            
            for item in target_exists:
                db.session.delete(item)
            
            db.session.delete(target)
            db.session.commit()
            flash(f'{target.product_name} has been removed successfully!')
            return redirect('/show-added-cars')
        
        except Exception as e:
            print(e)
            flash(f'{target.product_name} removal failed!')

        return redirect('/show-added-cars')

    return render_template('404.html')

@admin.route('/view-orders')
@login_required
def view_orders():
    if current_user.id in admin_id:
        orders = Order.query.all()
        return render_template('view_orders.html', orders = orders)
    return render_template('404.html')


@admin.route('/update-order-status/<int:order_id>', methods = ['GET', 'POST'])
@login_required
def update_order_status(order_id):
    if current_user.id in admin_id:
        form = OrderUpdateForm()
        order = Order.query.get(order_id)

        if form.validate_on_submit():
            status = form.order_status.data
            order.status = status

            try:
                db.session.commit()
                flash(f'Order {order_id} Updated successfully')
                return redirect('/view-orders')
            except Exception as e:
                print(e)
                flash(f'Order {order_id} Update Failed!')
                return redirect('/view-orders')

        return render_template('update_order_status.html', form=form)

    return render_template('404.html')

@admin.route('/customers')
@login_required
def display_customers():
    if current_user.id in admin_id:
        customers = Customer.query.all()
        return render_template('customers.html', customers=customers)
    return render_template('404.html')

@admin.route('/admin-page')
@login_required
def admin_page():
    if current_user.id in admin_id:
        return render_template('admin.html')
    return render_template('404.html')