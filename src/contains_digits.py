# it should retain all numbers within the specified range that contains the specified digit


def contains_digits(digit, range_of_numbers):
    if not isinstance(digit, int) or not isinstance(range_of_numbers, int):
        raise TypeError('input object must be an instance of integer')
    output = []
 

    for i in range(1, (range_of_numbers + 1)):
        for j in str(i):
            if int(j) == digit:
                output.append(i)
                break
            
        
   
       
    return output

