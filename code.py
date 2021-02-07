def fib(n, memo= {}):
    
    if n in memo:
        return memo[n]
    if n <=2:
        return 1
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]
    

fb_0 = fib(0)   
fb_1 = fib(1)
fb_2 = fib(6)
fb_3 = fib(50)

def grid_traveler(row, cols, memo = {}):
    
    x = row, cols
    if x in memo:
        return memo[x]
    
    if row == 1 or cols == 1:
        return 1
    
    memo[x] =grid_traveler(row-1, cols) + grid_traveler(row, cols-1)
    
    return memo[x]


gd_1 = grid_traveler(1,1)
gd_2 = grid_traveler(2,3)
gd_3 = grid_traveler(3,2)
gd_4 = grid_traveler(3,3)
gd_5 = grid_traveler(15,15)



def sum_match(target_sum, arr, memo= {}):
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    for ele in arr:
        remiander = target_sum - ele
        result = sum_match(remiander, arr, memo)
        if result is not None:
            memo[target_sum] = result + [ele]
            return memo[target_sum]
    memo[target_sum] = None
    
    return None




sm1 = sum_match(100,[1,4])
print(sm1)


import heapq

arr = [ [1, 3, 5, 7], [2, 4, 6, 8], [0, 9, 10, 11]] 

k = 3
n = 4
l = 0
m = 0
lst = []
k_n = []

while(l < n):
    for x in range(0,k):
        heapq.heappush(k_n,arr[x][l])
    l +=1
    lst.append(heapq.heappop(k_n))

for x in range(0, (k-1)*n):
    lst.append(heapq.heappop(k_n))


print(lst)
print(k_n)







def anagram(arr, arr2):
    

    if (len(arr) != len(arr2)):
        return False
    
    m = {}
    
    for x in arr:
        if x not in m:
            m[x] = 1
        else:
            m[x] +=1
    ##{'c':1, 't':1, 'a':2}
    
    for y in arr2:
        if y in m:
            m[y] -=1
    
    ## {'c':0, 't':0, 'a':0}
            
    for _,v in m.items():
        
        if v !=0:
            return False
    return True



def anagram(str1, str2):
    
    if not str1 and  not str2:
        return False
    
    if len(str1) != len(str2):
        return False
    
    count = 0

    for x in str1:
        count += ord(x)
        
    for y in str2:
        count -= ord(y)
    if count == 0:
        return True
    
    return False


def anagram_check(str1, val):
    
    for y in str1:        
        val -=ord(y)

    return val ==  0 
      
      
def sub_string(actstring, pattern):
    
    l_p = len(pattern)-1
    l_act = len(actstring) - 1
    l = 0
    f_index = -1
    
    pat_val = 0
    
    for x in pattern:
        
        pat_val += ord(x)
    
    while(l_p <=l_act):
        if (anagram_check(actstring[l:l_p+1], pat_val)):
            f_index = l
            break
        l_p +=1
        l +=1
        
    return f_index


print(sub_string('actor', 'cat'))
print(sub_string('actor', 'tar'))
print(sub_string('actor', 'rot'))
print(sub_string('actor', 'toc'))



def anagram(str1, str2):
    
    if not str1 and  not str2:
        return False
    
    if len(str1) != len(str2):
        return False
    
    count = 0

    for x in str1:
        count += ord(x)
        
    for y in str2:
        count -= ord(y)
    if count == 0:
        return True
    
    return False



print(anagram('', ''))
print(anagram('tttt', 'aaa'))
print(anagram('cat', 'tac'))
print(anagram('abcd', 'cdef'))




gj

g =  g, h ,f

i = i, o, k


gi, go, gk
hi, ho, hk
fi, fo, fk

def all_permute(l1, l2):
    st = set()
    for x in l1:
        for y in l2:
            st.add(x+y)
    return list(st)

def valid_wordfind(str1, str2, valid_word):
    
    l1 = list(str1)
    l2 = list(str2)
    valid = []
    lst = all_permute(l1, l2)
    for x in lst:
        if x in valid_word:
            valid.append(x)
        
    return valid





valid_word = ['go', 'hi']
        
l = valid_wordfind('ghf', 'iok', valid_word)

print(l)
123 



open_b = ['[', '{', '(']
close_b = [']', '}', ')']

