# def func(name, **kwargs):
#     print(kwargs)
# func(first="solitaire", last="infosys", age="24")
# def func(name,**kwargs):
#     print(kwargs)
#     print(name)
# func(name="solitaire",last="infosys",age="24")
def func(**kwargs):
    for k,v in kwargs.items():
        print(f"{k}->{v}")
func(first="solitaire",last="infosys",age="24")
# def func(**kwargs):
#     for k,v in kwargs.items():
#         print(f"{k}->{v}")
# dict={"first":"solitaire","last":"infosys","age":"24"}
# func(**dict)
# def func(name, *args, age = True, **kwargs):
#     print(name)
#     print(args)
#     print(age)
#     print(kwargs)
#
#
# func('abc', 1, 2, 3, a = 1, b = 2)
