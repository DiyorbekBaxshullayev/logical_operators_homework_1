def main(a):
    """
    Given integer a,  check the following statement "The integer is two-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    x = str(a)
    if len(x)==2:
        return True
    return False
print(main(165))