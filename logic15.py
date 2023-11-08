def main(a):
    """
    Given a three-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    if (a%10+(a%100)//10+a//100)%2==1:
        return True
    return False
print(main(300))