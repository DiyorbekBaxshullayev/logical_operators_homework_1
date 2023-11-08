#def main(a):
"""
    Given a two-digit integer a,  check the following statement "All digits of the number are the same".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
#    x = str(a)
#    return x[0]==x[1]
#print(main(22))

def main(a):
    if a%10==a//10:
        return True
    return False
print(main(55))