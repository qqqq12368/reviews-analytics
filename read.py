data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 # count = count + 1
		if count % 1000 == 0: # %求於數
			print(len(data))
print('檔案讀取完了，總共有', len(data), '筆資料')



#計算每筆資料平均長度
sum_len = 0
for d in data:
	sum_len = sum_len + len(d)

print('平均是', sum_len/len(data))

# filter1
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '比留言長度小於100')
print(new[0])
# filter 2
good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '是good字串')
print(good[0])

#快寫法版本
good = [d for d in data if 'good' in d]  #最前面d代表把每個d裝進清單中