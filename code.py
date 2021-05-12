"""
Pascals Triangle is usually given by the Combination (nCr) where n is the row number and r is the respective column number
"""

from math import factorial
n = 10
for i in range(n):
    for j in range(n-i+1):
  
        # for left spacing
        print(end=" ")
  
    for j in range(i+1):
  
        # nCr = n!/((n-r)!*r!)
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
    print()