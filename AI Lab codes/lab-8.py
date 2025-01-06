import matplotlib.pyplot as plt
import networkx as nx
class SimpleMultiGraph:
    def __init__(self):
        self.graph = {}
    def add_edge(self, from_node, to_node, label):
        if from_node not in self.graph:
            self.graph[from_node] = []
        self.graph[from_node].append((to_node, label))
    def has_path(self, start, end):
        visited = set()
        return self.dfs(start, end, visited)
    def dfs(self, current, target, visited):
        if current == target:
            return True
        visited.add(current)
        for neighbor, _ in self.graph.get(current, []):
            if neighbor not in visited:
                if self.dfs(neighbor, target, visited):
                    return True
        return False
paragraph = ["Ali is teacher.",
    "Teachers educate students.",
    "Students learn subjects.",
    "Subjects are important for exams.",
    "Ali teaches Math.",
    "Math helps students.",
    "Exams test subjects.",
    "Teachers prepare students for exams.",
    "Ali advises students.",
    "Students ask questions to teachers.",
    "Teachers review exams.",
    "Students practice Math for exams.",
    "Math improves problem-solving.",
    "Problem-solving helps in exams."]
G = nx.DiGraph()
multigraph = SimpleMultiGraph()
for sentence in paragraph:
    words = sentence.replace('.', '').split()
    if len(words) >= 3:
        subject = words[0]
        verb = words[1]
        obj = words[2]
        multigraph.add_edge(subject, obj, verb)
        G.add_edge(subject, obj, label=verb)
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=500, node_color='red', font_size=5, arrows=True)
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.axis('off')
plt.show()
print("Edges:")
for from_node in multigraph.graph:
    for to_node, label in multigraph.graph[from_node]:
        print(f"{from_node} --({label})--> {to_node}")
print("Path from 'Ali' to 'exams':", multigraph.has_path('Ali', 'exams'))
print("Path from 'Ali' to 'Math':", multigraph.has_path('Ali', 'Math'))
print("Path from 'Math' to 'students':", multigraph.has_path('Math', 'students'))