import random
import string
import itertools
from math import factorial
import time
import threading

def Start():
    value=0
    print(value)
    
    # Generate a random integer between 0 and 100
    print(random.randint(0, 25))

    # Generate a random float in [0.0, 1.0)
    print(random.random())

    # Reproducible example with a seed
    random.seed(42)
    print(random.randint(1, 10))


# def RandomLetter():
#     letters = 'abcdefghijklmnopqrstuvwxyz'
#     j=0
#     for i in range(6):
#         j = random.choice(letters)
#         j=j+1
#         i=i+1    
#     print(''.join(j))

# RandomLetter()
def RandomString(length, repetitions=1000, unique=True, uppercase=True):
    # """Generate `repetitions` random strings of `length` using uppercase letters by default.

    # If `unique` is True, ensure no string is output more than once. This will raise
    # ValueError if the requested number of unique strings exceeds the total possible
    # combinations for the chosen alphabet and length.
    # """
    # Choose alphabet based on uppercase flag
    alphabet = string.ascii_uppercase if uppercase else string.ascii_lowercase

    # Total number of possible strings of given length (with repetition allowed)
    total_possible = len(alphabet) ** length

    # Safety check: if caller requests more unique strings than possible, fail early
    if unique and repetitions > total_possible:
        raise ValueError(
            f"Requested {repetitions} unique strings, but only {total_possible} possible for length={length}"
        )

    # Track already-produced strings when uniqueness is required
    seen = set()

    # Start timing so caller can see how long generation took
    _start = time.time()

    # Continue generating until we have produced the requested number of strings
    # When `unique` is True we skip any repeat that was already generated.
    while len(seen) < repetitions:
        # Build a candidate string by sampling alphabet with replacement
        result_str = ''.join(random.choice(alphabet) for _ in range(length))

        if unique:
            # If it's a duplicate, skip and generate another candidate
            if result_str in seen:
                continue
            # Otherwise record it and proceed to output
            seen.add(result_str)
        else:
            # When duplicates are allowed we still add to `seen` so the
            # loop termination condition can be based on `repetitions`.
            seen.add(result_str)

        # Optionally present the string in paired groups for readability
        paired = '-'.join(result_str[j:j+2] for j in range(0, len(result_str), 2))
        print("Random string of length", length, "is:", result_str)
        print("Paired string:", paired)

    # Report elapsed time
    end = time.time()
    time_elapsed = (end - _start)
    print("Time taken for", repetitions, "repetitions:", time_elapsed, "seconds")



RandomString(6)














# def count_permutations(n, k):
#     if k > n:
#         return 0
#     return factorial(n) // factorial(n - k)

# def generate_all_unique_strings(length, output_path=None, uppercase=True, max_allowed=1_000_000_000):
#     """
#     Generate every possible string of given `length` from the alphabet without repeating characters.
#     - If output_path is provided, writes one string per line to that file.
#     - Otherwise returns a generator (do not iterate it if the count is huge).
#     - Safety: if total permutations > max_allowed, raises ValueError to avoid excessive work.
#     """
#     alphabet = string.ascii_uppercase if uppercase else string.ascii_lowercase
#     n = len(alphabet)
#     total = count_permutations(n, length)
#     if total == 0:
#         raise ValueError("length is greater than alphabet size")
#     if total > max_allowed:
#         raise ValueError(f"Too many permutations ({total}). Increase max_allowed if you really want to proceed.")

#     perms = (''.join(p) for p in itertools.permutations(alphabet, length))
#     if output_path:
#         with open(output_path, 'w', encoding='utf-8') as f:
#             for s in perms:
#                       f.write(s + '\n')
#         return total
#     return perms 

#count_permutations(26, 6)
