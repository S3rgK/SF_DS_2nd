"""
'Guess-a-number' game - machine thinks and guesses a number by itself
"""

import numpy as np

def random_predict(number:int=1) -> int:
    
    """
    Randomly guessing a number
    Args:
        number (int, optional) - number made, defaults to 1
    Returns:
        int - number of attempts
    """
    count = 0
    
    while True:
        count += 1
        predicted_number = np.random.randint(1, 101) #estimated number
        if number == predicted_number:
            break #quitting the cycle when we made a right guess
    return(count)


# test run print(f'Number of attempts: {random_predict()}')

def game_score(random_predict) -> int:
    
    """
    Average number of attempts, made by function random_predict to guess a number
    Args:
        random_predict ([type]): function for guessing a number
    Returns:
        int: average number of attempts
    """
    
    attempts_lst = [] # list for storing number of attempts
    np.random.seed(1) # securing the seed for reproducibility
    random_array = np.random.randint(1, 101, size = (10000)) # making a list of numbers
    
    for number in random_array:
        attempts_lst.append(random_predict(number))
    
    score = int(np.mean(attempts_lst)) # finding average number of attempts
    
    print (f'Your algoritm guesses a number for {score} attempts (average)')
    return score

# RUN
if __name__ == '__main__':
    game_score(random_predict)
    

