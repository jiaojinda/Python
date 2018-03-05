number = 23
guess = int( input( ' Enter an integer : ' ) )
if guess == number:
    # 新块从这里开始
    print( ' Congratulations, you guessed it. ' )
    print( ' ( but you do not win any prizes! ) ' )
    # 新块在这里结束
elif guess < number:
    # 另 一代码块
    print( ' No, it is a little higher than that' )
    # 你可以在此做任何你希望在该代码块内 进行的事情
else:
    print( ' No, it is a little lower than that' )
    # 你必须 通过猜测一个大于（ >） 设置数的数字来到 达这里。
print( ' Done' )
# 这最后 一句 语句 将在
# if 语句 执行完毕后 执行。
