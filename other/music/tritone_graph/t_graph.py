import networkx as nx
import matplotlib.pyplot as plt
# Given a Cfullydim7 chord can resolve to Fmajor/Minor, AflatMajor/Minor
# B Major or monior, or Dflat Major or minor. So the 2, the 2sharp, the 4
# the 5 sharp, 7flat, 7
notes = {
    "C"     : 1,
    "Dflat" : 2,
    "D"     : 3,
    "Eflat" : 4,
    "E"     : 5,
    "F"     : 6,
    "Gflat" : 7,
    "G"     : 8,
    "Aflat" : 9,
    "A"     : 10,
    "Bflat" : 11,
    "B"     : 12,
}
class Node:
    num_reachable = []
    note_reachable = []
    note_to_num = {
        "C"     : 1,
        "Dflat" : 2,
        "D"     : 3,
        "Eflat" : 4,
        "E"     : 5,
        "F"     : 6,
        "Gflat" : 7,
        "G"     : 8,
        "Aflat" : 9,
        "A"     : 10,
        "Bflat" : 11,
        "B"     : 12,
    }
    num_to_note = {
        1  : "C",
        2  : "Dflat",
        3  : "D",
        4  : "Eflat",
        5  : "E", 
        6  : "F", 
        7  : "Gflat",
        8  : "G",
        9  : "Aflat",
        10 : "A",
        11 : "Bflat",
        12 : "B",
    }
    Note = ""
    def __init__(self, Note):
    # A node is a note. It connects to its defined above
        self.Note = Note
    def calc_adj_list(self):
        # Take the note letter, enumerate to a number.
        if len(self.num_reachable):
            return self.note_reachable, self.num_reachable
        num = self.note_to_num[self.Note]
        reachable = []
        for grab in [1, 2, 5, 8, 10, 11]:
            r = num+grab
            if r > 12: r-=12
            reachable.append(r)
        adj = []
        for elem in reachable:
            adj.append(self.num_to_note[elem])
        self.num_reachable = reachable
        self.note_reachable = adj
        return adj, reachable
# Build the Graph
G = nx.Graph()
for Note in notes.keys():
    M = Node(Note)
    G.add_node(Note)
    for elem in M.calc_adj_list()[0]:
        G.add_edge(Note, elem)
nx.draw_networkx_labels(G, pos=nx.spring_layout(G))
nx.draw(G)
plt.savefig("Graph.png")
