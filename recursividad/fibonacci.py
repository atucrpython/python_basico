
def fibonnacci(n):
    if n <0:
        raise
    if n==0:
        return 0
    if n==1:
        return 1
    return fibonnacci(n-1) + fibonnacci(n-2)

print(fibonnacci(8))
