from htn_planner import load_breeding_data, create_htn_tree, find_best_path_htn

def get_available_breeds(pets_we_have, breeding_data):
    # Determine which pets can be bred
    available_breeds = []
    for pet in pets_we_have:
        if pet in breeding_data["results"]:
            available_breeds.extend(breeding_data["results"][pet].values())
    return list(set(available_breeds))

def find_optimal_breeding_path(pets_we_have, desired_pet=None):
    breeding_data = load_breeding_data("breeding_data.json")
    
    htn_tree = create_htn_tree(pets_we_have, desired_pet, breeding_data)
    return find_best_path_htn(htn_tree)
