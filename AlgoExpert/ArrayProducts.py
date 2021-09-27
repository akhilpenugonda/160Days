import math
def arrayOfProducts(array):
    numberOfZeros = 0
    product = math.prod(array)
    if(product == 0):
		if(array.count(0) > 1):
			return [0 for _ in range(len(array))]
    result = []
    if(product != 0):
		for i in array:
			result.append(product/i)
    else:
		product = 1
		for i in array:
			if(i != 0):
				product *= i
		for i in array:
			if(i==0):
				result.append(product)
			else: 
				result.append(0)
    return result


def arrayOfProducts(array):
    products = [1 for _ in range(len(array))]
    leftPoducts = 1
    for i in range(len(array)):
        products[i] = leftPoducts
        leftPoducts *= array[i]

    rightProducts = 1
    for i in reversed(range(len(array))):
        products[i] *= rightProducts
        rightProducts *= array[i]
    
    return products
        