def check_para(str1):
    
    if not str1:
        return False
    
    if (len(str1) == 0):
        return False
    
    stack = []
    
    for x in str1:
        
        if x in open_b:
            
            stack.append(x)
        elif x in close_b:
            
            pos = close_b.index(x)
            
            if len(stack) > 0 and open_b[pos] == stack[len(stack) - 1]:
                stack.pop()
                
            else:
                return False
        
    if len(stack) == 0:
        return True
    else:
        return False
    

    
print(check_para(")(){}"))


# Driver code 
string = "{[]{()}}"
print(string,"-", check_para(string)) 

string = "[({}{})()]"
print(string,"-", check_para(string)) 

string = "((()"
print(string,"-",check_para(string)) 





Input: K = 4, X = 35
       arr[] = {12, 16, 22, 30, 35, 39, 42, 
               45, 48, 50, 53, 55, 56}
Output: 30 39 42 45


def binary_search(arr, low, high, num):
    while (low <= high):
        mid = low + (high-low) // 2
        
        if  num >= arr [mid] and num < arr[mid +1] :
            return arr[mid], mid
        elif num > arr[mid]:
            
            low = mid +1
        else:
            
            high = mid - 1
    return -1, -1

arr  = [12, 16, 22, 30, 35, 39, 42, 45, 48, 50, 53, 55, 56]
low = 0
high = len(arr) -1
val = 30
index = -1
num = -1
(num, index) = binary_search(arr, low, high, val)
k =4
if index + k <=high:
    n = index + k
else:
    n = index
if (index-k >= 0):
    l = index -k
else:
    if(index-k < 0):
        l = 0
    
m = {}
for x in range(l,n):
    if arr[x] != val:
        m[arr[x]] = arr[x] - val
    
l = {k:v for k, v in sorted(m.items(), key = lambda x:x[1], reverse=True)}

counter = 0

for x,v in l.items():
    print(x)
    counter +=1
    if counter >= k:
        break

print(binary_search(arr, low, high, 54))
print(binary_search(arr, low, high, 13))



m = {'1': 10, '2':5, '3':0, '4':15}

m = {k:v for k,v in sorted(m.items(), key = lambda x:x[1], reverse= True)}

print(m)
                           
                           
        
str1 = “abcba”
str2 = “abcbea”
        acbea, abcba
str3 = “abecbea”

def check_palindrome(str2):
    #print(str2)
    return str2 == str2[::-1]


def valid_palindrome(str1):
    
    l =0
    r= len(str1) -1
    final = len(str1)
    can = False
    while(l <= r):
        
        if str1[l] == str1[r] and l!=r:
            l +=1
            r -=1
        elif str1[l] != str1[r] or l == r:
            # print(str1[0:l] + str1[l+1:final])
            # print(str1[0:r] + str1[r+1:final])
            if (check_palindrome(str1[0:l] + str1[l+1:final]) or check_palindrome(str1[0:r] + str1[r+1:final])):
                can =True
                break
            else:
                can = False
                break 
    return can


print(valid_palindrome("abcba"))
print(valid_palindrome("abcbea"))
print(valid_palindrome("abecbea"))

x= "P".isalpha()

print(x)

    
l1 =[1,3,5,7,9]
l2 =[2,4,6,8,10]
    
    
def merge_list(l1,l2):
    
    l = len(l1)
    k = len(l2)
    r_l = [None]*(l+k)
    ln = 0
    m = 0
    n = 0
    print(r_l, l, k)
    while( (m+n) <= (l+k)):
        print(m+n)
        # import pdb; pdb.set_trace()
        print(r_l)
        if m <= l and l1[m] < l2[n]:
            r_l[ln] = l1[m]
            ln +=1
            m +=1
        elif n <= k and l2[n] < l1[m]:
            r_l[ln] = l2[n]
            ln +=1
            n +=1
        
    print(r_l)

def merge_lists(my_list, alices_list):
    # Set up our merged_list
    merged_list_size = len(my_list) + len(alices_list)
    merged_list = [None] * merged_list_size

    current_index_alices = 0
    current_index_mine = 0
    current_index_merged = 0
    while current_index_merged < merged_list_size:
        is_my_list_exhausted = current_index_mine >= len(my_list)
        is_alices_list_exhausted = current_index_alices >= len(alices_list)
        if (not is_my_list_exhausted and
                (is_alices_list_exhausted or
                 my_list[current_index_mine] < alices_list[current_index_alices])):
            # Case: next comes from my list
            # My list must not be exhausted, and EITHER:
            # 1) Alice's list IS exhausted, or
            # 2) the current element in my list is less
            #    than the current element in Alice's list
            merged_list[current_index_merged] = my_list[current_index_mine]
            current_index_mine += 1
        else:
            # Case: next comes from Alice's list
            merged_list[current_index_merged] = alices_list[current_index_alices]
            current_index_alices += 1

        current_index_merged += 1

    return merged_list

    
