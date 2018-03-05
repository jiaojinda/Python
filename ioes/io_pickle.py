import pickle
# 我们 存储相 关对象的文件的名 称
shoplistfile = 'shoplist.data'
# 需要购买 的物品清单
shoplist = ['apple' , 'mango' , 'carrot' ]
# 准备写 入文件
f = open( shoplistfile, 'wb' )
# 转储对象至文件
pickle. dump( shoplist, f)
f. close( )
# 清除 shoplist 变量
del shoplist
# 重新打开存储文件
f = open( shoplistfile, 'rb' )
# 从文件中 载入对象
storedlist = pickle. load( f)
print( storedlist)
