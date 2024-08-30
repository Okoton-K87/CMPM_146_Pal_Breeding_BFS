import json
import time
from collections import deque
from binarytree import Node

def bfs(graph, initial_pals, target_pal, time_limit=3):
    """
    Performs BFS to find the shortest path to breed the target_pal, allowing for multiple instances of the same Pal.
    Terminates if the search exceeds the specified time limit.
    
    :param graph: The graph representing breeding paths
    :param initial_pals: The list of Pals the player currently has
    :param target_pal: The target Pal we want to reach
    :param time_limit: The time limit in seconds for the BFS search
    :return: A list of tuples representing the breeding path, or None if no path is found or if the search exceeds the time limit
    """
    start_time = time.time()  # Record the start time
    queue = deque([(initial_pals, [])])  # Queue stores (current_pals, path)
    visited = set()  # Track all visited states
    
    while queue:
        # Check if the time limit has been exceeded
        if time.time() - start_time > time_limit:
            print("Time limit exceeded. No path found.")
            return None
        
        current_pals, path = queue.popleft()
        current_state = tuple(sorted(current_pals))
        
        # Check if we've already visited this exact state
        if current_state in visited:
            continue
        
        visited.add(current_state)  # Mark this state as visited

        # Explore all possible breeding combinations within the current Pals
        for i, pal in enumerate(current_pals):
            for j, other_pal in enumerate(current_pals):
                if i != j:  # Ensure we're not breeding a Pal with itself
                    for other_parent, result in graph.get(pal, []):
                        if other_parent == other_pal:
                            new_path = path + [(pal, other_parent, result)]
                            new_pals = current_pals + [result]


                            print(f"Exploring: {pal} + {other_pal} = {result}, New Pals: {new_pals}")

                            # Check if we have reached the target
                            if result == target_pal:
                                print(f"Target reached with {new_path}")
                                return new_path

                            # Add the new state to the queue even if result is already in current_pals
                            queue.append((new_pals, new_path))
    
    print("No path found within the time limit.")
    return None  # No path found

def build_tree(path):
    path.reverse()
    node_list = []
    path[0] = tuple(reversed(path[0]))
    root = Node(path[0][0])
    root.left = Node(path[0][1])
    root.right = Node(path[0][2])
    node_list.append(root)
    node_list.append(root.left)
    node_list.append(root.right)
    if len(path) == 1:
        return root
    else:
        for i in range(1, len(path)):
            path[i] = tuple(reversed(path[i]))
            for node in node_list:
                if node.value == path[i][0]:
                    node.left = Node(path[i][1])
                    node.right = Node(path[i][2])
                    node_list.append(node.left)
                    node_list.append(node.right)

    return root

if __name__ == "__main__":
    with open('breeding_graph.json', 'r') as f:
        graph = json.load(f)
    
    # Example lists of pets the player currently has
    #initial_pals = ["Lamball", "Lifmunk"]
    
    # Example target Pals
    # target = "Jolthog"
    # target = "Gumoss"
    #target = "Nitewing"
    # target = "Blazehowl"  # Try getting Blazehowl from a pool of Gumoss, Tombat, and Nitewing

    initial_pals = ["Tombat", "Nitewing", "Gumoss"]  # Example list of pets the player currently has
    target = ["Blazehowl", "Vaelet"]  # Example target Pal
    tree_list = []
    for pal in target:
        path = bfs(graph, initial_pals, pal)
        if path:
            print("BFS Path:", " -> ".join([f"{p[0]} + {p[1]} = {p[2]}" for p in path]))
        else:
            print(f"No path found to breed {target} with the current Pals")
        tree = build_tree(path)
        tree_list.append(tree)
    for tree in tree_list:
        print(tree)
