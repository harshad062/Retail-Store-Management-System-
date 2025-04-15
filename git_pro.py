import datetime

class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

class Sale:
    def __init__(self, product, quantity_sold, sale_time):
        self.product = product
        self.quantity_sold = quantity_sold
        self.total_price = product.price * quantity_sold
        self.sale_time = sale_time

class Store:
    def __init__(self):
        self.products = {}
        self.sales = []

    def add_product(self, product_id, name, price, quantity):
        if product_id in self.products:
            self.products[product_id].quantity += quantity
            print(f"Updated stock for {name}.")
        else:
            self.products[product_id] = Product(product_id, name, price, quantity)
            print(f"Added new product: {name}.")

    def view_products(self):
        print("\nAvailable Products:")
        for product in self.products.values():
            print(f"ID: {product.product_id} | Name: {product.name} | Price: ${product.price} | Stock: {product.quantity}")

    def make_sale(self, product_id, quantity):
        if product_id not in self.products:
            print("Product ID not found.")
            return
        product = self.products[product_id]
        if product.quantity < quantity:
            print(f"Insufficient stock. Available: {product.quantity}")
            return
        product.quantity -= quantity
        sale = Sale(product, quantity, datetime.datetime.now())
        self.sales.append(sale)
        print(f"Sold {quantity} of {product.name}. Total: ${sale.total_price:.2f}")

    def view_sales(self):
        print("\nSales Report:")
        for sale in self.sales:
            print(f"{sale.sale_time.strftime('%Y-%m-%d %H:%M:%S')} | Product: {sale.product.name} | Quantity: {sale.quantity_sold} | Total: ${sale.total_price:.2f}")

def main():
    store = Store()
    while True:
        print("\n--- Retail Store Management ---")
        print("1. Add Product")
        print("2. View Products")
        print("3. Make a Sale")
        print("4. View Sales")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            pid = input("Enter Product ID: ")
            name = input("Enter Product Name: ")
            price = float(input("Enter Product Price: "))
            quantity = int(input("Enter Quantity: "))
            store.add_product(pid, name, price, quantity)

        elif choice == "2":
            store.view_products()

        elif choice == "3":
            pid = input("Enter Product ID to sell: ")
            quantity = int(input("Enter Quantity to sell: "))
            store.make_sale(pid, quantity)

        elif choice == "4":
            store.view_sales()

        elif choice == "5":
            print("Exiting system.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
