def egg_drop_recursive(eggs, floors):
    # Base cases
    if eggs == 1:
        return floors
    if floors == 0 or floors == 1:
        return floors

    min_drops = float('inf')

    # Consider dropping the egg from each floor and find the worst case
    for i in range(1, floors + 1):
        # If egg breaks, search in lower floors with one less egg
        breaks = egg_drop_recursive(eggs - 1, i - 1)
        # If egg doesn't break, search in upper floors with the same number of eggs
        doesn_break = egg_drop_recursive(eggs, floors - i)

        # Find the maximum in the worst case
        worst_case = max(breaks, doesn_break)

        # Update the minimum drops
        min_drops = min(min_drops, worst_case)

    # Add 1 for the current drop
    return 1 + min_drops

# Example usage:
eggs = 2
floors = 10

result = egg_drop_recursive(eggs, floors)
print(f"Minimum drops needed: {result}")
