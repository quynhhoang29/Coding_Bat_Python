#%%sleep_in
"""
The parameter weekday is True if it is a weekday, and the parameter vacation
is True if we are on vacation. We sleep in if it is not a weekday or we're on
vacation. Return True if we sleep in.
sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True
"""
#weekday =true if weekday and not sleep in
 #vacation = true if sleepin
def sleep_in(weekday, vacation):
  if not weekday or vacation: #if not weekday that means we're on vacation
    return True
  else: #weekday is true and we're NOT on vacation
    return False
  # This can be shortened to: return(not weekday or vacation)

#%% dif21 #1
""""Given an int n, return the absolute difference between n and 21, 
except return double the absolute difference if n is over 21.
diff21(19) → 2
diff21(10) → 11
diff21(21) → 0"""

standard_number = 21
ask_number = int(input("Enter a number: "))
if ask_number <0:
    result = standard_number - ask_number
elif ask_number >=0 and ask_number<21:
    result = standard_number - ask_number
else:
    result = (ask_number - standard_number)*2
print("The final result is", result)

#%% near_hundred
"""Given an int n, return True if it is within 10 of 100 or 200. 
Note: abs(num) computes the absolute value of a number.
near_hundred(93) → True
near_hundred(90) → True
near_hundred(89) → False"""

number = int(input("Enter a number: "))
def near_hundred(n):
    n = abs(n)
    if n>0 and n<=150:
        result = abs(100 - n)
        if result<=10:
            return True
        else:
            return False

    elif n>150:
        result = abs(200-n)
        if result<=10:
            return True
        else:
            return False
calculate_near_hundred = near_hundred(number)
print(calculate_near_hundred)

#%% missingChar #1
string = input("Enter a string: ")
list_string = list(string)
index = int(input("Enter the index: "))
del list_string[index]
#print(list_string)
new_string=''.join(list_string)
    #using the join function to make a list become a string
#print(new_string)


#%% missingChar #2
#string = input("Enter a string: ") #input statement here to test out the result
#index = int(input("Enter the index: ")) #input statement here to test out the result
def missing_character(string,index):
    list_string = list(string)
    del list_string[index]
    new_string = ''.join(list_string)
    return new_string
#result = missing_character(string, index) #statement here to test result
#print(result) #statement here to test result


#%%backAround
#string=input("Enter a string: ") #input statement for checking purposes
def backAround(string):
    list_string=list(string)
    string_length = int(len(string))
        #get the length of the string to use it as index
    last_letter=(list_string[string_length-1: string_length])
        #this gets the last letter of the string
    list_string = last_letter  + list_string + last_letter
        #adding the last letter in front and at the end of the string
    list_string = ''.join(list_string)
    return list_string

#result = backAround(string) #for checking purposes
#print(result) #for checking purposes

#%%monkey_trouble
"""
We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if 
they are both smiling or if neither of them is smiling. Return True if we are in trouble.
monkey_trouble(True, True) → True
monkey_trouble(False, False) → True
monkey_trouble(True, False) → False"""
#smiling = 0, not smilling=1
a_smile = int(input("For monkey A, enter 0 for smiling and 1 for not smiling: "))
b_smile = int(input("For monkey B, enter 0 for smiling and 1 for not smiling: "))
def monkey_trouble(a_smile, b_smile):
    if a_smile == 0 and b_smile == 0:
        return True
    elif a_smile == 1 and b_smile == 1:
        return True
    else:
        return False
result = monkey_trouble(a_smile, b_smile)
print(result)

#%%parrot trouble
"""We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. 
We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.
parrot_trouble(True, 6) → True
parrot_trouble(True, 7) → False
parrot_trouble(False, 6) → False"""
#talking = 1, no_talking=0
talking = int(input("Enter 1 if parrot is talking and 0 if it isn't: "))
hour=int(input("Enter hour the parrot talks: "))
def parrot_trouble(talking, hour):
    if talking ==1:
        if hour <7 :
            return True

        elif hour >=7 and hour<=20:
            return False

        else:
            return True
    elif talking==0: #this assumes that talking = 0
        return False
result = parrot_trouble(talking, hour)
print(result)

#%% makes10
"""
Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
makes10(9, 10) → True
makes10(9, 9) → False
makes10(1, 9) → True"""
a = int(input("Enter value A: "))
b = int(input("Enter value B: "))

def makes10(a, b):
    if a==10 or b==10:
        #print("Either a or b is greater than 10") #checking statement
        return True
    elif a+b ==10:
        #print("the sum of a and b is greater than 10") #checking statement
        return True

    else:
        #print("placeholder") #checking statement
        return False

result = makes10(a,b)
print(result)

#%%pos_neg
"""
Given 2 int values, return True if one is negative and one is positive. 
Except if the parameter "negative" is True, then return True only if both are negative.
pos_neg(1, -1, False) → True
pos_neg(-1, 1, False) → True
pos_neg(-4, -5, True) → True"""
#negative  = True when 1
a = float(input("Enter value A: "))
b = float(input("Enter value B: "))
negative = int(input("Enter 1 if the parameter is negative. Else, enter 0"))
def pos_neg(a, b, negative):
    if negative==0 :
        if a<0 and b<0:
            print("0 negative, both nums are neg")
            return False
        if a>0 and b>0:
            print("0 negative, both nums are pos")
            return False
        else: #either num is pos
            return True
    else: #negative ==1
        if a<0 and b<0:
            print("negative, both nums are neg")
            return True
        else: #assumes that either b or a is postive, or both is pos
            print("negative, both nums are pos or either num is positive")
            return False

