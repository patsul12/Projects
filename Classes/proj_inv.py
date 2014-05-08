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
		self.total_val = 0.00

	def add(self, object):
		self.products.append(object)

	def delete(self, object):
		self.products.remove(object)
	
	def list(self):
		print "\nList of Products: (id, name, quantity, price)"
		print "------------------------------------------"
		for product in self.products:
			print "|%s, %s, %s, %s|" % (product.id, product.name, product.quant, product.value)
		print "------------------------------------------"
		for product in self.products:
			self.total_val += product.value
		print "Total value of all products is: $%s\n" % (self.total_val)
		self.total_val = 0.00

	
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
	two.edit(new_value = 230000000.67)
	inv.list()
