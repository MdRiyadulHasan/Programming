def closestValue(root, target):
    closest = float("inf")
    while root:
        # Update closest if the current node is closer to the target
        if abs(root.val - target) < abs(closest - target):
            closest = root.val
        # Decide whether to go left or right
        if target < root.val:
            root = root.left
        else:
            root = root.right
    return closest
