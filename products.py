import os # operating system

# refactor 重構

# 讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue # 繼續，跳到下一迴
			name, price = line.strip().split(',')
			products.append([name, price])
	return products	

# 讓使用者輸入
def user_input(products):
	while True:
		name = input('請輸入商品名稱：')
		if name == 'q':
			break
		price = input('請輸入商品價格：')
		p = [name, price]
		price = int(price)
		products.append(p) # p = [name, price]也可以移到此行
	print(products)
	return products

# 印出所有商品購買紀錄
def print_products(products):
	for n in products:
		print(n[0], '的價格是', n[1])

# 寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n') # 在csv檔中，','是重要的分隔符號 #字串只能＋字串

def main():
	filename = 'products.csv'
	if os.path.isfile(filename): # 檢查檔案存不存在
		print('yeah! 找到檔案了!')
		products = read_file(filename)
	else:
		print('找不到檔案...')

	products = user_input(products)
	print_products(products)
	write_file(filename, products)

main()



