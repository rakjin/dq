
class Node:
	def __init__(self, altitude):
		self.altitude = altitude
		self.adjacents = []
		self.is_destination = False

	def add_adjacent(self, node):
		self.adjacents.append(node)

	def remove_unvisitable_adjacents(self):
		visitables = \
			filter(lambda x: x.is_visitable(from_=self), self.adjacents)
		self.adjacents = visitables

	def is_visitable(self, from_):
		return (from_.altitude >= self.altitude)

	def __repr__(self):
		return '<Node altitude=%d>' % self.altitude


def parse_and_get_first_node(raw):
	rows = raw.splitlines()

	dimension = rows.pop(0)
	dimension = dimension.split(' ')
	height = int(dimension[0])
	width = int(dimension[1])

	for y in range(0, len(rows)):
		row = rows[y] = rows[y].split(' ')
		for x in range(0, len(row)):
			altitude = row[x] = int(row[x])
			row[x] = node = Node(altitude)

			if x > 0:
				left = row[x-1]
				node.add_adjacent(left)
				left.add_adjacent(node)

			if y > 0:
				upper = rows[y-1][x]
				node.add_adjacent(upper)
				upper.add_adjacent(node)

	flat = [item for sublist in rows for item in sublist] # googled how to
	[node.remove_unvisitable_adjacents() for node in flat]

	first_node = flat[0]
	last_node = flat[-1]
	last_node.is_destination = True

	return first_node

# visit recursively and return possible paths' count within its trials
def visit(node, path):
	if node in path:
		return 0
	path.append(node)
	if node.is_destination:
		# found possible path
		path.remove(node)
		return 1
	count = 0
	for i in range(0, len(node.adjacents)):
		adjacent = node.adjacents[i]
		count += visit(adjacent, path)
	# dead end
	path.remove(node)
	return count


if __name__ == '__main__':

	raw = '5 3\n\
	22 22 22 11 11\n\
	22 22 22 11 11\n\
	11 11 22 22 22'

	first_node = parse_and_get_first_node(raw)

	path = []
	count = visit(first_node, path)

	print (count)
