#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Tests that I passed on codility.com
#


def binary_gap(N):
    '''
    A binary gap within a positive integer N is any maximal
    sequence of consecutive zeros that is surrounded by ones
    at both ends in the binary representation of N.

    Args:
      - N: integer within the range [1..2,147,483,647]
    '''
    bin_rep = str(bin(N)[2:]) # Getting the binary representation
    y = bin_rep.split('1') 
    if y[len(y)-1] !='':
        y = y[:(len(y)-1)] # Fix trailing zeroes
    big = 0
    for i in y:
        if str(i).count('0') > big:
            big = str(i).count('0')
    return big

print binary_gap(1041)



def cyclic_rotation(A, K):
    '''
    A zero-indexed array A consisting of N integers is given. 
    Rotation of the array means that each element is shifted right by one index, 
    and the last element of the array is also moved to the first place.
    
    Args:
      - A: a list
      - N: integer within the range [1 ... 1000]    
    '''
    import collections
    d = collections.deque(A)
    d.rotate(K)
    return list(d)

print cyclic_rotation([1,2,3], 1)



def missing_element(A):
    '''
    A zero-indexed array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], 
    which means that exactly one element is missing. Your goal is to find that missing element.
    '''
    n = len(A)+1
    sum_calculated = n*(n+1)/2
    sum_actual = sum(A)
    return (sum_calculated - sum_actual)

print missing_element([2,3,1,5])



def count_div(A, B, K):
    '''
    Returns the number of integers within the range [A..B] that are divisible by K.

    Used generators to save memory on large amounts of data.

    Args:
      - A: is an integer within the range [0..2,000,000,000]
      - B: is an integer within the range [0..2,000,000,000] and A <= B
      - K: is an integer within the range [1..2,000,000,000]
    '''
    divs_count = 0
    for x in xrange(A, B + 1):
        if (x % K) == 0:
            divs_count += 1
    return divs_count

print count_div(1, 200000000, 1000)



def triangle(A):
    '''
    Calculate triangel of integers, where sentense of numbers P, Q, R
    correspond to next rules:
     - P + Q > R
     - Q + R > P
     - R + P > Q

    Args:
      - A: list of integers, where we will search triangle

    Return: 1 - if triangle exists, and 0 - otherwise
    '''
    A = tuple(enumerate(A))
    for p, P in A:
        for q, Q in A[p + 1:]:
            for r, R in A[q + 1:]:
                if (P + Q > R) and (Q + R > P) and (R + P > Q):
                    return 1 
    return 0

print triangle([10, 2, 5, 1, 8, 20])
