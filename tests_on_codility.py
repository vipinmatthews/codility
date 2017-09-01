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


def oddOccurrence(A):
    '''
An array contains an odd number of elements, and each element of the array can be paired with another element 
that has the same value, except for one element that is left unpaired. Find the unpaired element.
    '''
    oddOne = 0
    for number in A:
        oddOne = oddOne ^ number
    return oddOne

print oddOccurrence([1,2,1])

def count_div(A, B, K):
    '''
    Returns the number of integers within the range [A,B] that are divisible by K.
    '''
    if A % K == 0:
        n = 1
    else:
        n = 0
    return (n + B/K - A/K)

print count_div(6, 11, 2)


def PermCheck(A):
    '''
A non-empty zero-indexed array A consisting of N integers is given.A permutation is a sequence containing 
each element from 1 to N once, and only once.  Check whether array A is a permutation.
'''
    Aset = set(A)
    for i in range(1,len(A)+1):
        if i not in Aset:
            return 0
    return 1

print PermCheck([4,1,3])


def FrogRiverOne(X, A):
    '''
    Find the earliest time when a frog can jump to the other side of a river. 
    '''
    y = set([i for i in range(1,X+1)])
    time = 0
    while len(y) > 0:
        if time < len(A):
            y.discard(A[time])
            time = time + 1
        else:
            return -1
    return time-1

print FrogRiverOne(5, [1, 3, 1, 4, 2, 3, 5, 4])



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