result = pos_neg(a,b,negative)
print(result)

#%%not-string
"""Given a string, return a new string where "not " has been added to the front. 
However, if the string already begins with "not", return the string unchanged.
not_string('candy') → 'not candy'
not_string('x') → 'not x'
not_string('not bad') → 'not bad' """

string_input = input("Enter a string: ")
def not_string(string_input):
    string_list = list(string_input)
    not_list = ["n", "o", "t"]
    string_list_3 = string_list[0:3]
    not_list_3= not_list[0:3]
    if string_list_3 == not_list_3:
        return string_input
    else:
        not_list = ["n", "o", "t", " "]
        string_list = ''.join(not_list + string_list)
        return string_list

result = not_string(string_input)
print(result)

#%%front_back
"""
Given a string, return a new string where the first and last chars have been exchanged.
front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'"""
str = input("Enter a string: ")
def front_back(str):
    if len(str)==1:
        pass
    else:
        first_letter = str[0]
        last_letter = str[len(str)-1]
        str = last_letter + str[1:len(str)-1] + first_letter
    return str
result = front_back(str)
print(result)


#%% front3
"""
Given a string, we'll say that the front is the first 3 chars of the string. 
If the string length is less than 3, the front is whatever is there. Return 
a new string which is 3 copies of the front.
front3('Java') → 'JavJavJav'
front3('Chocolate') → 'ChoChoCho'
front3('abc') → 'abcabcabc'"""
str=input("Enter a string: ")
def front3(str):
    return str[:3]*3

result = front3(str)
print(result)


#%% sum_double
"""
Given two int values, return their sum. Unless the two values are the same, then return double their sum.
sum_double(1, 2) → 3
sum_double(3, 2) → 5
sum_double(2, 2) → 8"""

a=float(input("Enter A value: "))
b=float(input("Enter A value: "))
def sum_double(a, b):
    if a ==b:
        return (a+b)*2
    else:
        return a+b
result = sum_double(a,b)
print(result)


#%% string_times
"""Given a string and a non-negative int n, return a larger string that is n copies of the original string.
string_times('Hi', 2) → 'HiHi'
string_times('Hi', 3) → 'HiHiHi'
string_times('Hi', 1) → 'Hi' """

n = int(input("Enter a integer: "))
str = input("Enter a string: ")
def string_times(str, n):
    return str *n
result = string_times(str, n)
print(result)

#%% string_times using loops
"""desired output: Hi
                   HiHi 
                   HiHiHi """
n = int(input("Number of times the string be printed: "))
str = input("Enter a string: ")
def string_times(n,str):
    for i in range(n): #if the range is 5, the range INCLUDES the 5
        print(str*(i+1)) #have to add 1 in order for i to start at 1. If 1 wasn't there, i would start at 0, but we
        #can't print anything at 0
        i+=1 #i increases by one until i is equal n and then the statement will no longer be printed
    return
result = string_times(n, str)


#%%front_times 
"""
Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, 
or whatever is there if the string is less than length 3. Return n copies of the front;
front_times('Chocolate', 2) → 'ChoCho'
front_times('Chocolate', 3) → 'ChoChoCho'
front_times('Abc', 3) → 'AbcAbcAbc'"""
n = int(input("Number of times the string be printed: "))
str = input("Enter a string: ")
def front_times(str,n):
    result = ""
    for i in range(n):
        result += str[:3]
    return result
front_times_result = front_times(str,n)
print(front_times_result)


#%%string_bits
"""Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'"""

string = input("Enter a string: ")
def string_bits(string):
    new_string = "" #this string will be used to save the accumulated results
    for i in range(0,len(string),2):
        new_string += string[i]
    return new_string
result = string_bits(string)
print(result)


#%% string_splosion 
""""Given a non-empty string like "Code" return a string like "CCoCodCode".
string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'"""
string = input("Enter a string: ")
def string_splosion(string):
    new_string =""
    final_string =""
    for i in range (len(string)):
        new_string = new_string + string[i]
        final_string = final_string + new_string
    return final_string
result = string_splosion(string)
print(result)

#%%last2 
"""Given a string, return the count of the number of times that a substring 
length 2 appears in the string and also as the last 2 chars of the string, 
so "hixxxhi" yields 1 (we won't count the end substring).
last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2"""
str = input("Enter a string: ")
def last2(str):
    last_2_letters = str[len(str)-2:len(str)+1]
    #print(last_2_letters) #use for checking result
    count=0
    for i in range(len(str)):
        new_string = str[i:i+2]
        print(new_string)
        if new_string == last_2_letters:
            count+=1
    return count-1
result = last2(str)
print(result)


#%%array_count9 
"""Given an array of ints, return the number of 9's in the array.
array_count9([1, 2, 9]) → 1
array_count9([1, 9, 9]) → 2
array_count9([1, 9, 9, 3, 9]) → 3"""
nums=[1, 9, 9, 3, 9]
def array_count9(nums):
    count=0
    for i in range(len(nums)):
        new_num = nums[i] #we don't have to include if line of code here because "i" would automatically becomes the next number
        if new_num == 9:
            count+=1
    return count

result = array_count9(nums)
print(result)



#%% array_front9
"""Given an array of ints, return True if one of the first 4 elements
in the array is a 9. The array length may be less than 4.
array_front9([1, 2, 9, 3, 4]) → True
array_front9([1, 2, 3, 4, 9]) → False
array_front9([1, 2, 3, 4, 5]) → False"""

nums = [1, 2, 2]
def array_front9(nums):
    new_nums = nums[:4]
    for n in new_nums:
        if n==9:
            return True
    return False

