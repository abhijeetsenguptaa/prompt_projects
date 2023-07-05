from flask import Flask, request, render_template, redirect
from flask_cors import CORS
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
cors = CORS(app)

# MongoDB Atlas connection details
# Replace <username>, <password>, <cluster_name>, and <database_name> with your own values
username = "abhijeet"
password = "abhijeetsenguptaa"
cluster_name = "cluster0.cdgrd8h"
database_name = "zesty_zomato"

# Create the MongoDB Atlas connection string
connection_string = f"mongodb+srv://{username}:{password}@{cluster_name}.mongodb.net/{database_name}?retryWrites=true&w=majority"

# Create a MongoClient instance
client = MongoClient(connection_string)

# Access the database
db = client[database_name]

# Access the collection
menu_collection = db["menu"]
# orders_collection = db["orders"]

# Routes
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/menu")
def menu():
    menu_items = list(menu_collection.find())
    return render_template("menu.html", menu=menu_items)

@app.route("/add_dish", methods=["GET", "POST"])
def add_dish():
    if request.method == "POST":
        name = request.form["dish_name"]
        price = float(request.form["price"])
        availability = request.form["availability"]

        new_dish = {
            "name": name,
            "price": price,
            "availability": availability,
        }
        print(new_dish)
        menu_collection.insert_one(new_dish)
        return redirect("/menu")

    return render_template("add_dish.html")

@app.route("/update", methods=["POST"])
def update():
    id = request.form["id"]
    name = request.form["name"]
    price = float(request.form["price"])
    availability = request.form["availability"]

    menu_collection.update_one(
        {"_id": ObjectId(id)},
        {"$set": {"name": name, "price": price, "availability": availability}}
    )
    return redirect("/menu")


@app.route("/delete", methods=["POST"])
def delete():
    id = request.form["id"]
    menu_collection.delete_one({"_id": ObjectId(id)})
    return redirect("/menu")

orders_collection = db['orders']

@app.route('/add_order', methods=['POST'])
def add_order():
    customer_name = request.form['customer_name']
    item_name = request.form['item_name']
    item_id = request.form['item_id']
    quantity = int(request.form['quantity'])
    total_price = float(request.form['total_price'])
    status = request.form['status']

    order = {
        'name': customer_name,
        'item_name': item_name,
        'item_id': item_id,
        'quantity': quantity,
        'total_price': total_price,
        'status': status
    }

    orders_collection.insert_one(order)

    return '''
    <html>
    <head>
        <style>
            .popup {
                position: fixed;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                background-color: #fff;
                padding: 20px;
                border-radius: 5px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
                display: none;
                animation-name: popupAnimation;
                animation-duration: 1s;
            }

            .popup.show {
                display: block;
            }

            .popup p {
                margin: 0;
                text-align: center;
                font-weight: bold;
            }

            @keyframes popupAnimation {
                0% {
                    transform: translate(-50%, -50%) scale(0.8);
                    opacity: 0;
                }
                100% {
                    transform: translate(-50%, -50%) scale(1);
                    opacity: 1;
                }
            }

            .tick-mark {
                display: inline-block;
                width: 40px;
                height: 40px;
                background-image: url('https://th.bing.com/th/id/OIP.oYSdZ2ozK1UW890889kGCQHaId?w=157&h=180&c=7&r=0&o=5&dpr=1.5&pid=1.7');
                background-size: cover;
                animation-name: tickAnimation;
                animation-duration: 1s;
                animation-delay: 0.5s;
                animation-fill-mode: both;
            }

            @keyframes tickAnimation {
                0% {
                    transform: scale(0.1) rotate(0deg);
                }
                70% {
                    transform: scale(1.2) rotate(0deg);
                }
                100% {
                    transform: scale(1) rotate(720deg);
                }
            }
        </style>
    </head>
    <body>
        <div class="popup">
            <div class="tick-mark"></div>
            <p>Order added successfully!</p>
        </div>

        <script>
            document.addEventListener("DOMContentLoaded", function () {
                var popup = document.querySelector(".popup");
                popup.classList.add("show");
            });
        </script>
    </body>
    </html>
    '''


@app.route("/orders")
def orders():
    orders = list(orders_collection.find())
    return render_template("order.html", orders=orders)

@app.route("/update_order", methods=["POST"])
def update_order():
    id = request.form["id"]
    item_name = request.form["item_name"]
    quantity = int(request.form["quantity"])
    total_price = float(request.form["total_price"])
    customer_name = request.form["name"]
    status = request.form["status"]

    orders_collection.update_one(
        {"_id": ObjectId(id)},
        {"$set": {
            "item_name": item_name,
            "quantity": quantity,
            "total_price": total_price,
            "name": customer_name,
            "status": status
        }}
    )
    return redirect("/orders")

@app.route("/delete_order", methods=["POST"])
def delete_order():
    id = request.form["id"]
    orders_collection.delete_one({"_id": ObjectId(id)})
    return redirect("/orders")

if __name__ == "__main__":
    app.run(port=8080)
