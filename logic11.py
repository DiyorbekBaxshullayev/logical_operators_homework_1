def main(a):
    """
    Given integer a,  check the following statement "The integer is three-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    x = str(a)
    if len(x)==3:
        return True
    return False
print(main(652))