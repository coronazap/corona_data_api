def split_array(array, size): 
    # Splits an array into multiples arrays of size "size" 
    arrays = [] 
    while len(array) > size: 
        piece = array[:size] 
        arrays.append(piece) 
        array = array[size:] 
    arrays.append(array)
    return arrays


def clear_data(array): 
    # Remove linebreaks and empty spaces from array 
    new_array = [] 
    for i, item in enumerate(array):
        
        if '\n' not in item: 
            # Remove empty spaces from cell value 
            new_array.append(item.replace(' ', '')) 
        elif '\n' in item and '\n' in array[i - 1]:
            if i < len(array) - 1 and 'Total' not in array[i + 1]: 
                new_array.append('0')
    return new_array

def empty_for_zero(array): 
    new_array = []
    for item in array: 
        if item == '': 
            new_array.append('0') 
        else: 
            new_array.append(item)             
    return new_array