def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits sum is even".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    if (a%10+a//10)%2==0:
        return True
    return False
print(main(56))