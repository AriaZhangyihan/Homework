
# coding: utf-8

# In[ ]:


def plalindrome(line):
    for i in range(1, len(line)*2):
        if i == 1:
            print(' '*(len(line)*2-1) +line[0])
        elif i%2 == 1:
            print(' '*(len(line)*2-i) + line[:i//2] + line[i//2] + line[i//2-1::-1])
        else:
            print(' '*(len(line)*2-i) + line[:i//2] + line[i//2-1::-1])

def main():
    text = '赏花归去马如飞'
    plalindrome(text)
    

if __name__ == '__main__':
    main()

