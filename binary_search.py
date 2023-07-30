import numpy as np
import math

import logging
from typing import List, Callable, Union
import timeit

logging.basicConfig(level=logging.INFO, format="[{asctime}] - {funcName} - {lineno} - {message}", style='{')
logger = logging.getLogger("grokking")


def calculate_elapsed_time(in_func: Callable)-> Callable:
    def calculate_timer(*args, **kwargs)-> int:
        start = timeit.default_timer()
        steps, value = in_func(*args)
        end = timeit.default_timer()
        elapsed_time = end-start

        return steps, value, elapsed_time
    
    return calculate_timer

@calculate_elapsed_time
def linear_search(input_number_array:List[int], search_for_this_number:int)->Union[int,str]:
    try:
        number_of_steps = 0
        for number in input_number_array:
            number_of_steps += 1
            if number == search_for_this_number:
                return number_of_steps, "Found"
            
        return number_of_steps, "Not Found"

    except Exception as error:
        raise error

@calculate_elapsed_time
def binary_search(input_number_array:List[int], search_for_this_number:int)->Union[int,str]:
    try:
        # keep track of which part of the list you'll search in.
        low = 0
        high = len(input_number_array)-1
        number_of_steps = 0

        while low <= high :
            number_of_steps += 1
            mid = math.floor((low + high)/2)    # check the middle element.
            guess = input_number_array[mid]

            if guess == search_for_this_number:
                return number_of_steps, "Found"

            if guess > search_for_this_number :
                high = mid - 1            
            else:
                low = mid + 1
        return number_of_steps, "Not Found"
    except Exception as error:
        raise error

if __name__ == "__main__":
    try:
        logger.info("Binary Search Grokking starts")

        logger.info("Generate random numbers array")

        random_int_array = np.sort(np.random.choice(np.arange(1,101), size=20, replace=False)).tolist()
        
        logger.info(f"Random Number Array : \n {random_int_array}")

        search_for_this_number = int(input("Enter a number between 1 and 100 to search :"))

        number_of_steps, result, time_taken = binary_search(random_int_array, search_for_this_number)
        logger.info(f"Binary Search Result : {search_for_this_number} is {result} , took {number_of_steps} steps and this took {time_taken:.10f} seconds")

        number_of_steps, result, time_taken = linear_search(random_int_array, search_for_this_number)
        logger.info(f"Linear Search Result : {search_for_this_number} is {result} , took {number_of_steps} steps and this took {time_taken:.10f} seconds")
    except Exception as error:
        logger.error(f"{type(error).__name__} - {error}")