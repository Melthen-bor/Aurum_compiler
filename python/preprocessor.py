class macro:
    def __init__(self,name,content):
        self.name=name;
        self.content=content
    def check(self,name):
        if self.name==name:
            return True
        else:
            return False
class preprocessor:
    def __init__(self):
        self.macros=[]
    def read(self,name):
        a=open(name+".gold")
        b=a.read()
        a.close()
        return b.split("\n")
    def directive_parse(self,arr,name):
        temp=""
        x=0
        while True:
            try:
                t=arr[x]
                if t[0]=="#":
                    if t[1]=="p":
                        if t[2]=="u":
                            if t[3]=="t":
                                if t[4]==" ":
                                    y=0
                                    a=t.split(" ")
                                    while True:
                                        try:
                                            print("finding macro")
                                            tm=self.macros[y]
                                            if tm.check(a[1]):
                                                print("placing macro")
                                                arr[x]=tm.content
                                                temp="\n".join(arr)
                                                arr=temp.split("\n")
                                                return arr
                                            else:
                                                y+=1
                                        except:
                                            break
                    elif t[1]=="s":
                        if t[2]=="t":
                            if t[3]=="a":
                                if t[4]=="r":
                                    if t[5]=="t":
                                        if t[6]=="_":
                                            if t[7]=="d":
                                                if t[8]=="e":
                                                    if t[9]=="f":
                                                        if t[10]==" ":
                                                            y=1
                                                            tm=""
                                                            nm=t.split(" ")
                                                            while True:
                                                                print("defining macro")
                                                                a=arr[x+y]
                                                                if a=="#end_def":
                                                                    self.macros+=[macro(nm[1],tm)]
                                                                    temp=""
                                                                    z=0
                                                                    while True:
                                                                        try:
                                                                            print("parsing list")
                                                                            if not z==0:
                                                                                temp+="\n"
                                                                            if z==x:
                                                                                print("removing macro lines")
                                                                                z+=y+1
                                                                            temp+=arr[z]
                                                                            z+=1
                                                                        except:
                                                                            break
                                                                    print("macro definition over")
                                                                    break
                                                                else:
                                                                    if not y==1:
                                                                        tm+="\n"
                                                                    tm+=a
                                                                    y+=1
                                                            arr=temp.split("\n")
                                                            return arr
                    elif t[1]=="m":
                        if t[2]=="o":
                            if t[3]=="v":
                                if t[4]=="e":
                                    if t[5]==" ":
                                        y=0
                                        a=t.split(" ")
                                        while True:
                                            try:
                                                tm=self.macros[y]
                                                if tm.check(a[1]):
                                                    arr[x]=tm.content
                                                    self.macros.remove(tm)
                                                    temp="\n".join(arr)
                                                    arr=temp.split("\n")
                                                    return arr
                                                else:
                                                    y+=1
                                            except:
                                                break
                    elif t[1]=="u":
                        if t[2]=="n":
                            if t[3]=="d":
                                if t[4]=="e":
                                    if t[5]=="f":
                                        if t[6]==" ":
                                            y=0
                                            a=t.split(" ")
                                            while True:
                                                try:
                                                    tm=self.macros[y]
                                                    if tm.check(a[1]):
                                                        self.macros.remove(tm)
                                                        arr[x]=""
                                                        temp="\n".join(arr)
                                                        arr=temp.split("\n")
                                                        return arr
                                                    else:
                                                        y+=1
                                                except:
                                                    break
                    elif t[1]=="i":
                        if t[2]=="n":
                            if t[3]=="c":
                                if t[4]=="l":
                                    if t[5]=="u":
                                        if t[6]=="d":
                                            if t[7]=="e":
                                                if t[8]==" ":
                                                    a=t.split(" ")
                                                    b=open(a[1]+".jh")
                                                    arr[x]=b.read()
                                                    tm=arr[x]
                                                    arr[x]=tm[:-1]
                                                    b.close()
                                                    temp="\n".join(arr)
                                                    arr=temp.split("\n")
                                                    return arr
                        #elif t[2]=="f":
                            #if t[3]=="_":
                                #if t[4]=="d":
                                    #if t[5]=="e":
                                        #if t[5]=="f":
                                            #if t[6]==" ":
                                                
                x+=1
            except:
                a=open(name+".gold_com","w")
                a.write("\n".join(arr))
                #a.write(arr)
                a.close()
                print("wrote to file")
                return 456
    def directives(self,inp):
        inpt=inp.split(" ")
        name=inpt[0]
        a=self.read(name)
        objfiles=inpt[1]
        while True:
            a=self.directive_parse(a,name)
            if objfiles=="true":
                if not a==453:
                    b=open(name+".gold_obj","w")
                    b.write("\n".join(a))
                    b.close()
                    input()
            if a==456:
                print("breaking main directives")
                break
if __name__=="__main__":
    a=preprocessor()
    a.directives(input())
