class PythonQuestionSolution:
    def __init__(self):
        pass
    def reverse_string(self,string:str)->str:
        """
          args: 
             string-> string should be a str.
         
          return: it will return reverse string.
            
         """
        self.string = string
        if not isinstance(string,str):
         raise TypeError("input should be string")
        rev_string = ""
        for char in string:
         rev_string = char + rev_string
        return rev_string
    def largest_number(self,list1:list)->list:
        
        if not isinstance(list1,list):
         raise TypeError("input should be list only")
        list1 = [12,23,43,5,41,2,43,32,4,55]
        largest = list1[0]
        for i in list1:
         if i > largest:
            largest = i
        return largest         
    
    def find_prime_no(self,n:int)->int:
        """
        args:
         n: n should be integer
        retrun:
           it will return prime if the number is prime else it return number is not prime
           
        """
        if not isinstance(n,int):
         raise TypeError("input should be an integer")
        if n <2:
         raise ValueError("Input should be greater than or equal to 2")
        for i in range(2,int(n**0.5)+1):
        
            if n%i==0:
                print("number is not prime")
                break
            
            else:
                 print("number is prime")
       
    def all_prime_no(self)->list:
        """
            
            retrun:
                it will return all prime number between 100 to 200          
        """
        
        result = []
        for i in range(100,201,1):
            number_is_prime = True 
        for j in range(2,int(i**0.5)+1):
            if i % j == 0:
                number_is_prime = False
                break
        if number_is_prime:
            result.append(i)
        return result  
    def calculate_factorial(self,n:int)->int:
        """
        args:
            n: input should be an integer
        retrun:
            it retrun the factoral of the given numbver
            
        """
        if not isinstance(n,int):
            raise TypeError("input should be integer")
        if not n.isdigit:
            raise ValueError("please input valid integer")
        fact = 1    
        for i in range(1,n+1):
            fact *=i
        return fact
    
    
    def check_palindrome(self,text:str)->str:
        """
        args:
            text: input should be string
        retrun 
            this will return the number is palindrome and not
        
        """
        if not isinstance(text,str):
            raise TypeError("input should be string")
        if text.strip() == "":
            raise ValueError("input cannot be empty")
        text = text.lower()    
        reverse_str = ""
        for i in text:
            reverse_str = i + reverse_str
        if reverse_str == text:
            print("number is palindrome")
        else:
            print("number is not palindrome")

    def count_vowel(self,text:str)->str:
        """
        args:
            text: text should be integer
        return:
            it will return how many vowel are present
            in the text
        
        
        """
        if not isinstance(text,str):
            raise TypeError("input should be string")
        if text.strip() == "":
            raise ValueError("input should not be empty")
        vowel = "aeiou"
        text = text.lower()
        count = 0
        for i in text:
            if i in vowel:
                count +=1
        return count
    
    
    def second_largest(self):
        """
        this function will retrun a second largest in the list
        """
        list1 = [22,2,23,53,4,43,4,56]
        largest = list1[0]
        second_lar = list1[0]
        for i in list1:
            if i > largest:
                second_lar = largest
                largest=i
            elif i > second_lar and i != largest:
                second_lar = i
        return f"largest= {largest} and second_largest= {second_lar}"
    
    def sum_digit(self,number:int)->int:
        """
        args:
            number: number should be an integer
        retrun:
            this function should return the sum of the given 
            number.
        
        """
        if not isinstance(number,int):
            raise TypeError("input should be an integer")
        total = 0
        for i in range(1,number+1):
            total +=i
        return total
    
    
    
    
    
    def duplicates_remo(self):
        """
        this function will remove the duplicates from the list
        """
        list1 = [1,2,3,1,1,2,3,4,45,4,2,11,2]
        result = []
        for i in list1:
            if i not in result:
                result.append(i)
        return result
    
    def factorial(self,n:int)->int :
        """
        this will return a factorial of a given number
        args:
            n: n should be an integer
        retrun: 
            it is recursive type function
        
        """
        if not isinstance(n,int):
            raise TypeError("intput should be an integer")
        if n < 0:
            raise ValueError("input should be greater than 0")
        if n==0 or n==1:
            return 1
        number = n * self.factorial(n-1)
        return number 
        
    def occurence_of_ch(self,text:str)->str:
        """
        args:
        text: text should be an integer
        return:
            this function tell nuber of occurence 
            of each character in the text
        
        """
        if not isinstance(text,str):
            raise TypeError("input should be an integer")
        if text.strip=="":
            raise ValueError("input should not be empty")
        result = {}
        text = text.lower()
        for i in text:
            if i in result:
                result[i] +=1
            else:
                result[i]=1
        return result     
    
    
    def string_anagram(self,text1:str,text2:str)->str:
        """
        args:
        text1: text1 should be string
        text2: text2 should be string
        return:
        this functiont tells that the given strings will be anagram or not
        
        """
        if len(text1)!=len(text2):
            raise TypeError("length of both string string should be equal")
        if not isinstance(text1,str) or not isinstance(text2,str):
            raise ValueError("input should be string")
        result = {}
        for i in text1:
            if i in result:
                result[i] +=1
            else:
                result[i] =1
        for i in text2:
            if i in result:
                result[i] -=1
            else:
                print("string are not anagram")
        if result[i] ==0:
            print("strings are anagram")
        else:
            print("strings are not anagram")
            
            
    def fibonacci_series(self,n:int)->int:
        """
        args:
            n: input should be an integer
        retrun:
            this function will return a fibonacci series
            of the input number
        """
        if not isinstance(n,int):
            raise TypeError("input should be an integer")
        if n <0:
            raise ValueError('input should not be negative')
        a = 0
        b = 1
        for i in range(n):
            print(a,end=" ")
            c = a+b
            a = b
            b = c  
            
            
            
    def check_leap(self,year:int)->int:
        """
        args:
            year: year should be an integer
        return:
            this function will tells that the 
            given year is leap year or not
        
        """
        if not isinstance(year,int):
            raise TypeError("input should be an integer")
        if year % 4==0 and year%100!=0:
            print("year is leap year")
        elif (year%400==0):
            print("year is leap year")
        else:
            print("year is not leap year")                
            
            
    def calculate_power(n:int,m:int)->int:
        """
        ars:
        n = n should be input
        m = m should input
        retrun : 
            this function will return the power of given input
        """
        if not isinstance(n,int) or not isinstance(m,int):
            raise TypeError("input should be integer")
        if m <0:
            raise ValueError("m should be greater than 0")
        result = 1
        for i in range(m):
            result = result * n
        return result         
    
    def even_no_list(self,n:int)->list:
        """
        args: 
            n : n should be an integer
        return :
            this function return a even number of list
            
        """
        if not isinstance(n,int):
            raise TypeError("input should integer")
            
        result = []
        for i in range(n+1):
            if i%2!=0:
                continue
            else:
                result.append(i)
        return result
    
    
    def binary_search(self,target:int)->int:
        """
        args:
            target : target value should integer
        return:
            this function will find the target value in the list1
            and it will return the index of the target position
            if targeted value not find then iot will return -1
            
        """
        list1 = [12,3,4,56,6,76,78,98,23,45,34]
        list1.sort()
        low = 0
        high = len(list1)-1
        while low <= high:
            mid = (low+high)//2
            if list1[mid] == target:
                print("number is at index =",mid)
                break
            elif target < list1[mid]:
                high = mid-1
            else:
                low = mid+1
        else:
            print(-1)
            
            
    def reverse_sentence(self,sentence:str)->str:
        """
        args:
        sentence: input sentence
        return:
        str: Sentence with words reversed.
        Raise:
        TypeError: if input is not a string
        
        """
        if not isinstance(sentence,str):
            raise TypeError("input must be string")
        list1 = []
        word = ""
        for i in sentence:
            if i != " ":
                word = word + i
            else:
                list1.append(word)
                word = ""
        list1.append(word)
        rev_sentence = ""
        for i in range(len(list1)-1,-1,-1):
            rev_sentence = rev_sentence + list1[i] + " "
        return rev_sentence        
    
    
    def find_gcd(self,a:int,b:int)->int:
        """
        args:
            a: a should be an integer.
            b: b should be an integer.
        result:
            it will return the greatest commom divisor of both input.
        """
        if not isinstance(a,int) and not isinstance(b,int):
            raise TypeError("input should be an integer")
        while b!=0:
            a,b=b,a%b
        return a
    def find_gcd_recursive(self,a:int,b:int)->int:
        """
        args:
            a: a should be an integer.
            b: b should be an integer.
        result:
            it will return the greatest commom divisor of both input.
        """
        if not isinstance(a,int) and not isinstance(b,int):
            raise TypeError("input should be an integer")
        if b==0:
            return a
        return self.find_gcd_recursive(b,a%b) 
    
    def calculate_binary(self,decimal:int)->str:
        """
        convert decimal number into binary number
        args:
            decimal: decimal should be an integer
            
        """
        if decimal == 0:
            return 0
        if not isinstance(decimal,int):
            raise TypeError("input should be an integer")
        binary = ""    
        while decimal > 0:
            remainder = decimal % 2
            binary = str(remainder) + binary
            decimal = decimal//2
        return binary
    
    
    def find_intersection(self,list1:list,list2:list)->list:
        """
        args:
            list1 and list2 should be list
        return :
            it will return the common elements from both list
            
        """
        if not isinstance(list1,list) and not isinstance(list2,list):
            raise TypeError("input should be list ")
        result = []
        for item in list1:
            if item in list2:
                result.append(item)
        return result
    
    def remove_whitespace(self,text:str)->str:
        """
        args: 
            text: text should be string
        return : 
            it will return string which have no whitespace
            
        """
        if not isinstance(text,str):
            raise TypeError("input should be string")
        text = text.strip()
        result = ""
        for i in text:
            if not i.isspace():
                result = result + i
        return result
    
    def list_sum(self,number:list)->int:
        """
        args:
            number: number should be list.
        return:
            it will return the sum of number in the list
        """
        if not isinstance(number,list):
            raise TypeError("input should be string")
        if len(number)==0:
            return 0
        return number[0] + self.list_sum(number[1:])
    
    
    def sort_list(list1:list)->list:
        
        """
        args:
            list1: list1 should be list
        return:
            it will return sort list
        """
        
        if not isinstance(list1,list):
            raise TypeError("input must be list")
        for i in range(len(list1)):
            for j in range(len(list1)-i-1):
                if list1[j] > list1[j+1]:
                    list1[j],list1[j+1] =list1[j+1],list1[j]
        return list1
    
    def merge_sort_list(self,list1:list,list2:list)->list:
        '''
        args:
            list1 and list2 both should be list
        return :
            it will return the single list
            of the two merge list

        
        '''
        if not isinstance(list1,list) and not isinstance(list2,list):
            raise TypeError("input should be list")
        result = []    
        i = 0
        j = 0
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                result.append(list1[i])
                i +=1
            else:
                result.append(list2[j])
                j +=i
        result.extend(list1[i:])
        result.extend(list2[j:])
        return result
    
    
    def check_sort(self,list1:list)->str:
        """
        args:
            list1: list1 should be a list
        return :
            this function tells us that the given
            list is sort aur not
        """
        if not isinstance(list1,list):
            raise TypeError("input should be list")
        for i in range(len(list1)-1):
            if list1[i] > list1[i+1]:
                print("list is not sorted")
                break
        return "list is sorted"
    
    
    def count_frequency(self,filename)->dict:
        """
        args:
            filename: filename should be correct
        return :
            it will return a number of reapting text in a file
        """
        if  not filename.endswith(".txt"):
            raise TypeError("file name should be correct")
        
        result = {}
        with open(filename,mode="r") as file:
            for line in file:
                word = line.split()

                for i in word:
                    if i in result:
                        result[i] +=1
                    else:
                        result[i] = 1
        return result
    
    
    def find_missing_consecutive(self,list1:list)->int:
        """
        args:
            list1: list1 must be a list.
        return:
            it will return missing number.
        """
        if not isinstance(list1,list):
            raise TypeError("Input must be a list")
        for i in range(len(list1)-1):
            if list1[i+1]-list1[i]!=1:
                break
        return f"missing number is: {list1[i]+1}" 
    
    
    
    
    def square_natural(self,n:int)->int:
        """  
        args:
            n -> n should be an integer
        result:
            it will return the square of sum natural number.
        """
        if not isinstance(n,int):
            raise TypeError("input must be integer")
        total = 0
        for i in range(0,n+1):
            total += (i**2)
        return total
    
    
    def reverse_integer(self,num:int)->int:
        """
        args:
            n -> n should be an integer.
        result:
            it will reverse the integer
        """
        if not isinstance(num,int):
            raise TypeError("input must be an integer")
        reverse = ""
        while num !=0:
            number = num %10
            reverse = reverse + str(number)
            num = num//10
        return reverse
    
    def find_longest_word(self,text:str)->str:
        """    
        args:
            text -> text should be a string.
        return: find longest word in the given input and return it.
        
        """
        if not isinstance(text,str):
            raise TypeError("input must be string")
        text = text.split()    
        word_num = {}
        for word in text:
            if word not in word_num:
                word_num[word] = len(word)
        max_value = max(word_num.values())
        longest_word = [key for key,value in word_num.items() if value == max_value]
        return longest_word
    
    
    def check_num_power(self,num:int)->bool:
        """      
        args:
            num -> num should be an integer.
        return:
                it will check that the number is power of 2 and give boolean value and power.
        """
        if not isinstance(num,int):
            raise TypeError("input must be integer")
        if num>0 and (num & (num-1)) ==0:
            return True, (num).bit_length()-1
        return False, None
    
    
    def Flatten_the_list(self,List:list)->list:
        """
        args:
            List -> input should be list.
        return :
            it will return the flatten list of nested list.
            
        """
        if not isinstance(List,list):
            raise TypeError("input must be list")
        result = []
        for item in List:
            if isinstance(item,list):
                result.extend(self.Flatten_the_list(item))
            else:
                result.append(item)
        return result 
    
    
    def convert_tuples_dict(self,List:list)->dict:
        """
        args:
            List -> input should be list.
        return:
            it will convert list of tuples into Dictionary
        
        """
        if not isinstance(List,list):
            raise TypeError("input must be list")
        Dict = {}
        for key,value in List:
            Dict[key] = value
        return Dict
    
    
    def find_median_list(self,List:list)->int:
        """
        args:
            List -> input should be list.
        return:
            it will return the median of the list
        
        """
        if not isinstance(List,list):
            raise TypeError("input must be list")
        List.sort()    
        list_length = len(List) 
        mid = list_length // 2
        if list_length % 2 != 0:
            return List[mid]
        else:
            return (List[mid-1] + List[mid]/2)
        
    def sorted_dictionary(self,data:dict)->dict:
        """
        args:
        data-> data should be a dictionary.
        return :
                it will return the sorted dictionary by value.
        """
        if not isinstance(data,dict):
            raise TypeError("input must be dictionary")
        sorted_dict = dict(sorted(data.items(),key=lambda x:x[1]))
        return sorted_dict     
    
    def find_lcm(self,a:int,b:int)->int:
        """
        args:
            a and b should be integer
        return :
            it will return the lcm of the number
        """
        if not isinstance(a,int) and not isinstance(b,int):
            raise TypeError("Input should be string")
        while b !=0:
            a,b=b,a%b
            return a
        lcm = a+b//a
        return lcm
    
    def binary_to_decimal(self,string:str)->int:
        """
        args:
            string-> input should be string.
        return:
                it will convert binary number into decimal.
        
        """
        if not isinstance(string,str):
            raise TypeError("Input must be string")
        if not string.isdigit():
            raise ValueError("Input should be in number form")
        if any(i not in "01" for i in string):
            raise ValueError("Input should contain only 0 and 1")
        total = 0
        power = 0
        for i in string[::-1]:
            if i =="0":
                continue
            else:
                total = total + (2**power)
            power = power + 1
        return total
    
    def swap_number(self,a:int,b:int)->int:
        """
        args:
            a and b should be integer.
        return:
                it will wsap two number each other
        
        """
        if not isinstance(a,int) and not isinstance(b,int):
            raise TypeError("input must be integer")
        a,b = b,a    
        return f"a is {a} and b is {b}"
    
    def find_commom_elements(self,list1:list,list2:list,list3:list)->list:
        """
        args:
            list1, list2 and list3 should be list.
        return :
            it will return list of commom elements form all thrre list.
        """
        if not isinstance(list1,list) and not isinstance(list2,list) and not isinstance(list3,list):
            raise TypeError("Input must be list")
        result = []
        for i in list1:
            if i in list2 and i in list3:
                if i not in result:
                    result.append(i)
                
        return result
    
    def remove_nth_character(self,string:str,ch:str,n:int)->str:
        """
        args: 
            string: string should be str.
            ch : ch should be str.
            n : n should be input.
        return:
            this function will delete nth number of character.
        
        """
        if not isinstance(string, str):
            raise TypeError("Input must be a string")

        if not isinstance(ch, str):
            raise TypeError("Character must be a string")

        if len(ch) != 1:
            raise ValueError("Please provide exactly one character")

        if not isinstance(n, int) or isinstance(n, bool):
            raise TypeError("n must be an integer")
    
        num = 0
        for i in range(len(string)):
            if string[i] == ch:
                num = num + 1
                if num == n:
                    return string[:i] + string[i+1:]
        return string
    
                
    def first_non_repeated_ch(self,text:str)->str:
        """
        args: 
            text-> text should be string.
        return :
                it will return fir non repeated charachter.
        """
        if not isinstance(text,str):
            raise TypeError("input must be string")
        dic = {}
        for i in text:
            if i in dic:
                dic[i] +=1
            else:
                dic[i] = 1
        for key,value in dic.items():
            if value==1:
                break    
        return key
    
    def check_only_digit(self,text:str)->str:
        """
        args: 
            text-> text should be string.
        return :
                it will return fir non repeated charachter.
        """
        if not isinstance(text,str):
            raise TypeError("input must be string")
        for i in text:
            if i < "0" or i > "9":
                print("string does not contain only digit")
                break
        else:
            print("string contains only digit")
            
    def check_armstrong(self,num:int)->bool:
        """
        args:
            num-> it should be an integer.
        return :
                it will check the number is armstrong or not.
        
        """
        if not isinstance(num,int):
            raise TypeError("input must be integer")
        num_count=0
        while num>0:
            num = num//10
            num_count +=1
        tem_num = num
        total = 0
        while num>0:
            tem_num = num%10
            total = total + tem_num**num_count
            num = num//10
        return total == num        
    
    def reverse_list(self,list1:list)->list:
        """
        args: 
            list1-> input should be list.
        return:
            it will reverse the string without using any method.
        
        """
        if not isinstance(list1,list):
            raise TypeError("input must be list")
        left = 0
        right = len(list1) - 1
        while left < right:
            list1[left],list1[right] = list1[right],list1[left]
            left +=1
            right -=1
        return list1
    
    def check_subsequence(self,larger_list:list,smaller_list)->list:
        """
        args: 
            list1-> input should be list.
        return:
            it will reverse the string without using any method.
        
        """
        if not isinstance(larger_list,list) and not isinstance(smaller_list,list):
            raise TypeError("input must be list")
        for item in smaller_list:
            if item not in larger_list:
                print("smaller_list is not subsequence of larger list")
        else:
            print("smaller_list is subsequence of larger list") 
            
            
    def find_subset(self,data:list)->list:
        """
        args: 
            list1-> input should be list.
        return:
            it will reverse the string without using any method.
        
        """
        if not isinstance(data,list):
            
            raise TypeError("input must be list")
        subsets = [[]]
        for item in data:
            new_subset = []
            for subset in subsets:
                new_subset.append(subset+[item])
            subsets.extend(new_subset)
        return subsets
                
     
class Stack:
    def __init__(self,list1):
        self.stack = list1
    def push(self,n):
        return self.stack.append(n)
    def pop(self):
        if len(self.stack) == 0:
            return "list is empty" 
        return self.stack.pop()
    def peek(self):
        if len(self.stack) == 0:
            return "list is empty" 
        return self.stack[-1] 
    
class Queue:
    def __init__(self):
        self.queue = []
    def isempty(self):
        len(self.queue) == 0
        return "queue is empty"
    def Enqueue(self,value):
        self.queue.append(value)
        print(self.queue)
    def Dequeue(self):
        if len(self.queue) == 0:
            return "queue is empty"
        else:
            self.queue.pop(0)
    def Peek(self):
        if len(self.queue) == 0:
            return "queue is empty"
        else:
            return self.queue[0]                     