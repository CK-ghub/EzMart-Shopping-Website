from flask import Blueprint, request, flash, render_template, redirect, url_for
from werkzeug.datastructures import MultiDict
from sql.db import DB
from flask_login import login_required, current_user
import traceback as tb

shop = Blueprint('shop', __name__, url_prefix='/',template_folder='templates')

@login_required
def get_item_count():
    query = "SELECT IFNULL(SUM(quantity), 0) as total from IS601_S_Cart where user_id = %s"
    result = DB.selectOne(query, current_user.get_id())
    if result.status and result.row:
        return int(result.row["total"])
    return 0
        

@shop.route("/shop", methods=["GET","POST"])
@login_required
def shop_list():
    # UCID: kc664 Date: 04/24/2023
    # to view all items as a logged-in user
    rows = []
    query = """SELECT id, name, description, stock, cost, image FROM IS601_S_Items WHERE visibility = 1"""
    args = [] # <--- append values to replace %s placeholders
    allowed_columns = ["name", "description", "cost"]
    for filter in allowed_columns[:-1]:
        if request.args.get(filter):
            query += f" AND {filter} LIKE %s"
            args.append(f"%{request.args.get(filter)}%")
    if request.args.get("order") and request.args.get("column"):
        if request.args.get("column") in allowed_columns \
            and request.args.get("order") in ["asc", "desc"]:
            query += f" ORDER BY {request.args.get('column')} {request.args.get('order')}"
    query += f" LIMIT %s"
    ql = int(request.args.get('limit', 25))
    if ql < 1 or ql > 100:
        flash("limit value should be in the range of 1-100; Defaulting to 25")
        args.append(25)
    else:
        args.append(ql)
    print("query",query)
    print("args", args)
    try:
        result = DB.selectAll(query, *args)
        if result.status and result.rows:
            rows = result.rows
    except Exception as e:
        print(tb.format_exc())
        flash("There was a problem loading items", "danger")
    return render_template("shop.html", rows=rows, allowed_columns=allowed_columns)

@shop.route("/shop/item", methods=["GET","POST"])
@login_required
def view_item():
    # UCID: kc664 Date: 04/23/2023
    # to view a specific item as a logged-in user
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

@shop.route("/cart", methods=["GET","POST"])
@login_required
def cart():
    # UCID: kc664 Date: 04/23/2023
    # to add and view cart as a logged-in user
    item_id = request.form.get("item_id")
    id = request.form.get("id", item_id)
    print("id", id)
    quantity = request.form.get("quantity", 1, type=int)
    user_id = current_user.get_id()
    if id and user_id:
        if quantity > 0:
            try:
                result = DB.selectOne("SELECT cost,name,stock from IS601_S_Items WHERE id = %s", id)
                print("result", result)
                if result.status and result.row:
                    cost = result.row["cost"]
                    name = result.row["name"]
                    stock = result.row["stock"]
                    if quantity > stock:
                        flash(f"{quantity} {name}s are not available; Please reduce the quantity", "danger")
                    else:
                        if item_id: # update from cart
                            result = DB.insertOne("""
                            UPDATE IS601_S_Cart SET
                            quantity = %(quantity)s,
                            cost = %(cost)s
                            WHERE item_id = %(id)s and user_id = %(user_id)s
                            """,{
                                "id":id,
                                "quantity": quantity,
                                "cost":cost,
                                "user_id":user_id
                            })
                            if result.status:
                                flash(f"Updated quantity for {name} to {quantity}", "success")
                        else: #add from shop
                            result = DB.insertOne("""
                            INSERT INTO IS601_S_Cart (item_id, quantity, cost, user_id)
                            VALUES(%(id)s, %(quantity)s, %(cost)s, %(user_id)s)
                            ON DUPLICATE KEY UPDATE
                            quantity = quantity + %(quantity)s,
                            cost = %(cost)s
                            """,{
                                "id":id,
                                "quantity": quantity,
                                "cost":cost,
                                "user_id":user_id
                            })
                            if result.status:
                                flash(f"Added {quantity} of {name} to cart", "success")
                                return redirect(url_for("shop.shop_list"))
            except Exception as e:
                print("Error updating cart" ,e)
                flash("Error updating cart", "danger")
        else:
            # assuming delete when quantity < 0
            try:
                result = DB.delete("DELETE FROM IS601_S_Cart where item_id = %s and user_id = %s", id, user_id)
                if result.status:
                    flash("Deleted item from cart", "success")
            except Exception as e:
                print("Error deleting item", e)
                flash("Error deleting item from cart", "danger")
    rows = []
    try:
        result = DB.selectAll("""SELECT A.id, item_id, name, A.quantity, (A.quantity * A.cost) as subtotal 
        FROM IS601_S_Cart A JOIN IS601_S_Items B on A.item_id = B.id
        WHERE A.user_id = %s
        """, current_user.get_id())
        if result and result.rows:
            rows = result.rows
    except Exception as e:
        print("Error getting cart", e)
        flash("Error fetching cart", "danger")
    return render_template("cart.html", rows=rows)

