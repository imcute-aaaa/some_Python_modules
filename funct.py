class function:
    def __init__(self,body,args):
        def funct(*a):
            return eval(body,locals=None)
        return funct

