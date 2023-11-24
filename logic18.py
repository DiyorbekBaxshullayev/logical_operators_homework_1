def main(a):
    """Given a five-digit integer a, check the following statement "All digits of the number are in descending order".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    answer = 0 #12345

    x=a%10
    a//=10

    y=a%10
    a//=10

    z=a%10
    a//=10

    k=a%10
    a//=10

    l=a%10
    
    if x<y and y<z and z<k and k<l:
        return False
    return True
print(main(95421))