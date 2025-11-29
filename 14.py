# def decor1(f):
#     def wrap():
#         print("Decor1")
#         f()
#     return wrap
# def decor2(f):
#     def wrap():
#         f()
#         print("Decor2")
#     return wrap

# @decor1
# @decor2
# def fun():
#     print("Main Function")
# fun()


# import time
# def timer(fun):
#     def wrapper (*args , **Kways):
#         start = time.perf_counter()
#         result = fun(*args , **Kways)
#         end = time.perf_counter()
#         print(f"It took {end-start:.6f} seconds")
#         return result
#     return wrapper

# @timer
# def compute():
#     total = sum(i for i in range (100000))
#     return total
# compute()



# def make_evens_gen():
#     for i in range (2,111,2):
#         yield i
# my_gen = make_evens_gen()
# for i in my_gen:
#     print(i,end=" ")
# a_list = list(my_gen)
# print(a_list)

 

# def numbers():
#     for i in range (1000):
#         yield i
# def evens(seq):
#     for j in seq:
#         if j%2 == 0:
#             yield j
# def square(seq):
#     for k in seq:
#         yield k*k
# pipeline = square(evens(numbers()))
# for x in range (10):
#     print(next(pipeline))


# def fibbo():
#     a,b = 0,1
#     while(True):
#         yield a
#         a,b = b,a+b
# g = fibbo()
# for i in range(10):
#     print(i , ":" , next(g))
