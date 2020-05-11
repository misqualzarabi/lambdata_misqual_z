 



def getmean(numbers):
  mean = sum(numbers)/ len(numbers)
  return mean
def getmedian(numbers):
  numbers.sort()
  mid = len(numbers)//2
  return(numbers[mid])
def getmode(numbers):
  mode = max(numbers , key = numbers.count)
  return mode
def meanmedianmode(numbers):
  mmm_dict = {'mean':getmean(numbers) , 'mode':getmode(numbers) , 'median':getmedian(numbers)}
  return mmm_dict
numbers = [1,3,10,3,8,6,4,3,9,7,3,8]
print("mean median mode" + str(meanmedianmode(numbers)))