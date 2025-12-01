def binary_search(data, target):
    """
    Searches for a target value in a SORTED list using the binary search algorithm.

    Args:
        data (list): A list of elements, which MUST BE SORTED.
        target: The value (integer) to search for.

    Returns:
        int: The index of the target element if found, or -1 if the target is not in the list.
    """
    
    # Initialize the search boundaries
    low = 0
    high = len(data) - 1
    
    # Keep searching as long as the search space is valid (low <= high)
    while low <= high:
        # Calculate the middle index
        # We use // for integer division
        mid = (low + high) // 2
        
        # Check if the middle element is the target
        if data[mid] == target:
            return mid  # Target found!
        
        # If the middle element is less than the target,
        # the target must be in the right half. Adjust 'low' to mid + 1.
        elif data[mid] < target:
            low = mid + 1
            
        # If the middle element is greater than the target,
        # the target must be in the left half. Adjust 'high' to mid - 1.
        else: # data[mid] > target
            high = mid - 1
            
    # If the loop completes, the target was not found
    return -1