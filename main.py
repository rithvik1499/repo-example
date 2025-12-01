import random

def main() -> list[int]:
    """_summary_

    Returns:
        list[int]: _description_
        rtype: list[int]
    """

    random_list = [random.randint(0, 10) for i in range(7)]
    
    return random_list