# it should retain all numbers within the specified range that contains the specified digit


def contains_digits(digit, range_of_numbers):
    if not isinstance(digit, int) or not isinstance(range_of_numbers, int):
        raise TypeError('input object must be an instance of integer')
    output = []
    if digit < 0 or digit > 9:
        raise Exception('digit argument must be from 0 to 9')

    for i in range(1, (range_of_numbers + 1)):
        for j in str(i):
            if int(j) == digit:
                output.append(i)
                break
            
        
   
       
    return output
