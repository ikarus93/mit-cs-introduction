def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    def count_element(l, e):
      return len([x for x in l if x == e]) % 2 != 0
    seq = [x for x in L if count_element(L, x)]
    if seq:
      return max(seq)
    else:
      return None