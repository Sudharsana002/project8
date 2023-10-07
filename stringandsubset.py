import itertools

def generate_subsets(N, strings):
    subsets = []
    
    # Rank 1 is always an empty set.
    subsets.append([])
    
    # Add individual strings as subsets.
    for string in strings:
        subsets.append([string])
    
    # Generate all possible combinations of strings.
    for r in range(2, N + 1):
        combinations = itertools.combinations(strings, r)
        for combo in combinations:
            subset = list(combo)
            
            # Check if the subset is a legal combination.
            is_legal = True
            for i in range(len(subset) - 1):
                if strings.index(subset[i]) > strings.index(subset[i + 1]):
                    is_legal = False
                    break
            
            if is_legal:
                subsets.append(subset)
    
    return subsets

# Input
N = int(input())
R = int(input())
strings = input().split(',')

subsets = generate_subsets(N, strings)

# Sort subsets based on the given rules.
subsets.sort(key=lambda subset: (len(subset), [strings.index(s) for s in subset]))

# Find the Rth subset and print it.
result = ','.join(subsets[R - 1])
print(result)