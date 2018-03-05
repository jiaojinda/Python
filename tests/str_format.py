age = 20
name = ' Swaroop'
print( ' {} was {} years old when he wrote this book' . format( name, age) )
print( ' Why is {} playing with that python?' . format( name) )
print( ' {0: .3f}' . format( 1.0/3) )
# 使用 下划 线填充文本， 并保持文字处于中 间 位置
# 使用 ( ^) 定义 ' ___hello___' 字符串 长度为 11
print( '{0:=^11}' . format( 'hello') )
# 基于关键词输出 ' Swaroop wrote A Byte of Python'
print( ' {name} wrote {book}' . format( name=' Swaroop' , book=' A Byte of Python' ) )
