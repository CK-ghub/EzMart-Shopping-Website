import traceback as tb
from flask import Blueprint, redirect, request, render_template, url_for, flash
from werkzeug.datastructures import MultiDict
from roles.permissions import admin_permission
from views.itemform import ItemForm
from flask_login import login_required, current_user
from sql.db import DB

admin = Blueprint('admin', __name__, url_prefix='/')

@admin.route('/admin/additem', methods = ["GET", "POST"])
@admin_permission.require(http_exception=403)
def add_item():
    # UCID: kc664 Date: 04/23/2023 - create/add a single item
    form = ItemForm()
    name = request.form.get("name", None)
    description = request.form.get("description", None)
    stock = request.form.get("stock", 0)
    cost = request.form.get("cost", None)
    image = request.form.get("image", None)
    visibility = True if int(stock) > 0 else False
    
    if form.validate_on_submit():
        try:
            result = DB.insertOne("""INSERT INTO IS601_S_Items (name, description, stock, cost, image, visibility) 
                                    VALUES (%s,%s,%s,%s,%s,%s)""",
                                    name, description, stock, cost, image, visibility)
            if result.status:
                flash(f"Successfully created item - '{form.name.data}'", "success")
        except Exception as e:
            print(tb.format_exc())
            flash(f"Error while creating item '{form.name.data}' :- {e}", "danger")
            
    return render_template("add_item.html", form=form)

@admin.route('/admin/viewitems', methods = ["GET", "POST"])
@admin_permission.require(http_exception=403)
def view_items():
    # UCID: kc664 Date: 04/23/2023  - will show items regardless of visibility
    rows = {}
    query = """SELECT id, name, description, stock, cost, image, visibility
               FROM IS601_S_Items LIMIT 25"""
    try:
        result = DB.selectAll(query)
        if result.status and result.rows:
            rows = result.rows
    except Exception as e:
        print(tb.format_exc())
        flash("There was a problem loading items", "danger")
    return render_template("admin_view_items.html", rows=rows)

@admin.route("/admin/item", methods=["GET","POST"])
@admin_permission.require(http_exception=403)
def view_item():
    # UCID: kc664 Date: 04/23/2023
    try:
        id = request.args.get("id", None)
        result = DB.selectOne("SELECT id, name, description, stock, cost, image FROM IS601_S_Items WHERE id = %s", id)
        if result.status and result.row:
            rows = result.row
    except Exception as e:
        print("Error fetching item", e)
        flash("Item not found", "danger")
        rows = []
    return render_template("view_item.html", rows=rows if rows else {})

@admin.route("/admin/edititem", methods=["GET","POST"])
@admin_permission.require(http_exception=403)
def edit_item():
    # UCID: kc664 Date: 04/23/2023 
    form = ItemForm()
    id = request.args.get("id", form.id.data or None)
    if id:
        if request.method == "POST" and form.validate_on_submit():
            visibility = True if int(form.stock.data)>0 else False
            try:
                result = DB.update("UPDATE IS601_S_Items set name = %s, description = %s, stock = %s, cost = %s, image=%s, visibility=%s WHERE id = %s",
                form.name.data, form.description.data, form.stock.data, form.cost.data, form.image.data, visibility, form.id.data)
                if result.status:
                    flash(f"Successfully updated item - '{form.name.data}'", "success")
            except Exception as e:
                print(tb.format_exc())
                flash(f"Error while updating item '{form.name.data}' :- {e}", "danger")
    
        try:
            result = DB.selectOne("SELECT id, name, description, stock, cost, image FROM IS601_S_Items WHERE id = %s", id)
            if result.status and result.row:
                form.process(MultiDict(result.row))
        except Exception as e:
            print("Error fetching item", e)
            flash("Item not found", "danger")
                      
    else:
        flash("ID is missing", "danger")
        return redirect(url_for("admin.view_items"))
            
    return render_template("edit_item.html", form = form)
        
                

@admin.route("/admin/deleteitem", methods=["GET","POST"])
@admin_permission.require(http_exception=403)
def delete_item():
    # UCID: kc664 Date: 04/23/2023 
    id = request.args.get("id")
    if id:
        try:
            result = DB.delete("DELETE FROM IS601_S_Items WHERE id = %s", id)
            if result.status:
                flash("Deleted item", "success")
        except Exception as e:
            print(tb.format_exc())
            flash(f"Error while deleting item :- {e}", "danger")
    return redirect(url_for("admin.view_items"))

@admin.route("/admin/orders", methods=["GET","POST"])
@admin_permission.require(http_exception=403)
def orders():
    # UCID: kc664 Date: 05/05/2023
    # to list all orders
    rows = []
    try:
        result = DB.selectAll("""
        SELECT A.id, B.username, total_price, number_of_items, A.created 
        FROM IS601_S_Orders A
        JOIN IS601_Users B on A.user_id = B.id 
        """)
        if result.status and result.rows:
            rows = result.rows
    except Exception as e:
        print("Error getting orders", e)
        flash("Error fetching orders", "danger")
    return render_template("orders.html", rows=rows)

@admin.route("/admin/order", methods=["GET"])
@admin_permission.require(http_exception=403)
def order():
    # UCID: kc664 Date: 05/05/2023
    # to view a particular order details
    rows = []
    total = 0
    id = request.args.get("id")
    if not id:
        flash("Invalid order", "danger")
        return redirect(url_for("shop.orders"))
    try:
        # locking query to order_id and user_id so the user can see only their orders
        result = DB.selectAll("""
        SELECT name, A.unit_cost, A.quantity, (A.unit_cost*A.quantity) as subtotal 
        FROM IS601_S_OrderItems A 
        JOIN IS601_S_Items B on A.item_id = B.id 
        WHERE order_id = %s
        """, id)
        if result.status and result.rows:
            rows = result.rows
            total = sum(int(row["subtotal"]) for row in rows)
        result = DB.selectAll("""
        SELECT first_name, last_name, address, payment_method
        FROM IS601_S_Orders where id=%s
        """, id)
        if result.status and result.rows:
            order_info = result.rows
    except Exception as e:
        print("Error getting order", e)
        flash("Error fetching order", "danger")
        rows = []
        total = None
        order_info = []
    print(rows)
    print(order_info)
    return render_template("order.html", rows=rows, total=total, order_info=order_info )

