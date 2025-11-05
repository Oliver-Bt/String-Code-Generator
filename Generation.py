import random
import string
import itertools
from math import factorial
import time
import threading
from database import Database


class Code_generation:
    repetitions = 165,675,600
    length=6 
    unique=True 
    uppercase=True

    def __init__(self):
        self.db = Database()
     
    def RandomString(self):
        # """Generate `repetitions` random strings of `length` using uppercase letters by default.

        # If `unique` is True, ensure no string is output more than once. This will raise
        # ValueError if the requested number of unique strings exceeds the total possible
        # combinations for the chosen alphabet and length.
        # """
        # Choose alphabet based on uppercase flag
        repetitions = self.repetitions
        length = self.length
        unique = self.unique   
        uppercase = self.uppercase

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
            
            # Only store the paired version in the database
            self.db.insert_string(paired, length)

        # Report elapsed time
        end = time.time()
        time_elapsed = (end - _start)
        print("Time taken for", repetitions, "repetitions:", time_elapsed, "seconds")
        return seen
    #from Generation import Code_generation

    #gen = Code_generation()
    #gen.RandomString(length=6, repetitions=1000, unique=True, uppercase=True)

    # # To see what's in the database:
    # for row in gen.db.get_recent_strings(10):
    #     print(row)



        
  




    # def Start():
    #     value=0
    #     print(value)
    
    #     # Generate a random integer between 0 and 100
    #     print(random.randint(0, 25))

    #     # Generate a random float in [0.0, 1.0)
    #     print(random.random())

    #     # Reproducible example with a seed
    #     random.seed(42)
    #     print(random.randint(1, 10))



if __name__ == "__main__":
    gen = Code_generation()
    gen.RandomString()
