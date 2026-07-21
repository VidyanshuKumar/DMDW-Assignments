class Product:
    def input(self):
        self.product_no = int(input("Enter Product Number: "))
        self.product_name = input("Enter Product Name: ")
        self.cost = float(input("Enter Cost: "))
        self.quantity = int(input("Enter Quantity: "))

    def calculate(self):
        self.total_amount = self.cost * self.quantity

    def display(self):
        print("\n----- Product Details -----")
        print("Product Number :", self.product_no)
        print("Product Name   :", self.product_name)
        print("Cost           :", self.cost)
        print("Quantity       :", self.quantity)
        print("Total Amount   :", self.total_amount)



p = Product()


p.input()
p.calculate()
p.display()