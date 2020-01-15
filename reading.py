data = []
count = 0
with open('review.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
        	print(len(data))
print(len(data))

sumlen = 0 
for d in data:
	sumlen = sumlen + len(d)
	len(d)
    print(sumlen)
print('留言的平均长度为'，sumlen/len（data)）

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有'， len(new), '笔留言长度小于100')