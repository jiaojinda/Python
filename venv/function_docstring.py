def print_max( x, y) :
    ''' Prints the maximum of two numbers. 打印两 个数值中 的最大数。
    The two values must be integers. 这两 个数都应 该是整数'''
    # 如果可能， 将其转换至整数类型
    x = int( x)
    y = int( y)
    if x > y:
        print( x, ' is maximum' )
    else:
        print( y, ' is maximum' )
print_max( 3, 5)
print( print_max. __doc__)
help( print_max)
