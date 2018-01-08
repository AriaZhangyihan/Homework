
# coding: utf-8

# In[1]:


with open(r'd:\temp\test.txt', 'w') as fw, open(r'd:\temp\语料.txt') as fr:
    line_number = 0
    for line in fr:
        if line_number < 5000:
            fw.write(line)
            line_number += 1
        else:
            break


# In[6]:


def get_word_table(filename):
    '''
    给定文本，统计词表
    '''
    word_table=[]
    with open(filename) as f:
        text=f.read()
    words=[word.split('/')[0] for word in text.split()] 
    for word in words:
        if word not in word_table:
            word_table.append(word)
    return word_table
filename=r'd:\temp\test.txt'
table=get_word_table(filename)
print(table[:20])


# In[4]:


def count_words_freq(filename, words):
    word_freq_pairs = []
    with open(filename) as f:
        text = f.read()
    for word in words:
        number = text.count(word)
        word_freq_pairs.append([word, number])
    return word_freq_pairs

words_freq = count_words_freq(filename, table)

#测试用print
print(words_freq[:100])


# In[14]:


#词典
d={'michael':45}
d['michael']


# In[15]:


def count_words_freq(filename):
    '''
    给定文本文件，建立词表并同时统计词频
    '''
    word_freq_pairs = []
    
    with open(filename) as f:
        text = f.read()
        
    words = [word.split('/')[0] for word in text.split()]
    for word in words:
        for item in word_freq_pairs:
            if word == item[0]:
                item[1] += 1
                break
        else:
            word_freq_pairs.append([word, 1])
            
    return word_freq_pairs

#测试用

filename = r'd:\temp\test.txt'
table = count_words_freq(filename)
print(table[:100])


# In[ ]:


#coding: utf-8
#示例程序9-6
import time

def count_words_freq(filename):
    '''
    给定文本文件，建立词表并同时统计词频
    '''
    word_freq_pairs = []
    linenum = 0 #当前处理行数
    total_line_number = 0
    
    with open(filename) as f:
        for line in f:
            total_line_number += 1
        print('总行数为：', total_line_number)
        
        f.seek(0)   #重新回到文件起始位置(即0位置)
        start_time = time.time()
        
        for line in f:
            words = [word.split('/')[0] for word in line.split()]
            for word in words:
                for item in word_freq_pairs:
                    if word == item[0]:
                        item[1] += 1
                        break
                else:
                    word_freq_pairs.append([word, 1])
                    
            if linenum % 1000 == 0:
                end_time = time.time()
                print('...当前已经处理到第{}行...已经处理了{:.2f}秒...'.format(linenum, end_time - start_time))
                
            linenum += 1
                    
    return word_freq_pairs

#测试用

filename = r'd:\temp\语料.txt'
table = count_words_freq(filename)
print(table[:100])


# In[24]:


def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
fibonacci(3)


# In[14]:


def fibonacci_iter(n):
    a,b=1,1
    for i in range(n-2):
        a,b=b,a+b
    return b
print(fibonacci_iter(3))


# In[19]:


def fibonacci3_iter(n):
    a, b, c = 1, 1, 1
    for i in range(n-3):
        a, b, c = b, c, a+b+c
    return c

# 测试
print(fibonacci3_iter(5))


# In[25]:


def hanoi(n, A, B, C):
    if n==1:
        print(A,'--->',C)
    else:
        hanoi(n-1, A, C, B)
        print(A,'--->',C)
        hanoi(n-1, B, A, C)

# 以5个盘子做测试
hanoi(5, 'A', 'B', 'C')


# In[26]:


#排序
def sort_simple_selection(seq):
    for i in range(len(seq)-1):
        min = i
        for j in range(i+1, len(seq)):
            if seq[j] < seq[min]:
                min = j
        seq[i], seq[min] = seq[min], seq[i]

numbers = [23,45,12,1,2,333,5,1,222,34,-9]
sort_simple_selection(numbers)
print(numbers)


# In[27]:


def sort_simple_select(seq):
    for i in range(len(seq)-1):
        min=i
        for j in range(i+1,len(seq)):
            if seq[j]<seq[min]:
                min=j
        seq[i],seq[min]=seq[min],seq[i]
numbers=[44,88,10,22,-9,15,8,4]
sort_simple_selection(numbers)
print(numbers)


# In[28]:


str='she is a girl.her boyfriend is a boy. He is a boy'
print(str.replace('is','was',2))


# In[35]:


numbers = [23,45,12,1,2,333,5,1,222,34,-9,-9]
nums = sorted(numbers)
print('nums = ', nums)
print(numbers)
numbers.sort()
print(numbers)


# In[36]:


#coding: utf-8
#示例程序9-18
import time, bisect

def count_words_freq_bisect(filename):
    '''
    给定文本文件，建立词表并同时统计词频
    '''
    word_freq_pairs = []
    linenum = 0 #当前处理行数
    total_line_number = 0
    
    with open(filename) as f:
        for line in f:
            total_line_number += 1
        print('总行数为：', total_line_number)
        
        f.seek(0)   #重新回到文件起始位置(即0位置)
        start_time = time.time()
        
        for line in f:
            words = [word.split('/')[0] for word in line.split()]
            for word in words:
                i = bisect.bisect_left(word_freq_pairs, [word])
                if i != len(word_freq_pairs) and word_freq_pairs[i][0] == word:
                    word_freq_pairs[i][1] += 1
                else:
                    word_freq_pairs.insert(i, [word,1])

            if linenum % 1000 == 0:
                end_time = time.time()
                print('...当前已经处理到第{}行...已经处理了{:.2f}秒...'.format(linenum, end_time - start_time))
                
            linenum += 1
                    
    return word_freq_pairs