result = array_front9(nums)
print(result)

#%% array123
"""Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
array123([1, 1, 2, 3, 1]) → True
array123([1, 1, 2, 4, 1]) → False
array123([1, 1, 2, 1, 2, 3]) → True"""
nums= [1, 1, 2, 3, 1]
def array123(nums):
    desired_nums=[1,2,3]
    new_num = []
    count=0
    for i in range(len(nums)): #this statement is the one below is how you traverse through a list
        new_num = nums[i:i+3]
        if new_num == desired_nums:
            count+=1
    if count>0:
        return True
    else:
        return False
result = array123(nums)
print(result)


#%% string_match 
"""Given 2 strings, a and b, return the number of the positions where they 
contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, 
since the "xx", "aa", and "az" substrings appear in the same place in both strings.
string_match('xxcaazz', 'xxbaaz') → 3
string_match('abc', 'abc') → 2
string_match('abc', 'axc') → 0"""
string_a=('abc')
string_b=('axc')
def string_match(string_a, string_b):
    count=0
    for i in range(len(string_a)-1): #as long as i is in the length of string a
        #this is how we traverese and compare individual elements in two different strings
        #--num 1 was added so the substrings wouldn't include just one character
        #print("--")
        a_substring = string_a[i:i+2]
        b_substring = string_b[i:i+2]
        #print(a_substring)
        #print(b_substring)
        if a_substring == b_substring:
            count+=1
    return count
result = string_match(string_a, string_b)
print(result)

#%% hello_name 
"""Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".
hello_name('Bob') → 'Hello Bob!'
hello_name('Alice') → 'Hello Alice!'
hello_name('X') → 'Hello X!'"""
name=input("Enter a name: ")
def hello_name(name):
    string = "Hello " + name + "!"
    return string
result = hello_name(name)
print(result)


#%%make_abba
""""Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".
make_abba('Hi', 'Bye') → 'HiByeByeHi'
make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
make_abba('What', 'Up') → 'WhatUpUpWhat'"""
a= input ("Enter the first string: ")
b= input("Enter the second string: ")

def make_abba(a, b):
    string= a +b +b+a
    return string
result = make_abba(a,b)
print(result)


#%%make_tags
"""The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text.
In this example, the "i" tag makes <i> and </i> which surround the word "Yay". 
Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".
make_tags('i', 'Yay') → '<i>Yay</i>'
make_tags('i', 'Hello') → '<i>Hello</i>'
make_tags('cite', 'Yay') → '<cite>Yay</cite>'"""
tag=input("Input the tag: ")
word = input("Input thw word: ")
def make_tags(tag, word):
    word_string = ""
    word_string = "<"+tag+">"+word+"</"+tag+">"
    return word_string

result = make_tags(tag, word)
print(result)


#%%make_out_word
"""Given an "out" string length 4, such as "<<>>", and a word, 
return a new string where the word is in the middle of the out 
string, e.g. "<<word>>".
make_out_word('<<>>', 'Yay') → '<<Yay>>'
make_out_word('<<>>', 'WooHoo') → '<<WooHoo>>'
make_out_word('[[]]', 'word') → '[[word]]'"""
out = input("Enter out value: ")
words = input("Enter words:" )
def make_out_word(out, words):
    new_string= out[0:2] + words + out[2:4]
    return new_string
result = make_out_word(out, words)
print(result)


#%% extra_end
"""Given a string, return a new string made of 3 copies of the last 2
 chars of the original string. The string length will be at least 2.
extra_end('Hello') → 'lololo'
extra_end('ab') → 'ababab'
extra_end('Hi') → 'HiHiHi'"""
str = input("Enter a string: ")
def extra_end(str):
    new_string = str[len(str)-2:len(str)]*3
    return new_string
result = extra_end(str)
print(result)

#%%first_two
"""Given a string, return the string made of its first two chars, so the String "Hello" 
yields "He". If the string is shorter than length 2, return whatever there is, so "X" 
yields "X", and the empty string "" yields the empty string "".
first_two('Hello') → 'He'
first_two('abcdefg') → 'ab'
first_two('ab') → 'ab'"""
str = input("Enter a string: ")
def first_two(str):
    if len(str)==0:
        new_string = "" #this is supposed to yield empty string
    else:
        new_string = str[0:2]
    return new_string
result = first_two(str)
print(result)

#%% first_half
"""Given a string of even length, return the first half. 
So the string "WooHoo" yields "Woo".
first_half('WooHoo') → 'Woo'
first_half('HelloThere') → 'Hello'
first_half('abcdef') → 'abc'"""
str = input("Enter a string: ")
def first_half(str):
    return str[0:int(len(str)/2)]
result = first_half(str)
print(result)

#%% without_end
"""Given a string, return a version without the first and last char, 
so "Hello" yields "ell". The string length will be at least 2.
without_end('Hello') → 'ell'
without_end('java') → 'av'
without_end('coding') → 'odin'"""
str= input("Enter a string: ")
def without_end(str):
    return str[1:int(len(str)-1)]
result = without_end(str)
print(result)

#%%combo_string
"""Given 2 strings, a and b, return a string of the form short+long+short, 
with the shorter string on the outside and the longer string on the inside. 
The strings will not be the same length, but they may be empty (length 0).
combo_string('Hello', 'hi') → 'hiHellohi'
combo_string('hi', 'Hello') → 'hiHellohi'
combo_string('aaa', 'b') → 'baaab'"""
a = input("Enter string A: ")
b = input("Enter string B: ")
def combo_string(a, b):
    if len(a)>len(b):
        new_string = b+a+b
    else:
        new_string = a+b+a
    return new_string
