'''Problem Statement : Power set in lexicographical order
   Approach used     : Sort the array first, after that fix characters one by one and then recursively generates all subsets from
   them.  '''

def permuteRecursively(string, n, index = -1, curr = ' '):
    if index == n:
        return
    
    if len(curr) > 0:
        print(curr)
    
    for i in range(index+1, n):
        curr += string[i]
        permuteRecursively(string, n, i, curr)
        curr = curr[:len(curr) - 1]

def powerset(string):
    string = ''.join(sorted(string))
    permuteRecursively(string, len(string))
if __name__ == '__main__':
    string = 'manvi'
    powerset(string)