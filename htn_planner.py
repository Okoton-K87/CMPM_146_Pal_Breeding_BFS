import json

def load_breeding_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def decompose_task(pal, breeding_data, pets_we_have, task_list=None):
    if task_list is None:
        task_list = []
    
    print(f"Decomposing task for: {pal}")  # Debugging
    
    # If we already have the Pal, no need to breed it
    if pal in pets_we_have:
        print(f"Already have {pal}, no need to breed.")  # Debugging
        return task_list
    
    # Check if the Pal exists in the breeding results
    if pal not in breeding_data["results"]:
        raise ValueError(f"No breeding data available for {pal}")
    
    # Find the required parents to breed this Pal
    for parent_1 in breeding_data["parents"]:
        parent_1_name = breeding_data["parents"][parent_1]  # Get the parent name
        print(f"Trying parent_1: {parent_1} ({parent_1_name})")  # Debugging
        
        if parent_1 in breeding_data["results"][pal]:
            parent_2_key = breeding_data["results"][pal][parent_1]
            
            # Ensure parent_2_key is still a key, not a name
            if parent_2_key not in breeding_data["parents"].values():
                parent_2_name = breeding_data["parents"][parent_2_key]  # Get the second parent name
            else:
                parent_2_name = parent_2_key  # In case the logic provides a name directly
            
            print(f"Found valid parents: {parent_1_name} + {parent_2_name} -> {pal}")  # Debugging
            
            # Decompose the task to breed the parents first
            task_list = decompose_task(parent_1_name, breeding_data, pets_we_have, task_list)
            task_list = decompose_task(parent_2_name, breeding_data, pets_we_have, task_list)
            
            # Add the current breeding task
            task_list.append((parent_1_name, parent_2_name))
            break
        else:
            print(f"parent_1 {parent_1_name} not valid for breeding {pal}")  # Debugging
    
    return task_list



def create_htn_tree(pets_we_have, desired_pet, breeding_data):
    # Start with the desired pet and decompose the tasks
    return decompose_task(desired_pet, breeding_data, pets_we_have)

def find_best_path_htn(htn_tree):
    # The HTN tree already represents the sequence of actions to take
    # Simply return it as the best path
    return htn_tree