result = combo_string(a,b)
print(result)


#%%%non_start
"""Given 2 strings, return their concatenation, except omit the 
first char of each. The strings will be at least length 1.
non_start('Hello', 'There') → 'ellohere'
non_start('java', 'code') → 'avaode'
non_start('shotl', 'java') → 'hotlava'"""
a = input("Enter string A: ")
b = input("Enter string B: ")
def non_start(a, b):
    #new_string = a[1:]+b[1:]
    #tried the code below but it didn't work because string doesn't suport item deletion
        """del a[1]
        del b[1]
        new_string = a+b"""
    return new_string
result = non_start(a,b)
print(result)

#%% left2
"""Given a string, return a "rotated left 2" version where the first 
2 chars are moved to the end. The string length will be at least 2.
left2('Hello') → 'lloHe'
left2('java') → 'vaja'
left2('Hi') → 'Hi'"""
def left2(str):
    return str[2:]+ str[0:2]

#%%first_last6
"""Given an array of ints, return True if 6 appears as either the first 
or last element in the array. The array will be length 1 or more.
first_last6([1, 2, 6]) → True
first_last6([6, 1, 2, 3]) → True
first_last6([13, 6, 1, 2, 3]) → False"""

def first_last6(nums):
    if nums[0]==6 or nums[len(nums)-1]==6:
        return True
    return False

#%%same_first_last
"""Given an array of ints, return True if the array is length 1 
or more, and the first element and the last element are equal.
same_first_last([1, 2, 3]) → False
same_first_last([1, 2, 3, 1]) → True
same_first_last([1, 2, 1]) → True"""
nums=[1,2,1]
def same_first_last(nums):
    if len(nums)>=1:
        if nums[0] == nums[len(nums)-1]:
            return True
    return False
result = same_first_last(nums)
print(result)

#%% make_pi
"""Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.
make_pi() → [3, 1, 4]"""
def make_pi():
    pie_array=[]
    pie_array.insert(0,3)
    pie_array.insert(1,1)
    pie_array.insert(2,4)
    return pie_array
result = make_pi()
print(result)

#%% common_end
"""Given 2 arrays of ints, a and b, return True if they have the same first 
element or they have the same last element. Both arrays will be length 1 or more.
common_end([1, 2, 3], [7, 3]) → True
common_end([1, 2, 3], [7, 3, 2]) → False
common_end([1, 2, 3], [1, 3]) → True"""

def common_end(a,b):
    if a[0]== b[0] or a[len(a)-1] == b[len(b)-1]:
        return True
    return False

#%%sum3
"""Given an array of ints length 3, return the sum of all the elements.
sum3([1, 2, 3]) → 6
sum3([5, 11, 2]) → 18
sum3([7, 0, 0]) → 7"""

def sum3(nums):
    return sum(nums)
 
#%% rotate_left3
"""Given an array of ints length 3, return an array with 
the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.
rotate_left3([1, 2, 3]) → [2, 3, 1]
rotate_left3([5, 11, 9]) → [11, 9, 5]
rotate_left3([7, 0, 0]) → [0, 0, 7]"""
nums=[1, 2, 3]
def rotate_left3(nums):
    #will use the pop function - this function deletes an item based on a position. Items behind this position will be
        #shifted to the left
    remove_item = nums.pop(0)
                #list_name.pop(position_number)
    nums.insert(len(nums),remove_item) #this is an insert function for list
    #list_name.insert(index_position, element)
    return nums
result = rotate_left3(nums)
print(result)

#%%reverse3
"""
Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.
reverse3([1, 2, 3]) → [3, 2, 1]
reverse3([5, 11, 9]) → [9, 11, 5]
reverse3([7, 0, 0]) → [0, 0, 7]"""
nums=[1, 2, 3]
def reverse3(nums):
    nums=nums[::-1]
    return nums
result = reverse3(nums)
print(result)

#%%max_end3
"""Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the 
other elements to be that value. Return the changed array.
max_end3([1, 2, 3]) → [3, 3, 3]
max_end3([11, 5, 9]) → [11, 11, 11]
max_end3([2, 11, 3]) → [3, 3, 3]"""
nums =[6, 2,6 ]
def max_end3(nums):
    if nums[0]>nums[len(nums)-1]:
        del nums[len(nums)-2]
        del nums[len(nums)-1]
        nums.append(nums[0])
        nums.append(nums[0])

    elif nums[0]<nums[len(nums)-1]:
        del nums[0]
        del nums[0]
        nums.append(nums[0])
        nums.append(nums[0])

    elif nums[0]==nums[len(nums)-1]:
        del nums[1]
        nums.append(nums[1])
    return nums
result = max_end3(nums)
print(result)

#%%%sum2
"""Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2, 
just sum up the elements that exist, returning 0 if the array is length 0.
sum2([1, 2, 3]) → 3
sum2([1, 1]) → 2
sum2([1, 1, 1, 1]) → 2"""
nums=[]
def sum2(nums):
    return sum(nums[0:2])
result = sum2(nums)
print(result)

#%%middle_way
"""Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.
middle_way([1, 2, 3], [4, 5, 6]) → [2, 5]
middle_way([7, 7, 7], [3, 8, 0]) → [7, 8]
middle_way([5, 2, 9], [1, 4, 5]) → [2, 4]"""
a =[7, 7, 7]
b =[3, 8, 0]
def middle_way(a, b):
    new_array =[a[1],b[1]]
    return new_array
result = middle_way(a,b)
print(result)

