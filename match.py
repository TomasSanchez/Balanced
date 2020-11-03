class Stack():
	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def get_stack(self):
		return self.items

	def is_empty(self):
		return self.items == []

	def first_item(self):
		if not self.is_empty():
			return self.items[-1]



def match(text):
	stack = Stack()
	index = 0
	is_balanced = True

	if text[index] in '], }, )':
		return False

	def match(top, item):
		if top == '(' and item == ')':
			return True
		elif top == '{' and item == '}':
			return True
		elif top == '[' and item == ']':
			return True
		else:
			return False

	while index < len(text) and is_balanced:
		item = text[index]
		if item in '(, {, [':
			stack.push(item)
		else:
			if stack.is_empty():
				is_balanced = False
			else:
				top = stack.pop()
				if not match(top, item):
					is_balanced = False
		index += 1

	return is_balanced
