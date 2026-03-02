import networkx as nx
import matplotlib.pyplot as plt

def build_relationships():

    relationships = [
        ("CFPNC_2026", "instance", "FootballUS"),
        ("Miami_Hurricanes", "instance", "SportsTeam"),
        ("Indiana_Hoosiers", "instance", "SportsTeam"),
        ("20_January_2026", "instance", "Day"),
        ("27", "instance", "NonnegativeInteger"),
        ("21", "instance", "NonnegativeInteger"),
        ("Carson_Beck", "instance", "Man"),
        ("Miami_Hurricanes", "lost", "CFPNC_2026"),
        ("Indiana_Hoosiers", "won", "CFPNC_2026"),
        ("20_January_2026", "is_date", "CFPNC_2026"),
        ("27", "winning_score", "CFPNC_2026"),
        ("21", "losing_score", "CFPNC_2026"),
        ("Carson_Beck", "contestParticipant", "CFPNC_2026"),
        ("Carson_Beck", "member", "Miami_Hurricanes"),
        ("FootballUS", "subclass", "TeamSport"),
        ("TeamSport", "subclass", "Sport"),
        ("Sport", "subclass", "Game"),
        ("Game", "subclass", "RecreationOrExercise"),
        ("RecreationOrExercise", "subclass", "IntentionalProcess"),
        ("IntentionalProcess", "subclass", "Process"),
        ("Process", "subclass", "Physical"),
        ("Physical", "subclass", "Entity"),
        ("SportsTeam", "subclass", "Organization"),
        ("Organization", "subclass", "Group"),
        ("Group", "subclass", "Agent"),
        ("Agent", "subclass", "Object"),
        ("Object", "subclass", "Physical"),
        ("Day", "subclass", "TimeInterval"),
        ("TimeInterval", "subclass", "TimeMeasure"),
        ("TimeMeasure", "subclass", "ConstantQuantity"),
        ("ConstantQuantity", "subclass", "PhysicalQuantity"),
        ("PhysicalQuantity", "subclass", "Quantity"),
        ("Quantity", "subclass", "Abstract"),
        ("Abstract", "subclass", "Entity"),
        ("NonnegativeInteger", "subclass", "Integer"),
        ("Integer", "subclass", "RationalNumber"),
        ("RationalNumber", "subclass", "RealNumber"),
        ("RealNumber", "subclass", "Number"),
        ("Number", "subclass", "Quantity"),
        ("Man", "subclass", "Human"),
        ("Human", "subclass", "Hominid"),
        ("Hominid", "subclass", "Primate"),
        ("Primate", "subclass", "Mammal"),
        ("Mammal", "subclass", "WarmBloodedVertebrate"),
        ("WarmBloodedVertebrate", "subclass", "Vertebrate"),
        ("Vertebrate", "subclass", "Animal"),
        ("Animal", "subclass", "Organism"),
        ("Organism", "subclass", "OrganicObject"),
        ("OrganicObject", "subclass", "CorpuscularObject"),
        ("CorpuscularObject", "subclass", "SelfConnectedObject"),
        ("SelfConnectedObject", "subclass", "Object"),
    ]

    return relationships

def create_KG(relationships):

    graph = nx.DiGraph()

    for relationship in relationships:
        source = relationship[0]
        target = relationship[2]
        relation = relationship[1]
        graph.add_node(source)
        graph.add_node(target)
        graph.add_edge(source, target, relation=relation, weight=1)

    return graph

def draw_KG(graph, source_node, filename):

    instance_nodes = ["CFPNC_2026", "Miami_Hurricanes", "Indiana_Hoosiers",
                      "20_January_2026", "27", "21", "Carson_Beck"]

    node_colors = []
    for node in graph.nodes:
        if node == "Entity":
            node_colors.append('lightcoral')
        elif node in instance_nodes:
            node_colors.append('lightyellow')
        elif node == source_node:
            node_colors.append('lightgreen')
        else:
            node_colors.append('lightblue')

    position = nx.spring_layout(graph, seed=42, k=2.5, iterations=100)
    plt.figure(figsize=(24, 20))

    nx.draw_networkx_nodes(graph, position, node_size=2000, node_color=node_colors)
    nx.draw_networkx_labels(graph, position, font_size=6, font_color='black')

    edge_labels = nx.get_edge_attributes(graph, 'relation')
    nx.draw_networkx_edges(graph, position, edge_color='black', arrows=True,
                           arrowsize=15, min_target_margin=22)
    nx.draw_networkx_edge_labels(graph, position, edge_labels=edge_labels, font_size=5)

    plt.title("CFPNC 2026 Ontological Knowledge Graph (SUMO)", fontsize=16)
    plt.tight_layout()
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {filename}")

def run_dijkstra(graph, source_node):

    distances, paths = nx.single_source_dijkstra(graph, source=source_node)
    for target_node, path in paths.items():
        if target_node != source_node:
            print(f"\nPath from {source_node} to {target_node}:")
            for node_index in range(len(path) - 1):
                source, sink = path[node_index], path[node_index+1]
                relationship = graph[source][sink]['relation']
                print(f"{source} --{relationship}--> ", end='')
            print(f"{sink}")

def main():

    relationships = build_relationships()
    graph = create_KG(relationships)
    draw_KG(graph, "CFPNC_2026", "Football.png")
    run_dijkstra(graph, "CFPNC_2026")

    print("\n")

if __name__ == "__main__":
    main()