#%%makes_ends
"""Given an array of ints, return a new array length 2 containing the first and last elements from the original array. 
The original array will be length 1 or more.
make_ends([1, 2, 3]) → [1, 3]
make_ends([1, 2, 3, 4]) → [1, 4]
make_ends([7, 4, 6, 2]) → [7, 2]"""
nums = [7, 4, 6, 2]
def make_ends(nums):
    new_array=[nums[0],nums[len(nums)-1]]
    return new_array
result = make_ends(nums)
print(result)

#%%has23
"""
Given an int array length 2, return True if it contains a 2 or a 3.
has23([2, 5]) → True
has23([4, 3]) → True
has23([4, 5]) → False"""
nums = [2, 5]
def has23(nums):
    if nums[0]==2 or nums[0]==3:
        return True
    if nums[1]==2 or nums[1]==3:
        return True
    return False

result = has23(nums)
print(result)

#%%cigar party
"""When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number 
of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the 
number of cigars. Return True if the party with the given values is successful, or False otherwise.
cigar_party(30, False) → False
cigar_party(50, False) → True
cigar_party(70, True) → True"""
cigars = int(input("How many cigars did the squirrels collect? "))
is_weekend = int(input("Enter 1 for weekend and 0 for not weekend: "))
def cigar_party(cigars, is_weekend):
    if is_weekend ==1:
        if cigars >= 40:
            return True
    elif is_weekend==0:
        if cigars >= 40 and cigars <= 60:
            return True
    return False
result = cigar_party(cigars,is_weekend)
print(result)

#%%date_fashion
"""You and your date are trying to get a table at a restaurant. The parameter "you" is the stylishness of your clothes, 
in the range 0..10, and "date" is the stylishness of your date's clothes. The result getting the table is encoded as an
int value with 0=no, 1=maybe, 2=yes. If either of you is very stylish, 8 or more, then the result is 2 (yes). With the 
exception that if either of you has style of 2 or less, then the result is 0 (no). Otherwise the result is 1 (maybe).
date_fashion(5, 10) → 2
date_fashion(5, 2) → 0
date_fashion(5, 5) → 1"""
you_stylish = int(input("Enter your stylishness: "))
date_stylish = int(input("Enter your date's stylishness: "))
def date_fashion(you_stylish, date_stylish):
    if you_stylish<=2 or date_stylish<=2:
        table_chance=0
    elif you_stylish>=8 or date_stylish>=8:
        table_chance = 2
    else:
        table_chance = 1
    return table_chance
result = date_fashion(you_stylish, date_stylish)
print(result)

#%%squirrel_play
"""The squirrels in Palo Alto spend most of the day playing. In particular, they play if the temperature is between 
60 and 90 (inclusive). Unless it is summer, then the upper limit is 100 instead of 90. Given an int temperature and 
a boolean is_summer, return True if the squirrels play and False otherwise.
squirrel_play(70, False) → True
squirrel_play(95, False) → False
squirrel_play(95, True) → True"""
temp= int(input("Enter a current temperature: "))
is_summer = int(input("Enter 1 for summer and 0 for not summer: "))
def squirrel_play(temp, is_summer):
    if is_summer ==1:
        if temp>=60 and temp<=100:
            return True
    if is_summer ==0:
        if temp>=60 and temp<=90:
            return True
    return False
result = squirrel_play(temp,is_summer)
print(result)

#%%caught_speeding
"""You are driving a little too fast, and a police officer stops you. Write code to compute the result, encoded as an 
int value: 0=no ticket, 1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0. If speed is between 61 
and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, 
your speed can be 5 higher in all cases.
caught_speeding(60, False) → 0
caught_speeding(65, False) → 1
caught_speeding(65, True) → 0"""
speed = int(input("Enter your speed: "))
is_birthday = int(input("Enter 1 for birthday and 0 for not birthday: "))
def caught_speeding(speed, is_birthday):
    #this following "if" statement serves to only make only one condition for the speed
    if is_birthday==1:
        new_speed = speed -5
    else:
        new_speed =speed

    if new_speed>=81:
        ticket=2
    elif new_speed<=60:
        ticket=0
    else:
        ticket =1
    return ticket
result = caught_speeding(speed, is_birthday)
print(result)

#%%sorta_sum
"""Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case 
just return 20.
sorta_sum(3, 4) → 7
sorta_sum(9, 4) → 20
sorta_sum(10, 11) → 21"""
a = int(input("Enter A number: "))
b = int(input("Enter B number: "))
def sorta_sum(a, b):
    total_sum = a+b
    if total_sum>=10 and total_sum<=19:
        total_sum =20
    return total_sum
result = sorta_sum(a,b)
print(result)

#%% alarm_clock
"""Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation, 
return a string of the form "7:00" indicating when the alarm clock should ring. Weekdays, the alarm should be "7:00" 
and on the weekend it should be "10:00". Unless we are on vacation -- then on weekdays it should be "10:00" and 
weekends it should be "off".
alarm_clock(1, False) → '7:00'
alarm_clock(5, False) → '7:00'
alarm_clock(0, False) → '10:00'"""
def alarm_clock(day, vacation):
    if day==0 or day==6:
        if vacation ==1:#weekends and vacations
            alarm_time="off"
        else: #weekends, not vacation
            alarm_time="10:00"
    else: #weekdays
        if vacation==1:
            alarm_time = "10:00"
        else:
            alarm_time= "7:00"
    return alarm_time

#%% love6
"""The number 6 is a truly great number. Given two int values, a and b, return True if either one is 6. Or if their sum 
or difference is 6. Note: the function abs(num) computes the absolute value of a number.
love6(6, 4) → True
love6(4, 5) → False
love6(1, 5) → True"""
def love6(a, b):
    difference_result = abs(a-b)
    sum_result = a+b
    if a==6 or b==6:
        return True
    if sum_result==6 or difference_result==6:
        return True
    return False

