products = []
while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入商品價格：')
	p = [name, price]
	price = int(price)
	products.append(p) # p = [name, price]也可以移到此行
print(products)

for n in products:
	print(n[0], '的價格是', n[1])

with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n') # 在csv檔中，','是重要的分隔符號 #字串只能＋字串