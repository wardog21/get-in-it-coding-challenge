import json

start_node = "Erde"
target_node = "b3-r7-r4nd7"
generated_graph_file = "generatedGraph.json"

generated_graph = open(generated_graph_file, "r")
graph = json.loads(generated_graph.read())
generated_graph.close()
nr_of_nodes = len(graph["nodes"])

nodes = []
route = []
edges = []
costs = []

for i in range(nr_of_nodes):
	nodes.append(None)
	route.append(None)
	edges.append([])
	costs.append([])
	if graph["nodes"][i]["label"] == start_node:
		start_node = i
	elif graph["nodes"][i]["label"] == target_node:
		target_node = i

for edge in graph["edges"]:
	edges[edge["source"]].append(edge["target"])
	edges[edge["target"]].append(edge["source"])
	costs[edge["source"]].append(edge["cost"])
	costs[edge["target"]].append(edge["cost"])

current_set = []
current_set.append(start_node)
nodes[start_node] = 0.1
route[start_node] = None

while current_set:
	my_node = current_set.pop(0)
	for node, cost in zip(edges[my_node], costs[my_node]):
		if not nodes[node]:
			nodes[node] = nodes[my_node] + cost
			route[node] = my_node
			current_set.append(node)

		elif (nodes[my_node] + cost) < nodes[node]:
			nodes[node] = nodes[my_node] + cost
			route[node] = my_node
			current_set.append(node)
			
my_route = []
current_route = target_node

while current_route:
	my_route.append(current_route)
	current_route = route[current_route]

planets = []

for node in list(reversed(my_route)):
	planets.append(graph["nodes"][node]["label"])

print("Route:", planets, " Gesamtentfernung:", (nodes[target_node]-nodes[start_node]))