#%%in1to10
"""Given a number n, return True if n is in the range 1..10, inclusive. Unless outside_mode is 
True, in which case return True if the number is less or equal to 1, or greater or equal to 10.
in1to10(5, False) → True
in1to10(11, False) → False
in1to10(11, True) → True"""
def in1to10(n, outside_mode):
    if outside_mode==1:
        if n<=1 or n>=10:
            return True
    elif outside_mode==0:
        if n>=1 and n<=10:
            return True
    return False
   
#%%near_ten
"""Given a non-negative number "num", return True if num is within 2 of a multiple of 10. Note: (a % b) is the 
remainder of dividing a by b, so (7 % 5) is 2. See also: Introduction to Mod
near_ten(12) → True
near_ten(17) → False
near_ten(19) → True"""
print(19/10)
print(6%10)

num = int(input("Enter a num: "))
def near_ten(num):
    remainder = num%10
    if remainder>2 and remainder<8:
        return False
    return True
result = near_ten(num)
print(result)

#%%make_bricks
"""We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big 
bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. This is a 
little harder than it looks and can be done without any loops. See also: Introduction to MakeBricks.
make_bricks(3, 1, 8) → True
make_bricks(3, 1, 9) → False
make_bricks(3, 2, 10) → True"""
goal = int(input("Enter brick goal: "))
small_stock = int(input("Enter number of small bricks: "))
big_stock = int(input("Enter number of big bricks: "))
def make_bricks(small_stock, big_stock, goal):
    need_big= goal//5
    if need_big >big_stock:
        used_big = big_stock
    elif need_big<=big_stock: #we have more big then we need
        used_big=need_big
    need_small = goal - used_big*5
    if need_small<=small_stock: #the amount of small bricks needed are less than small stock
        return True
    else:
        return False
result = make_bricks (small_stock, big_stock, goal)
print(result)

 #%%lone_sum
"""Given 3 int values, a b c, return their sum. However, if one of the values 
is the same as another of the values, it does not count towards the sum.
lone_sum(1, 2, 3) → 6
lone_sum(3, 2, 3) → 2
lone_sum(3, 3, 3) → 0
"""
a= int(input("Enter A number: "))
b= int(input("Enter B number: "))
c= int(input("Enter C number: "))

def lone_sum(a, b, c):
    if a==b and b==c and c==a:
        return 0
    elif b==c:
        return a
    elif c==a:
        return b
    elif a==b :
        return c
    else:
        return a+b+c
result = lone_sum(a,b,c)
print(result)

#%%lucky_sum
"""Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards 
the sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.
lucky_sum(1, 2, 3) → 6
lucky_sum(1, 2, 13) → 3
lucky_sum(1, 13, 3) → 1"""
a = int(input("Enter A value: "))
b = int(input("Enter B value: "))
c = int(input("Enter C value: "))
def lucky_sum(a, b, c):
    total_sum=0
    if a!=13:
        total_sum+=a
    else:
        return 0
    if b!=13:
        total_sum +=b
    else:
        return a
    if c!=13:
        total_sum +=c
    else:
        return a+b
    return total_sum
result = lucky_sum(a,b,c)
print(result)

#%% no_teen_sum
"""Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19
inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens. Write a separate helper
"def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule. In this way,
you avoid repeating the teen code 3 times (i.e. "decomposition"). Define the helper below and at the
same indent level as the main no_teen_sum().
no_teen_sum(1, 2, 3) → 6
no_teen_sum(2, 13, 1) → 3
no_teen_sum(2, 1, 14) → 3"""
#n = int(input("Enter number: "))

a = int(input("Enter number A: "))
b = int(input("Enter number B: "))
c = int(input("Enter number C: "))

def no_teen_sum(a,b,c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)
result = no_teen_sum(a,b,c)
print(result)

def fix_teen(n):
    if n==15 or n==16:
        num=n
    elif n>=13 and n<=19:
        num=0
    else:
        num=n
    return num

#%%round_sum
"""For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more,
so 15 rounds up to 20. Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5,
so 12 rounds down to 10. Given 3 ints, a b c, return the sum of their rounded values. To avoid code repetition, write a
separate helper "def round10(num):" and call it 3 times. Write the helper entirely below and at the same indent level as
round_sum().
round_sum(16, 17, 18) → 60
round_sum(12, 13, 14) → 30
round_sum(6, 4, 4) → 10"""
a = int(input("Enter number A: "))
b = int(input("Enter number B: "))
c = int(input("Enter number C: "))
def round_sum(a, b, c):
    return round10(a) + round10(b)+ round10(c)
result = round_sum(a,b,c)
print(result)

def round10(num):
    if num%10>=5:
        most_signigicant_digit = num//10 +1
        multiple_10 = most_signigicant_digit*10
    else:
        most_significant_digit = num // 10
        multiple_10 = most_significant_digit * 10
    return multiple_10

#%%close_far
"""Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other is
"far", differing from both other values by 2 or more. Note: abs(num) computes the absolute value of a number.
close_far(1, 2, 10) → True
close_far(1, 2, 3) → False
close_far(4, 1, 3) → True
close_far(4, 3, 5) → False"""
a = int(input("Enter number A: "))
b = int(input("Enter number B: "))
c = int(input("Enter number C: "))
def close_far(a, b, c):
    if abs(b-a)<=1 and abs(c-a)>=2 and abs(c-b)>=2:
            return True
    elif abs(c-a)<=1 and abs(b-a)>=2 and abs(b-c)>=2:
            return True
    return False
