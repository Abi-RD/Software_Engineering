'''
Capstone Project IV:
 - Objects & Class
 - Files
 - Functions
 - List
Q & A
'''
from tabulate import tabulate
from product import  Product

product_list = []
			
def read_File():
	with open("items.txt", "r") as items_file:
		items_file.readline()
		for line in items_file:
			b, l, p, q =line.strip('\n').split(',')
			prod = Product(b, l, float(p), int(q))
			product_list.append(prod)

def view_all():
	for p in product_list:
		print(p)
def update_file():
	file_upade = open("items.txt", 'w')
	file_upade.write("Barcode,Product Label,Product Price,Quantity")
	for p in product_list:
		file_upade.write(f'\n{p.to_file()}')
	file_upade.close()

def update_qty(item_b):
	pr_pos = -1
	for index, p in enumerate(product_list):
		if p.barcode == item_b:
			pr_pos = index

	if pr_pos == -1:
		print(f'{item_b} was not found')
	else:
		q = int(input(f"Enter new Qantity for product {item_b}: "))
		product_list[pr_pos].qty = q
		update_file()

def print_table():
	data_list = []
	top_row = ["Barcode","Product Label","Product Price","Quantity"]
	for p in product_list:
		data_list.append(p.to_table())
	#print(data_list)
	print(tabulate(data_list, top_row, tablefmt="grid"))

read_File()
print_table()
# b = input("Enter barcode: ")
# update_qty(b)