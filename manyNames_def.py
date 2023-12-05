def fi(name1,name2):
    print("hello " +name1)
    print("hello "+name2)

fi("ahmed","omar")

print("===========")

def hiall(*names):
    for name in names:
        print("hello "+name) 
hiall("hasan","ehab","amr","amine")
print("======")
hiall("zino")
