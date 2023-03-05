class  Product:
	def __init__(self, barcode, prod_label, prod_price, prod_qty):
		self.barcode = barcode
		self.label = prod_label
		self.price = prod_price
		self.qty = prod_qty
	def to_file(self):
		return f'''{self.barcode},{self.label},{self.price},{self.qty}'''
	def to_table(self):
		return [self.barcode, self.label, self.price, self.qty]
	def __str__(self):
		return f'''===================
Item Barcode: {self.barcode}
Item Description: {self.label}
Item Price: {self.price}
Qantity: {self.qty}
=====================
'''