result = close_far(a,b,c)
print(result)

#%%make_chocolate
"""We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each).
Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.
make_chocolate(4, 1, 9) → 4
make_chocolate(4, 1, 10) → -1
make_chocolate(4, 1, 7) → 2"""
available_small = int(input("Enter the amount of small bars: "))
available_big =  int(input("Enter the amount of big bars: "))
goal = int(input("Enter the goal amount: "))
def make_chocolate(available_small, available_big, goal):
    big_needed = goal//5
    if big_needed<=available_big:
        small_needed = goal-(big_needed*5)
        #print(small_needed)
    else: #big_needed>=available_big
        small_needed = goal-(available_big*5)
    if small_needed <=available_small:
        return small_needed
    else:
        return -1
result = make_chocolate(available_small, available_big, goal)
print(result)

#%%double_char
"""Given a string, return a string where for every char in the original, there are two chars.
double_char('The') → 'TThhee'
double_char('AAbb') → 'AAAAbbbb'
double_char('Hi-There') → 'HHii--TThheerree'"""
str = input("Enter a string: ")
def double_char(str):
    new_string = ""
    for i in range(len(str)):
        new_string += str[i]*2
    return new_string
result = double_char(str)
print(result)

#%%count_hi
"""Return the number of times that the string "hi" appears anywhere in the given string.
count_hi('abc hi ho') → 1
count_hi('ABChi hi') → 2
count_hi('hihi') → 2
"""
str = input("Enter a string: ")
def count_hi(str):
    counter = 0
    for i in range(len(str)-1):
        #print(str[i], str[i+1])
        if str[i] =="h" and str[i+1]=="i": # we can check for two values in the string at once by doing this
            counter+=1
            #print(str[i],str[i+1])
    return counter
result = count_hi(str)
print(result)

#%%cat_dog
"""Return True if the string "cat" and "dog" appear the same number of times in the given string.
cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True"""
str = input("Enter a string: ")
def cat_dog(str):
    cat_counter = 0
    dog_counter = 0
    for i in range (len(str)-2):
        if str[i]=="c" and str[i+1]=="a" and str[i+2]=="t":
            cat_counter+=1
            print(cat_counter)
        elif str[i]=="d" and str[i+1]=="o" and str[i+2]=="g":
            dog_counter +=1
    if dog_counter==cat_counter:
        return True
    else:
        return False
result = cat_dog(str)
print(result)

#%%count_code
"""Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any
letter for the 'd', so "cope" and "cooe" count.
count_code('aaacodebbb') → 1
count_code('codexxcode') → 2
count_code('cozexxcope') → 2"""
str = input("Enter a string: ")
print("this is count_code1")

def count_code(str):
    code_counter = 0
    for i in range (len(str)-3):
        if str[i]=="c" and str[i+1]=="o" and str[i+3]=="e":
            code_counter+=1
            #print(code_counter)
    return code_counter
result = count_code(str)
print(result)

#%%end_other
"""Given two strings, return True if either of the strings appears at the very end of the other string,
ignoring upper/lower case differences (in other words, the computation should not be "case sensitive").
Note: s.lower() returns the lowercase version of a string.
end_other('Hiabc', 'abc') → True
end_other('AbC', 'HiaBc') → True
end_other('abc', 'abXabc') → True"""
a = input("Enter A string: ")
b = input("Enter B string: ")
print(a[:len(a)])
def end_other(a, b):
    a = a.lower()
    b = b.lower()
    if len(a)>=len(b): #search whether str b is in str a
        if a[len(a)-len(b):len(a)] == b[0:len(b)]:
            return True
    elif len(a)<len(b):
        if b[len(b)-len(a):len(b)] == a[:len(a)]:
            return True
    return False

result = end_other(a,b)
print(result)

#%% end_other - Using class
class End_Other:
    def __init__(self,a,b):
        self.a = a.lower()
        self.b = b.lower()

    def end_other(self):
        if len(self.a)>=len(self.b): #search whether str b is in str a
            if self.a[len(self.a)-len(self.b):len(self.a)] == b[0:len(self.b)]:
                return True
        elif len(self.a)<len(self.b):
            if self.b[len(self.b)-len(self.a):len(self.b)] == self.a[:len(self.a)]:
                return True
        return False

set_1 = End_Other("Hiabc","abc")
print(set_1.end_other())

set_2 = End_Other("yz","12xz")
print(set_2.end_other())
#%%xyz_there
"""Return True if the given string contains an appearance of "xyz" where the xyz is not directly
preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.
xyz_there('abcxyz') → True
xyz_there('abc.xyz') → False
xyz_there('xyz.abc') → True"""

str = input("Enter a string: ")
class Xyz_there:
    def __init__(self, str):
        self.str = str
    def calculate_xyz(self):
        count_without_period = 0
        count_with_period = 0
        for i in range(len(str)):
            if str[i]=="x" and str[i+1]=="y" and str[i+2]=="z":
                count_with_period+=1
        for i in range(len(str)): #the length in this function converts the str to an integer element
            if str[i]=="." and str[i+1]=="x" and str[i+2]=="y" and str[i+3]=="z":
                count_without_period+=1
        if count_with_period == count_without_period: #when .xyz appears, both of these counts are equal to each other
            return False
        elif count_with_period>count_without_period:  #except when .xyz appears first and then another xyz appear
            return True
result = Xyz_there(str)
print(result.calculate_xyz())

