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
def RandomString(length):

    letters = string.ascii_uppercase
    i=0
    repetitions = 200,000
    _start=0.0
    _start = time.time()

    for i in range(i, repetitions ):
        
        result_str = ''.join(random.choice(letters) for i in range(length))
        # divide into pairs separated by dashes, last group may be single if length is odd
        paired = '-'.join(result_str[i:i+2] for i in range(0, len(result_str), 2))
        #pairs = [result_str[i:i+2] for i in range(0, len(result_str), 2)]
        print("Random string of length", length, "is:", result_str)
        print("Paired string:", paired)
        i+=1
    end= time.time()
    #print(end)
    time_elapsed = (end - _start)
    print("Time taken for", repetitions, "repetitions:", time_elapsed, "seconds")


          # for pair in pairs:
          #print(pair)


RandomString(6)




def count_permutations(n, k):
    if k > n:
        return 0
    return factorial(n) // factorial(n - k)

def generate_all_unique_strings(length, output_path=None, uppercase=True, max_allowed=1_000_000_000):
    """
    Generate every possible string of given `length` from the alphabet without repeating characters.
    - If output_path is provided, writes one string per line to that file.
    - Otherwise returns a generator (do not iterate it if the count is huge).
    - Safety: if total permutations > max_allowed, raises ValueError to avoid excessive work.
    """
    alphabet = string.ascii_uppercase if uppercase else string.ascii_lowercase
    n = len(alphabet)
    total = count_permutations(n, length)
    if total == 0:
        raise ValueError("length is greater than alphabet size")
    if total > max_allowed:
        raise ValueError(f"Too many permutations ({total}). Increase max_allowed if you really want to proceed.")

    perms = (''.join(p) for p in itertools.permutations(alphabet, length))
    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            for s in perms:
                      f.write(s + '\n')
        return total
    return perms 

#count_permutations(26, 6)
