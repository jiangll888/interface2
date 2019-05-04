def te(*args,**kwargs):
    t(*args,**kwargs)
    print(*args,kwargs)

def t(*args,**kwargs):
    #args[0]=1
    kwargs["a"]="a"

if __name__ == "__main__":
    te(10,2,a=3)