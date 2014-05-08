class Product(object):

	def __init__(self, name, quant = 0, value = 0.00):
		self.id = id(self)
		self.name = name
		self.quant = quant
		self.value = value

	def edit(self, new_name = None, new_quant = None, new_value = None):
		if new_name != None:
			self.name = new_name
		elif new_quant != None:
			self.quant = new_quant
		elif new_value != None:
			self.value = new_value
		else:
			pass

class Inventory():
	
	def __init__(self):
		self.product_count = 0
		self.products = []

	def add(self, object):
		if object.id in self.products:
			self.products.remove(object)
		self.products.append(object)

	def delete(self, object):
		self.products.remove(object)
	
	def list(self):
		print "\nList of Products: (name, quantity, price)"
		print "------------------------------------------"
		for product in self.products:
			print "|%s, %s, %s, %s|" % (product.id, product.name, product.quant, product.value)
		print "------------------------------------------"


	
if __name__ == "__main__":
	inv = Inventory()
	one = Product("tomato", 234, 23.99)
	two = Product("carrot", 54, 43.55)
	three = Product("asparagus", 456789, 12345678.34)
	one.edit(new_name = "fish")

	inv.add(one)
	inv.add(two)
	inv.add(three)

	inv.list()

	one.edit(new_quant = 2345678)
	inv.list()