@shop.route("/confirm_order", methods=["GET","POST"])
@login_required
def confirm_order():
    # UCID: kc664 Date: 05/04/2023
    # to confirm order as a logged-in user
    cart = []
    total = 0
    try:
        # get cart to verify
        result = DB.selectAll("""SELECT A.user_id as user_id, A.id, item_id, name, A.quantity, B.stock, A.cost as cart_cost, B.cost as item_cost, (A.quantity * A.cost) as subtotal 
        FROM IS601_S_Cart A JOIN IS601_S_Items B on A.item_id = B.id
        WHERE A.user_id = %s
        """, current_user.get_id())
        if result.status and result.rows:
            cart = result.rows
        # verify cart
        has_error = False
        if len(cart)==0:
            flash("Cart is empty", "danger")
            return redirect(url_for("shop.cart"))
        for item in cart:
            if item["quantity"] > item["stock"]:
                flash(f"Item {item['name']} doesn't have enough stock left", "warning")
                has_error = True
                if item["stock"] == 0:
                    result = DB.delete("DELETE FROM IS601_S_Cart where item_id = %s and user_id = %s", item["item_id"], current_user.get_id())
                    flash(f"Deleting item: {item['name']} from your cart", "warning")
                else:
                    result = DB.insertOne("""
                            UPDATE IS601_S_Cart SET
                            quantity = %(quantity)s
                            WHERE item_id = %(id)s and user_id = %(user_id)s
                            """,{
                                "id":id,
                                "quantity": item["stock"],
                                "item_id":item["item_id"],
                                "user_id":item['user_id']
                            })
                    if result.status:
                        flash(f"Updated quantity for {item['name']} to {item['stock']}", "warning")
            if item["cart_cost"] != item["item_cost"]:
                flash(f"Item {item['name']}'s price has changed, the cart has been refreshed", "warning")
                has_error = True
                result = DB.insertOne("""
                            UPDATE IS601_S_Cart SET
                            cost = %(cost)s
                            WHERE item_id = %(item_id)s and user_id = %(user_id)s
                            """,{
                                "cost": item["item_cost"],
                                "item_id":item["item_id"],
                                "user_id":item['user_id']
                            })
                print(item)
                print(result.status)
                if result.status:
                    flash(f"Updated cost for {item['name']} to {item['item_cost']}")
            total += float(item["subtotal"] or 0) 
        if has_error:
            return redirect(url_for("shop.cart"))
    except Exception as e:
        print("Transaction exception", e)
        flash("Something went wrong", "danger")
        tb.print_exc()
        return redirect(url_for("shop.cart"))
    return render_template("pending_order.html", rows=cart, total=total)

