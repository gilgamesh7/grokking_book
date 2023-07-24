import numpy as np

import logging

logging.basicConfig(level=logging.INFO, format="[{asctime}] - {funcName} - {lineno} - {message}", style='{')
logger = logging.getLogger("grokking")

if __name__ == "__main__":
    try:
        logger.info("Binary Search Grokking starts")

        logger.info("Generate random numbers array")

        random_int_array = np.sort(np.random.choice(np.arange(1,101), size=20, replace=False)).tolist()
        
        logger.info(f"Random Number Array : \n {random_int_array}")
    except Exception as error:
        logger.error(f"{type(error).__name__} - {error}")