#%%count_evens
"""Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
count_evens([2, 1, 2, 3, 4]) → 3
count_evens([2, 2, 0]) → 3
count_evens([1, 3, 5]) → 0"""

nums = [1,3,5]
def count_evens(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i]%2 ==0: #if the operation ==0, this means that the number is an even number
            #print("this is the i",i)
            #print("this is the result",i%2)
            count+=1
    return count
result = count_evens(nums)
print(result)

#%% count_evens - using class
class Count_Evens:
    def __init__(self,nums):
        self.nums = nums
    def count_operation(self):
        count =0
        for i in range(len(self.nums)):
            if self.nums[i] % 2 == 0:  # if the operation ==0, this means that the number is an even number
                 print("this is the i",nums[i])
                # print("this is the result",i%2)
                count += 1
        return count
nums = [2,4,6,8]
set_1 = Count_Evens(nums)
print(set_1.count_operation())

#%% big_diff
"""Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array.
 Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.
big_diff([10, 3, 5, 6]) → 7
big_diff([7, 2, 10, 9]) → 8
big_diff([2, 10, 7, 2]) → 8"""

nums = [7, 7, 6, 8, 5, 5, 6]
class Big_diff:
    def __init__(self,nums):
        self.nums = nums
    def calculate_small(self):
        small = nums[0]
        for i in range(len(nums)):
           if nums[i]<small:
               small = nums[i]
        return small

    def calculate_big (self):
        big = nums[0]
        for i in range(len(nums)):
            if nums[i]> big:
                big = nums[i]
        return big

    def calculate_difference(self,):
        difference = self.calculate_big() - self.calculate_small()
        return difference

set1 = Big_diff(nums)
print(set1.calculate_difference())

#%% centered_average
class Centered_average:
    def __init__(self, nums):
        self.nums = nums

    def calculate_small(self):
        small = self.nums[0]
        for i in range(len(self.nums)):
            if self.nums[i]<small:
                small= self.nums[i]
        return small

    def calculate_big(self):
        big = self.nums[0]
        for i in range(len(self.nums)):
            if self.nums[i]>big:
                big = self.nums[i]
        return big

    def calculate_centered_average(self):
        small_number = self.calculate_small()
        big_number = self.calculate_big()
        sum = 0
        count = 0
        count_small = 0
        count_big = 0
        for i in range(len(nums)):
            if nums[i]==small_number:
                count_small+=1
                """if count_small ==1 or count_small>=3:
                    pass"""
                if count_small ==2:
                    sum +=self.nums[i]
                    count+=1
            elif nums[i]== big_number:
                count_big +=1
                """if count_big ==1 or count_big >=3:
                    del self.nums[i]"""
                if count_big ==2:
                    sum +=self.nums[i]
                    count+=1
            else:
                sum += self.nums[i]
                count+=1

        division_product = sum // count
        return division_product

nums = [1, 2, 3, 4, 100]
result1 = Centered_average(nums)
print(result1.calculate_centered_average())
#%%sum13
"""Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, 
so it does not count and numbers that come immediately after a 13 also do not count.
sum13([1, 2, 2, 1]) → 6
sum13([1, 1]) → 2
sum13([1, 2, 2, 1, 13]) → 6"""
class Sum13:
    def __init__(self,nums):
        self.nums = nums

    def calculate_sum13(self):
        total_sum = 0
        count =0 #this count will be use as a signal. for count =0, this will tell program to add. if count =1, program will not add th number
        for i in range(len(self.nums)):
            if nums[i] ==13:
                count=1
            else: #the number is not 13, will have to check now if this number is right after 13
                if count ==1:
                    #don't add the number immediately right after 13
                    count =0 #sets count to 0 so that the 2nd number after 13 will be added
                elif count ==0:
                    total_sum +=nums[i] #add the number
        return total_sum

nums = [5, 7, 2]
result1 = Sum13(nums)
print(result1.calculate_sum13())

#%%sum67
"""Return the sum of the numbers in the array, except ignore sections of numbers starting with a 
6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
sum67([1, 2, 2]) → 5
sum67([1, 2, 2, 6, 99, 99, 7]) → 5
sum67([1, 1, 6, 7, 2]) → 4"""
class Sum67:
    def __init__(self,nums):
        self.nums = nums

    def calculate_sum67(self):
        count =0
        seven_part_six=0
        total_sum =0
        for i in range(len(nums)):
            if nums[i]==6:
                count =1 #sets count to 1 to stop adding the numbers
            elif nums [i] ==7:
                if count==0: # signals that the seven comes before the six, thus, 7 can be added to the total sum
                    total_sum +=nums[i]
                elif count==1: #end of the 6 to 7 range
                    count =0 #sets count to 0 so that we start adding again
            else:
                if count ==1 and seven_part_six ==1: #conditions are met IF numbers are inside the 6 and 7
                    pass
                if count ==0 and seven_part_six ==0:
                    total_sum += nums[i]
        return total_sum
nums = [2, 2, 6, 7, 7]
result1 = Sum67(nums)
print(result1.calculate_sum67())

#%%has22
"""Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.
has22([1, 2, 2]) → True
has22([1, 2, 1, 2]) → False
has22([2, 1, 2]) → False"""

class Has22:
    def __init__(self,nums):
        self.nums = nums

    def calculate_has22(self):
        count=0
        for i in range(len(nums)):
            if nums[i]==2:
                count+=1
                if count==2:
                    return True
            else: #other numbers appear in the list OR the number appear after the first 2 is not another 2
                count=0
        return False #this scenario occurs when the last number is 2
nums = [5, 2, 5, 2]
result1=Has22(nums)
print(result1.calculate_has22())
