# x:int = 1

# def add_numbers(a:int , b:int, c:int) -> int:
#     return a + b + c

# print(add_numbers(1,2,3))

from typing import List, Dict, Set, Optional, Any, Sequence, Tuple, Callable, TypeVar

# x: List[List[int]] = [[1,2,3],[4,5,6]]

# y: Dict[str, str] = {"masila":"david"}

# z: Set[str] = {"a","b"}


# #custom types 
# vector = List[float]

# def foo(x: vector) -> vector:
#     return x

# vectors = List[vector]

# def foo2(y: vectors) -> vector:
#     return y 

#optional type 

# def foo(x: Optional[bool] = False):
#     pass 


# def foo2(x: Any):
#     pass 


#sequence  >> Anything that can be indexed

# def foo(seq: Sequence[str]):
#     pass

# foo(("a","b","c"))
# foo(["a","b","c"])

#tuple and Tuple 

# x: tuple = (1,2,3,4,5)
# y: Tuple[int, int, bool] = (1,2,False)

#collable 

# def foo(func: Callable[[int, int, Optional[int]], int]) -> None: #Callable function takes in two ints and returns an int
#     func(1,2)

# def foo2() -> Callable[[int, int], int]:
#     def add(x:int, y:int) -> int:
#         return x + y 
    
#     return add

#Generics 

T = TypeVar('T')

def get_item(lst: List[T], index: int) -> T:
    return lst[index]

#donno what type is going to be in the list but assume they are going to be same type
#We respresent the assumed all same type with the T and return it. Hopefully as same type