@shop.route("/place_order", methods=["GET","POST"])
@login_required
def place_order():
    # UCID: kc664 Date: 05/04/2023
    # to place order and clear cart
    total = float(request.form.get('total', 0))
    total = f"{total:.2f}"
    money_received = float(request.form.get("money_received", 0))
    if money_received and f"{money_received:.2f}" == total:
        flash("Payment received, proceeding to place order", "success")
    elif money_received:
        flash("The payment received does not match the total cost, cancelling order", "danger")
        flash("Any amount debited will be refunded in 3-5 business days", "warning")
        return redirect(url_for("shop.cart"))
    else:
        flash("Payment failed, please try again")
        return redirect(url_for("shop.cart"))
    cart = []
    total = 0
    quantity = 0
    order = {}
    try:
        DB.getDB().autocommit = False # make a transaction

        # get cart to verify
        
        result = DB.selectAll("""SELECT A.id, item_id, name, A.quantity, B.stock, A.cost as cart_cost, B.cost as item_cost, (A.quantity * A.cost) as subtotal 
        FROM IS601_S_Cart A JOIN IS601_S_Items B on A.item_id = B.id
        WHERE A.user_id = %s
        """, current_user.get_id())
        if result.status and result.rows:
            cart = result.rows
        # verify cart
        has_error = False
        for item in cart:
            if item["quantity"] > item["stock"]:
                flash(f"Item {item['name']} doesn't have enough stock left", "warning")
                has_error = True
            if item["cart_cost"] != item["item_cost"]:
                flash(f"Item {item['name']}'s price has changed, the cart has been refreshed", "warning")
                has_error = True
            total += int(item["subtotal"] or 0)
            quantity += int(item["quantity"])
        
        # create order data
        order_id = -1
        if not has_error:
            result = DB.insertOne("""INSERT INTO IS601_S_Orders (first_name, last_name,
                                total_price, number_of_items, user_id, address, payment_method,
                                money_received)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""", request.form.get('fname'), request.form.get('lname'),
                                    total, quantity, int(current_user.get_id()),
                                    request.form.get('address'),request.form.get('payment'),
                                    money_received)
            if not result.status:
                flash("Error generating order", "danger")
                DB.getDB().rollback()
                has_error = True
            else:
                order_id = int(DB.db.fetch_eof_status()["insert_id"])
                order["order_id"] = order_id
                order["total"] = total
                order["quantity"] = quantity
        # record order history
        if order_id > -1 and not has_error:
            # Note: Not really an insert 1, it'll copy data from Table B into Table A
            result = DB.insertOne("""INSERT INTO IS601_S_OrderItems (quantity, unit_cost, order_id, item_id, user_id)
            SELECT quantity, cost, %s, item_id, user_id FROM IS601_S_Cart A WHERE A.user_id = %s""",
            order_id, current_user.get_id())
            if not result.status:
                flash("Error recording order history", "danger")
                has_error = True
                DB.getDB().rollback()
        # update stock based on cart data
        if not has_error:
            result = DB.update("""
            UPDATE IS601_S_Items 
                set stock = stock - (select IFNULL(quantity, 0) FROM IS601_S_Cart WHERE item_id = IS601_S_Items.id and user_id = %(uid)s),
                visibility = (select if(stock - (select IFNULL(quantity, 0) FROM IS601_S_Cart WHERE item_id = IS601_S_Items.id and user_id = %(uid)s)>0, 1, 0) 
                FROM IS601_S_Cart WHERE item_id = IS601_S_Items.id and user_id = %(uid)s) 
                WHERE id in (SELECT item_id from IS601_S_Cart where user_id = %(uid)s)
            """, {"uid":current_user.get_id()} )
            if not result.status:
                flash("Error updating stock", "danger")
                has_error = True
                DB.getDB().rollback()

        # empty the cart
        if not has_error:
            result = DB.delete("DELETE FROM IS601_S_Cart WHERE user_id = %s", current_user.get_id())
    
        if not has_error:
            DB.getDB().commit()
            flash("Purchase successful!", "success")
        else:
            return redirect(url_for("shop.cart"))
        order_info = [{"First_name": request.form.get('fname'),
                        "Last_name": request.form.get('lname'),
                        "Address": request.form.get('address'),
                        "Payment_Method": request.form.get('payment')
                        }]
    except Exception as e:
        print("Transaction exception", e)
        flash("Something went wrong", "danger")
        flash("Any amount debited will be refunded in 3-5 business days", "warning")
        tb.print_exc()
        return redirect(url_for("shop.cart"))
    return render_template("order_summary.html", rows=cart, order=order, order_info=order_info)

@shop.route("/payment", methods=["POST"])
@login_required
def payment():
    # UCID: kc664 Date: 05/04/2023
    # to make payment 
    missing = False
    reqd_fields = ['fname', 'lname', 'address', 'payment']
    form_data = {}
    for field in reqd_fields:
        if not request.form.get(field):
            flash(f"Missing Required Field: {field}, Please Try again", "danger")
            missing = True
        else:
            form_data[field] = request.form.get(field)
    print(missing)
    if missing:
        return redirect(url_for("shop.confirm_order"))
    return render_template("payment.html", form=form_data)

@shop.route("/orders", methods=["GET"])
@login_required
def orders():
    # UCID: kc664 Date: 05/04/2023
    # to view all orders specific to a user
    rows = []
    try:
        result = DB.selectAll("""
        SELECT id, total_price, number_of_items, created FROM IS601_S_Orders WHERE user_id = %s
        """, current_user.get_id())
        if result.status and result.rows:
            rows = result.rows
    except Exception as e:
        print("Error getting orders", e)
        flash("Error fetching orders", "danger")
    return render_template("orders.html", rows=rows)

@shop.route("/order", methods=["GET"])
@login_required
def order():
    # UCID: kc664 Date: 05/05/2023
    # to view a specific order
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
        WHERE order_id = %s AND user_id = %s
        """, id, current_user.get_id())
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