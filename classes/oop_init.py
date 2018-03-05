class Person:
    def __init__( self, name) :
        self. name = name
    def say_hi( self) :
        print( ' Hello, my name is' , self. name)
p = Person( ' Swaroop' )
p. say_hi( )
# 前面两 行同 时也能写 作
# Person( ' Swaroop' ) . say_hi( )
