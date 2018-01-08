
# coding: utf-8

# In[1]:


import random

def win():
    # 可将小节5中的同名函数代码复制
    return
    
def lose():
    # 可将小节5中的同名函数代码复制
    return
    
def get_ch_table(line):
    ch_table = []
    for ch in line:
        if ch not in ch_table:
            ch_table.append(ch)
    return ch_table

def idiom_robot(file_name):
    with open(file_name) as fh:
        text = fh.read()
    idioms = text.split()
    idiom = random.choice(idioms)
    chs = get_ch_table(text.replace('\n', ''))

    guess_ch_table = [ch for ch in idiom]
    while len(guess_ch_table) < 6:
        ch = random.choice(chs)
        if ch not in guess_ch_table:
            guess_ch_table.append(ch)
    
    random.shuffle(guess_ch_table)
    
    for i in range(0,6,2):
        print(guess_ch_table[i], guess_ch_table[i+1])
    
    return idiom

def main():
    filename = r'd:\temp\idioms_correct.txt'
    score = 10
    while score >= 0:
        real_idiom = idiom_robot(filename)
        answer_idiom = input('请输入猜测成语，回车结束，直接回车表示退出游戏：')
        if answer_idiom == real_idiom:
            print('答对了，加十分')
            score += 10
            print('你当前的分数是：', score)
            if score == 100:
                win()
                return
        elif answer_idiom == '':
            print('退出游戏。')
            print('你最后的分数是：', score)
            return
        else:
            score -= 10
            print('答错了，减十分')
            print('成语其实是：', real_idiom)
            print('你当前的分数是：', score)
    else:
        lose()
        return

if __name__ == '__main()__':
    main()

