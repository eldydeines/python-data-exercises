def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num_1 = list(str(num1))
    num_2 = list(str(num2))
    digits = set(str(num1)) & set(str(num2))
  
    for digit in digits:
        
        digit1 = num_1.count(digit)
        digit2 = num_2.count(digit)

        if digit1 != digit2:
            return False
   
    return True
  