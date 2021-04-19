data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 # count = count + 1
		if count % 1000 == 0: # %求於數
			print(len(data))
print('檔案讀取完了，總共有', len(data), '筆資料')

# 計算每筆資料平均長度
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

# 快寫法版本
#good = [d for d in data if 'good' in d]  #最前面d代表把每個d裝進清單中
#print(good)

#bad = ['bad' in d for d in data]  #第二種塊寫法範例
#print(bad)

# 文字計數功能
wc = {} # word_count
for d in data:
	words = d.split() #split預設值為空白鍵
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1  # 新增新的key進字典
for word in wc: # word是字典中的key
	if wc[word] > 1000000:
		print(word, wc[word])
print(len(wc))

while True:
	word = input('請問你想查甚麼字?')
	if word == 'q':
		print('thanks for using this')
		break
	if word in wc:
		print(word, '出現過的次數為: ', wc[word])
	else:
		print('這個字沒有出現過喔')
	
	
