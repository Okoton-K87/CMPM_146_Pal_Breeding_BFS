import json
from collections import deque

def bfs(graph, initial_pals, target_pal):
    """
    Performs BFS to find the shortest path to breed the target_pal.
    
    :param graph: The graph representing breeding paths
    :param initial_pals: The list of Pals the player currently has
    :param target_pal: The target Pal we want to reach
    :return: A list of tuples representing the breeding path, or None if no path is found
    """
    queue = deque([(initial_pals, [])])  # Queue stores (current_pals, path)
    visited = set(tuple(initial_pals))  # Track all visited combinations of Pals
    
    while queue:
        current_pals, path = queue.popleft()
        print(f"Current Pals: {current_pals}, Path so far: {path}")
        
        # Explore all possible breeding combinations within the current Pals
        for i, pal in enumerate(current_pals):
            for j, other_pal in enumerate(current_pals):
                if i != j:  # Ensure we're not breeding a Pal with itself
                    for other_parent, result in graph.get(pal, []):
                        if other_parent == other_pal and result not in current_pals:
                            new_path = path + [(pal, other_parent, result)]
                            new_pals = current_pals + [result]
                            if tuple(new_pals) in visited:
                                continue
                            print(f"Exploring: {pal} + {other_pal} = {result}, New Pals: {new_pals}")

                            if result == target_pal:
                                print(f"Target reached with {new_path}")
                                return new_path

                            if tuple(new_pals) not in visited:
                                visited.add(tuple(new_pals))
                                queue.append((new_pals, new_path))
    
    return None  # No path found

if __name__ == "__main__":
    with open('breeding_graph.json', 'r') as f:
        graph = json.load(f)
    
    #initial_pals = ["Lamball", "Lifmunk", "Chikipi", "Flambelle"]  # Example list of pets the player currently has
    #target = "Cremis"  # Example target Pal

     # try getting Blazehowl from a pool of Gumoss, Tombat, and Nitewing.
    initial_pals = ["Gumoss", "Tombat", "Nitewing"]  # Example list of pets the player currently has
    target = "Blazehowl"  # Example target Pal
    
    path = bfs(graph, initial_pals, target)
    if path:
        print("BFS Path:", " -> ".join([f"{p[0]} + {p[1]} = {p[2]}" for p in path]))
    else:
        print(f"No path found to breed {target} with the current Pals")