l = merge_lists([1,3,5,7,9], [2,4,6,8,10])
print(l)
            
    
    
    
    
def merge_lists(l1, l2):
    
    f_l = len(l1) + len(l2)
    final = [None]*f_l
    
    current_l1 =0
    current_l2 = 0
    final_l = 0
    
    while(final_l < f_l):
        
        is_l1_exhaust = current_l1 >= len(l1)
        is_l2_exhaust = current_l2 >= len(l2)
        
        if (not is_l1_exhaust and (is_l2_exhaust or l1[current_l1] < l2[current_l2])):
            
            final[final_l] =  l1[current_l1]
            current_l1 +=1
        else:
            
            final[final_l] =  l2[current_l2]
            current_l2 +=1
        final_l +=1
    return final
            
          
        
l1 = [1,9,13,15,17]
l2 = [2,6,8,12,14]
l3 =[3,7,10,19, 21]
l4 =[5,17,23,25,27]

l = [[1,9,13,15,17], [2,6,8,12,14], [3,7,10,19, 21], [5,17,23,25,27]]
            
p = []    
l1 = l[0]
for x in range(1,len(l)):    
    x = merge_lists(l1, l[x])
    l1 = x
    
print(l1)
    

    
    
class queue:
    
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def enqueue(self, x):
        self.stack1.append(x)
        
    def dequeue(self):
        
        if len(self.stack2) == 0 and len(self.stack1) == 0:
            print("queue is empty")
            return
        
        elif len(self.stack2) == 0 and len(self.stack1) > 0:
            
            while(self.stack1):
                tmp = self.stack1.pop()
                self.stack2.append(tmp)
            return self.stack2.pop()
        else:
            return self.stack2.pop()
    
q = queue() 
q.enqueue(1) 
q.enqueue(2) 
q.enqueue(3) 
  
print(q.dequeue()) 
q.enqueue(4) 
q.enqueue(5)
print(q.dequeue()) 
print(q.dequeue()) 
print(q.dequeue()) 
print(q.dequeue()) 


 123

num = 123
result = 0

while(num > 0):
    
    tmp = num % 10
    result = result * 10 + tmp
    num = num //10
    
print(result)


highest product of 3 numbers

highest product of three
highest product of 2 numbers
lowest product of two numbers 
highest number
lowest number


def highest_product_three(arr):
    
    if not arr or len(arr) < 3 :
        return -1
    
    highest_prod_3 = arr[0]*arr[1]*arr[2]
    highest_prod_2 = arr[0]*arr[1]
    lowest_prod_2 = arr[0]*arr[1]
    highest_num = arr[0]
    lowest_num = arr[0]
    i = 2
    while (i < len(arr)):
        highest_prod_3 = max(highest_prod_3, highest_prod_2 * arr[i], lowest_prod_2 *arr[i])
        highest_prod_2 = max(highest_num * arr[i], lowest_num*arr[i], highest_prod_2)
        highest_num = max(highest_num, arr[i])
        lowest_num = min(lowest_num, arr[i])
        i +=1
    return highest_prod_3
    

print(highest_product_three([]))
print(highest_product_three([1,2]))
print(highest_product_three([1,2,3,4,5,6])) # all positive 
print(highest_product_three([-1,-2,-3,-4,-5,-6])) # all negative
print(highest_product_three([1,-2,3,-4,5,6])) # mix of neg and pos



[1,2,3,4,1,2,3] #=> 4
[1,2,1,2] #=> 0
[1] #=> 1

def unique(arr):
    
    if len(arr) <1:
        return -1
    if len(arr) == 1:
        return arr[0]
    
    x = arr[0]
    
    for i in range(1, len(arr)):
        x = arr[i] ^ x
    
    return x
                  

print(unique([1,2,3,4,1,2,3]))
print(unique([1,2,1,2]))
print(unique([1]))




    
                
        
        
        
        
    
    






















    




    
    
    
    
    
















    



            
            

 
