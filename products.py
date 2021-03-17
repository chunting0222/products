products = []
while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入商品價格：')
	p = [name, price]
	products.append(p) # p = [name, price]也可以移到此行
print(products)

for n in products:
	print(n[0], '的價格是', n[1])