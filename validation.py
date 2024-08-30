import json

def load_breeding_data(file_path):
    """
    Load breeding data from a JSON file.

    :param file_path: Path to the JSON file
    :return: Dictionary containing the breeding data
    """
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def validate_pals(pals, breeding_data):
    """
    Validate that all given Pals are present in the breeding data.

    :param pals: List of Pals to validate
    :param breeding_data: Dictionary containing the breeding data
    :return: Tuple (is_valid, invalid_pals)
             - is_valid: True if all Pals are valid, False otherwise
             - invalid_pals: List of Pals that are not found in the breeding data
    """
    parents = breeding_data.get('parents', {})
    invalid_pals = [pal for pal in pals if pal not in parents.values()]

    return len(invalid_pals) == 0, invalid_pals

# Example usage:
if __name__ == "__main__":
    breeding_data = load_breeding_data('breeding_data.json')
    pals_to_check = ["Lamball", "FakePal", "Kitsun"]
    is_valid, invalid_pals = validate_pals(pals_to_check, breeding_data)

    if is_valid:
        print("All Pals are valid.")
    else:
        print(f"Invalid Pals found: {invalid_pals}")
