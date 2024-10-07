def decorator_outer(fun):
    def decorator_inner(name):
        print("welcome keerthana, Thanks for entering into CODE CLASH!")
        fun("keerthana")
        print("Bye....")
    return decorator_inner
@decorator_outer
def congrats_message(name):
    print("Hi keerthana")
    print("congratulations charu All the best for your furture endeavors!")
congrats_message("keerthana")