#测试用

filename = r'd:\temp\test.txt'
table = count_words_freq_bisect(filename)
print(table[:100])


# In[40]:


words = set()  #建立一个空的set
print('空set：',words)
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}   #集合赋值
print(basket)       # show that duplicates have been removed
letters = set('aadfijskdfsakdfjlasd')                               #字符串直接给集合赋值
print(letters)
print('分割-'*50)
letters = {letter.upper() for letter in 'abcde'}    #集合解析/推导
print(letters)


# In[51]:


letters = {letter.upper() for letter in 'abcde'}    #集合解析/推导
print(letters)
letters.add('h')
print(letters)
print(len(letters))
letters.remove('A')
print(sorted(letters))
letters.clear()
print(letters)


# 集合是可变数据类型。  
# 集合内不存在相同的对象，如在建立集合时有相同对象，则只保留一个。  
# 集合是哈希表，判断对象是否在集合中，比判断对象是否在列表/元组中要快很多，因此这类任务，尽量使用集合而不是列表或元组。  
# 集合内的元素，没有固定的顺序，没有下标，因此你不能用类似list一样的数字索引来取得键值对。

# In[57]:


filename = r'd:\temp\test.txt'
word_table = set()
with open(filename) as f:
    for line in f:
        word_table |= {word.split('/')[0] for word in line.split()}

for i, word in enumerate(word_table):
    print(word)
    if i==5:       #词表较长，本例仅取20个打印出来作为示例
        break


# In[61]:


filename=r'd:\temp\test.txt'
word_table=set()
with open(filename) as f:
    for line in f:
        word_table |={word.split('/')[0] for word in line.split()}
for i,word in enumerate(word_table):
    print(word)
    if i==10:
        break


# In[67]:


list1 = ["这", "是", "一个", "测试"]
for index, item in enumerate(list1):
    print (index, item)
str1 = "this is string example....wow!!!";
str2 = "exam";
 
print(str1.index(str2))
print(str1.index(str2, 10))
aList = [123, 'xyz', 'zara', 'abc'];

print (aList.index( 'xyz' ) )
print (aList.index( 'zara' )) 


# In[78]:


ords = {}                      #建立一个空的dict，与words = dict()等价
print('空dict：',words)
basket = dict(apple=1, orange=2, pear=3, banana=10)   #词典赋值，键不能有重复
print(basket)

tel = {'jack': 4098, 'sape': 4139}
print(tel)
print(tel['jack'])              #词典某个具体键的值


# In[80]:


tel = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]) #利用列表生成词典
print(tel)
letters = {letter:10 for letter in 'abcde'}         #词典解析/推导
print(letters, len(letters))                        #len()求词典内键值对的个数
tel['pengyuan'] = 4078                                 #词典中加入键:值对
print('after:', tel)    
del tel['jack']                                     #删除词典的键。注意值也随之删除
print('after del a key from tel:', tel)
letters.clear()                                     #清空词典
print('after clear():', letters)


# In[95]:


letters = {letter:5 for letter in '人生苦短'}

for key in letters:             #对dict直接遍历，就是对key进行遍历
    print(key)

for key in letters.keys():          #得到dict_keys类型对象，可称为键视图
    print(key)
for value in letters.values():  #得到dict_values类型对象，可称为值视图，可对其遍历得到各个value。
    print(value)
    
for key, value in letters.items():  #得到dict_items类型对象，可称为键值对视图，可对其进行遍历同时得到键与值
    print(key, value)


# In[108]:


letters = {letter:1 for letter in '人生苦短'}

values = list(letters.values())
print(values)
    
items = list(letters.items())
print(items)
    
print(list(letters.keys())) 


# In[117]:



def count_words_freq_dict(filename):
    words_freq_dict = {}
    
    with open(filename) as f:
        for line in f:
            words = [word.split('/')[0] for word in line.split()]
            for word in words:
                if word in words_freq_dict: #如果词典中有键为word，则该word的value+1
                    words_freq_dict[word] += 1
                else:                       #否则，词典中加入键word，其value为1
                    words_freq_dict[word] = 1
                    
    return words_freq_dict

#测试用

filename = r'd:\temp\test.txt'
t = count_words_freq_dict(filename)

for i, item in enumerate(table):
    print(item, t[item])
    if i==5:
        break
    


# In[ ]:


def count_words_freq_dict(filename):
    words_freq_dict={}
    with open(filename) as f:
        for line in f:
            words=[word.split('/')[0] for word in line.split()]
            for word in words:
                if word in words_freq_dict:
                    words_freq_dict[word]+=1
                else:
                    words_freq_dict[word]=1
    return words_freq_dict
filename=r'd:\temp\test.txt'
t=count_words_freq_dict
print(item,t[item])


# In[119]:


#判断回文
def palindrome(seq):
    for i in range(len(seq)//2):
        if seq[i] != seq[len(seq)-i-1]:
            return False
            break
    return True
        
seq = 'abcdedcba'#非递归
def palindrome(seq):
    if len(seq) in [0, 1]:
        return True
    else:
        if seq[0] != seq[-1]:
            return False
        return palindrome(seq[1:-1])
        
seq = 'abcdedcba'
print(palindrome(seq))#递归

