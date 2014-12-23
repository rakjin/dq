
class Node:

	def __init__(self, altitude):
		self.altitude = altitude
		self.adjacents = []
		self.is_destination = False

	def add_adjacent_node(self, node):
		self.adjacents.append(node)

	# def __iter__(self):
	# 	for node in self.adjacents:
	# 		if node.visit_possible(from_=self):
	# 			clone = Node(self.altitude)
	# 			clone.adjacents = adjacents
	# 			yield node
	# 	raise StopIteration()

	def remove_unvisitable_adjacents(self):
		visitable_adjacents = \
			[node for node in self.adjacents if node.is_visitable(from_=self)]
		self.adjacents = visitable_adjacents


	def is_visitable(self, from_):
		if self in from_.adjacents and \
		   from_.altitude >= self.altitude:
		   	return True
		return False

	def __repr__(self):
		return '<Node altitude=%d>' % self.altitude

input = '2 5\n\
88 99 44 33 22\n\
77 66 55 99 11'


rows = input.splitlines()

dimension = rows.pop(0)
dimension = dimension.split(' ')
height = int(dimension[0])
width = int(dimension[1])



for y in range(0, len(rows)):
	row = rows[y] = rows[y].split(' ')
	for x in range(0, len(row)):
		altitude = row[x] = int(row[x])
		node = row[x] = Node(altitude)

		if x > 0:
			left = row[x-1]
			node.add_adjacent_node(left)
			left.add_adjacent_node(node)

		if y > 0:
			upper = rows[y-1][x]
			node.add_adjacent_node(upper)
			upper.add_adjacent_node(node)

flat = [item for sublist in rows for item in sublist] # googled

last_node = flat[-1]
last_node.is_destination = True

[node.remove_unvisitable_adjacents() for node in flat]

node0 = flat[0]

def visit(node):
	print('visiting %s' % node)
	if node.is_destination:
		print('destination')
		return
	for i in range(0, len(node.adjacents)):
		adjacent = node.adjacents[i]
		visit(adjacent)
	print('dead end')

visit(node0)
