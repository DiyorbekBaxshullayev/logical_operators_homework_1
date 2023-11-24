def main(x):
    """
    Given an integer x, return true if x is palindrome integer.
    An integer is a palindrome when it reads the same backward as forward.

    Args:
        x(int): parameter x
    Returns:
        bool: answer
    """
    if x>9 and x<100:
        a=x%10
        b=x//10
        X=a*10+b
    if x>99 and x<1000:
        a=x%10
        b=(x//10)%10
        c=x//100
        X=a*100+b*10+c
    return X==x
print(main(151))