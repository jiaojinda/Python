print( ' Simple Assignment' )
shoplist = [' apple' , ' mango' , ' carrot' , ' banana' ]
# mylist 只 是指向同 一对象的另 一种名 称
mylist = shoplist
# 我购买 了 第 一项项目 ， 所以我将其从列 表中 删 除
del shoplist[0]
print( ' shoplist is' , shoplist)
print( ' mylist is' , mylist)
# 注意到 shoplist 和 mylist 二者都
# 打印出 了 其中 都没有 apple 的同 样的列 表， 以此我们 确认
# 它们 指向的是同 一个对象
print( ' Copy by making a full slice' )
# 通过生成一份完整的切片 制 作一份列 表的副 本
mylist = shoplist[: ]
# 删 除第 一个项目
del mylist[0]
print( ' shoplist is' , shoplist)
print( ' mylist is' , mylist)
# 注意到 现在两 份列 表已出 现不同
