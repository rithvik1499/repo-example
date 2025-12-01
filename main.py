import random
from bs import binary_search

def main() -> list[int]:
    """_summary_

    Returns:
        list[int]: _description_
        rtype: list[int]
    """

    random_list = [random.randint(0, 10) for i in range(7)]
    index = binary_search(sorted(random_list), 5)
    print(f"Index of 5 in sorted list: {index}")
    return random_list