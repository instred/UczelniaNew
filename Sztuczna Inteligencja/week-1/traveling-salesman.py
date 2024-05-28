
import networkx as nx
from networkx.algorithms.approximation import traveling_salesman_problem
import matplotlib.pyplot as plt
import random
from typing import Tuple, List


"""
Autor: Jakub Bok
Projekt: rozwiązanie problemu komiwojażera (Travelling Salesman Problem)
Problem polega na znalezieniu jak najkrótszej ścieżki w kompletnym grafie, przechodząc przez wszystkie wierzchołki

Zdecydowałem się na użycie heurystyki, która wybiera ścieżkę chciwo (Greedy solution), to znaczy wybiera rozwiązanie lokalnie na podstawie minimum dostępnych wartości.
Do stworzenia grafu i przedstawienia tego procesu wybrałem bibliotekę networkx, która daje wiele przydatnych do tego narzędzi i ułatwia operacje na grafach.

Opis działania algorytmu:

Inicjalizuje kompletny graf z losowymi wagami z przedziału
Przechodzę po grafie, zaczynając i kończąc (dla uproszczenia) na pewnym wierzchołku startowym.
Przejście do następnego wierzchołka odbywa się na podstawie znalezienia najtańszej drogi z dostępnych lokalnie.
W trakcie przechodzenia, modyfikuję moją listę aktualnej trasy oraz wierzchołków pozostałych do przejścia.
Na koniec liczę cenę przejścia kompletnej trasy przez graf.
Po zakończeniu porównuje sobie mój algorytm do algorytmu aproksymacyjnego dostępnego w bibliotece networkx, który posiada pewną gwarantowaną jakość rozwiązania,
jednak dalej prawdopodobnie nie będzie to optymalne rozwiązanie

Rozwiązanie za pomocą tej heurystyki nie jest rozwiązaniem optymalnym, jest podobne do aproksymacji, ale bez gwarancji jakości,
jednak daje nam możliwość rozwiązania tego problemu dobrze, w sensownym czasie.
Algorytmy optymalne zwykle posiadają złożoność wykładniczą

Komentarze do kodu zostawiam w języku angielskim - prosiłbym o informację jeżeli będzie to stanowić problem.

"""




# Using networkx I can generate a complete graph with n nodes with simple function:
def generate_complete_graph(num_nodes: int, weight_range: Tuple[int]=(1,100)) -> nx.classes.graph.Graph:
    G = nx.complete_graph(num_nodes)

    # Using the weight range I assign weight for each edge in graph randomly
    for u, v in G.edges():
        G.edges[u, v]['weight'] = random.randint(*weight_range)

    return G


# Function for plotting actuall progress of the algorithm
def plot_graph(G: nx.classes.graph.Graph, tour: List[int], curr_node: int, pos) -> None:
    plt.clf()
    nx.draw(G, pos, with_labels=True, node_color='blue', node_size=500)

    # List of all connections in graph
    path_edges = list(zip(tour, tour[1:]))
    
    # Drawing functions
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='green', width=3)
    nx.draw_networkx_nodes(G, pos, nodelist=[curr_node], node_color='red', node_size=500)

    # Adding labels
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Pause so we can see the animation of the path
    plt.pause(0.4)



# Simple function to calculate the final path cost
def calculate_cost(G: nx.classes.graph.Graph, tour: List[int]) -> int:
    return sum(G[tour[i]][tour[i+1]]['weight'] for i in range(len(tour) - 1))


# Main algorithm for the heuristics
def nearest_neighbour_heuristics(G: nx.classes.graph.Graph, start_node: int = None) -> None:

    # Starting node can be None by default if user doesn't give starting point so we assign start randomly if so
    if not start_node:
        start_node = random.choice(list(G.nodes()))

    # Creating a layout for graph plotting so it doesn't change during the tour
    pos = nx.spring_layout(G)
    plt.ion()
    plt.show()

    # Creating unvisited nodes set
    unvisited = set(G.nodes)
    unvisited.remove(start_node)

    # Creating a list with out actuall path
    tour = [start_node]
    curr_node = start_node

    plot_graph(G, tour, curr_node, pos)

    # As long as we have unvisited nodes, we iterate and choose the next node by local minimum
    while unvisited:
        next_node = min(unvisited, key=lambda node: G[curr_node][node]['weight'])
        unvisited.remove(next_node)
        tour.append(next_node)
        curr_node = next_node
        plot_graph(G, tour, curr_node, pos)

    tour.append(start_node)
    plot_graph(G, tour, curr_node, pos)

    # In the end, we print the tour and the cost of it 
    print(tour)
    tour_cost = calculate_cost(G, tour)
    print(f'Heuristics function cost: {tour_cost}')

    plt.ioff()
    plt.show()



if __name__ == '__main__':

    # Comparing the two algorithms
    G = generate_complete_graph(8)
    nearest_neighbour_heuristics(G)

    approx_tour = traveling_salesman_problem(G, cycle=True)
    approx_tour_cost = calculate_cost(G, approx_tour)

    print(approx_tour)
    print(f'Approximation function cost: {approx_tour_cost}')