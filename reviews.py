data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 #count = count + 1
		if count % 1000 == 0: #只印出1000的倍數
			print(len(data))
print('檔案讀取完了總共有', len(data), '筆資料')

#算留言平均長度''

sum_len = 0
for d in data: #在data的每一筆資料命名為d
	sum_len += len(d)
print('留言的平均長度為', sum_len/len(data))


#篩選
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆長度留言小於100')
print(new[0])

#篩選2
good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言有提到good')
print(good[0])


print(data[0])
print('.....................')
print(data[2])
