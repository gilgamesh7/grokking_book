import numpy as np
import math

import logging
from typing import List, Callable
import timeit

logging.basicConfig(level=logging.INFO, format="[{asctime}] - {funcName} - {lineno} - {message}", style='{')
logger = logging.getLogger("grokking")


def calculate_elapsed_time(in_func: Callable)-> Callable:
    def calculate_timer(*args, **kwargs)-> int:
        start = timeit.default_timer()
        value = in_func(*args)
        end = timeit.default_timer()
        elapsed_time = end-start

        return value, elapsed_time
    
    return calculate_timer
    
@calculate_elapsed_time
def binary_search(input_number_array:List[int], search_for_this_number:int)->str:
    try:
        # keep track of which part of the list you'll search in.
        low = 0
        high = len(input_number_array)-1

        while low <= high :
            mid = math.floor((low + high)/2)    # check the middle element.
            print(mid, type(mid))
            guess = input_number_array[mid]

            if guess == search_for_this_number:
                return "Found"

            if guess > search_for_this_number :
                high = mid - 1            
            else:
                low = mid + 1
        return "Not Found"
    except Exception as error:
        raise error

if __name__ == "__main__":
    try:
        logger.info("Binary Search Grokking starts")

        logger.info("Generate random numbers array")

        random_int_array = np.sort(np.random.choice(np.arange(1,101), size=20, replace=False)).tolist()
        
        logger.info(f"Random Number Array : \n {random_int_array}")

        search_for_this_number = int(input("Enter a number between 1 and 100 to search :"))

        result, time_taken = binary_search(random_int_array, search_for_this_number)

        logger.info(f"Search Result : {search_for_this_number} is {result} in array {random_int_array} and this took {time_taken} seconds")
    except Exception as error:
        logger.error(f"{type(error).__name__} - {error}")