data = []
count = 0
with open('review.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
        	print(len(data))


print(data[0])
# 文字记数
wc = {}#wordcount
for d in data:
	words = d.split(' ') #split可以默认跳过多个空格
for word in words:
    if word in wc:
        wc[word] += 1
    else:
        wc[word] = 1
        print('这个字没有出现过') # 新增新的key进入word字典 
print(wc[word])       

for word in wc:
    if wc[word] > 100:
        print(word, wc[word])        
print(len(wc))


while True:
	word = input('请输入您想查询出的字：')
	if word == 'q':
		break
    if word in wc:
        print(word, '这个字出现的次数为：'， wc[word])
    else: 
    	print('这个字没有出现过哦')

    	





















 #sumlen = 0 
 #for d in data:
	 #sumlen = sumlen + len(d)
	 #len(d)
     #print(sumlen)
 #print('留言的平均长度为'，sumlen/len（data)）

 #new = []
 #for d in data:
	 #if len(d) < 100:
		#new.append(d)
 #print('一共有'， len(new), '笔留言长度小于100')

 #good = []
 #for d in data:
	 #if 'good' in d：
	     #good.append(d)
 #print('一共有'，len(good), '笔留言')