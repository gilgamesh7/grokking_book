import numpy as np

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
def binary_search(array:List[int], search_for_this_number:int)->str:
    return "Found"

if __name__ == "__main__":
    try:
        logger.info("Binary Search Grokking starts")

        logger.info("Generate random numbers array")

        random_int_array = np.sort(np.random.choice(np.arange(1,101), size=20, replace=False)).tolist()
        
        logger.info(f"Random Number Array : \n {random_int_array}")

        search_for_this_number = input("Enter a number between 1 and 100 to search :")

        result, time_taken = binary_search(random_int_array, search_for_this_number)

        logger.info(f"Search Result : {search_for_this_number} is {result} in array {random_int_array} and this took {time_taken} seconds")
    except Exception as error:
        logger.error(f"{type(error).__name__} - {error}")