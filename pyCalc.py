# class 'Calc' implemented with four calculator opeartion.
class Calc():
	
	# Constructor
	def __init__(self, a, b):
		self.a = a
		self.b = b

	# Operations:
	def add(self):
		return (self.a+self.b)

	def sub(self):
		return (self.a-self.b)

	def mul(self):
		return (self.a*self.b)

	def div(self):
		return (self.a/self.b)

	# Destructor
	def __del__(self):
		pass

# function which interects with class and function to perform operation based on user choice.
def fn(a,b,choice):
	obj = Calc(a,b)
	if choice==1:
		print(obj.add())
	elif choice==2:
		print(obj.sub())
	elif choice==3:
		print(obj.mul())
	elif choice==4:
		print(obj.div())

# Function that includes menu for a better look.
def menu():
	print("-"*55)
	print('\t\t-: Welcome to OOPs-Calculator :-')
	print("-"*55)

	print("Select from the following operations: ")
	print('''
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit
		''')

	print("-"*55)

# Driver code
if __name__ == '__main__':

	menu()
	while(True):
		try:
			choice = int(input("\nChoice: "))

			if choice==1:
				print("\nAdd operation Selected.")
			elif choice==2:
				print("\nSubtract operation Selected.")
			elif choice==3:
				print("\nMultiplication operation Selected.")
			elif choice==4:
				print("\nDivide operation Selected.")
			elif choice==5:
				print("Signing off...")
				break
			else:
				print("\nInvalid Choice!")
				continue

			a = float(input("Enter A: "))
			b = float(input("Enter B: "))

			fn(a,b,choice)
		except:
			print("\nInvalid Choice!")