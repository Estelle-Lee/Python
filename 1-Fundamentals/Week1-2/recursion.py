# The base condition (or base case) in a recursive function 
# is intended to prevent the function from calling itself infinitely.
def rfib(n):
    if n==0:
        return 0
    elif n==1 or n==2:
        return 1
    return rfib(n-1)+rfib(n-2)

# rfib(4)=rfib(3)+frib(2)
#         rfib(3)=rfib(2)+rfib(1)
#                 rfib(2)=1+1=2
#        =3


# testing recursion from python shell: type
# python -i recursion.py then 
# call the function with variable 
# etc) 
# python -i recursion.py 
# >>> rfib(4) 
# 3 
# >>> rfib(20) 
# 6765
# >>>exit() OR ctrl+z