def main(n):
    """
    A number consisting of one and zero is given (the number starts at once). 
    If the number of ones is greater than zero, true, otherwise False is returned.
    
    Args:
        n(int): parameter n
    Returns:
        bool: answer
    """
    answer = 0
    m = n%10
    if m > 0 :
        answer = True
    else:
        answer = False
    return answer

print(main(10001))