import random

number = random.randint(0,100)
running = True
i=0
print( '猜数游戏开始，范围为0-100' )
while running:
    i=i+1
    guess = int( input( '输入你猜的数 : ' ) )
    if guess == number:
        if i<=5:
            print( '哎，你真牛逼,不到五次就猜出来了！' )
        else:
            print( '真他妈菜，猜',i,'次傻子也猜出来了 ' )
        # 这将导致 while 循环中 止
        running = False
    elif guess < number:
        print( ' 怂几把啥，你往往大了怼！ ' )
    else:
        print( ' 你是不是虎，整那么大个数 ' )
else:
    print( ' 最终答案为 ', number )
    # 在这里你可以做你想做的任何事
print( ' 欢迎再来玩啊' )
