def main(a):
    """
    Given a five-digit integer a,  check the following statement "All digits of the number are in ascending order".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    x = a//10000
    y = (a-x*10000)//1000
    z = (a-(x*10000+y*1000))//100
    k = (a%100)//10
    l = (a%10)

    if x<y and y<z and z<k and k<l:
        return False
    return True
print(main(75421))