class parent:
    def __init__(self,name):
        print("parent init",name)

class child(parent):
    def __init__(self):
        print("child __init__")
        parent.__init__(self,"dhruvish")
        
child_obj=child()