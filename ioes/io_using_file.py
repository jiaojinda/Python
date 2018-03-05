poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
use Python!
'''
# 打开文件以编辑（ ' w' riting）
f = open( 'poem.txt' , 'w' )
# 向文件中 编写 文本
f. write( poem)
# 关闭 文件
f. close( )
# 如果没有特别 指定，
# 将假定启 用 默认的阅 读（ ' r' ead） 模式
f = open( 'poem.txt' )
while True:
    line = f. readline( )
    # 零长度指示 EOF
    if len( line) == 0:
        break
    # 每行（ ` line` ） 的末尾
    # 都已经有了 换行符
    #因 为 它是从一个文件中 进行读取的
    print( line, end='' )
# 关闭 文件
f. close( )
