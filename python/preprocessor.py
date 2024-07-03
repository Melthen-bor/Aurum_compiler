import os
class macro:
    def __init__(self,name,content,var):
        self.name=name;
        self.content=content
        self.var=var;
    def check(self,name):
        if self.name==name:
            return True
        else:
            return False
    def get_content(self,var):
        variable_amount=len(var)
        temp_list=self.content.split(" ")
        variable_count=0
        amount=len(temp_list)
        while variable_count<variable_amount:
            count=0
            while count<amount:
                check=temp_list[count]
                if check==self.var[variable_count]:
                    temp_list[count]=var[variable_count]
                count+=1
            variable_count+=1
        return " ".join(temp_list)
class preprocessor:
    def __init__(self,in_ext,mid_ext,out_ext):
        self.macros=[]
        self.in_files=[]
        self.in_name=in_ext
        self.mid_name=mid_ext
        self.out_name=out_ext
        self.runs=-1
    def read(self,name):
        a=open(name+"."+self.in_name)
        b=a.read()
        a.close()
        return b.split("\n")
    def directive_parse(self,arr,name,lang,direct,test):
        self.runs+=1
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
                                    varlist=a
                                    varlist.remove(0)
                                    varlist.remove(0)
                                    while True:
                                        try:
                                            tm=self.macros[y]
                                            if tm.check(a[1]):
                                                arr[x]=tm.get_content(varlist)
                                                temp="\n".join(arr)
                                                arr=temp.split("\n")
                                                print("\033[38;2;0;255;0mPlaced macro["+a[1]+"] on line:"+str(x)+"\033[0m")
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
                                                            varlist=nm
                                                            varlist.remove(0)
                                                            varlist.remove(0)
                                                            while True:
                                                                a=arr[x+y]
                                                                if a=="#end_def":
                                                                    self.macros+=[macro(nm[1],tm,varlist)]
                                                                    temp=""
                                                                    z=0
                                                                    while True:
                                                                        try:
                                                                            if not z==0:
                                                                                temp+="\n"
                                                                            if z==x:
                                                                                z+=y+1
                                                                            temp+=arr[z]
                                                                            z+=1
                                                                        except:
                                                                            break
                                                                    print("\033[38;2;0;255;0mMacro["+nm[1]+"] defined\033[0m")
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
                                        varlist=a
                                        varlist.remove(0)
                                        varlist.remove(0)
                                        while True:
                                            try:
                                                tm=self.macros[y]
                                                if tm.check(a[1]):
                                                    arr[x]=tm.get_content(varlist)
                                                    self.macros.remove(tm)
                                                    temp="\n".join(arr)
                                                    arr=temp.split("\n")
                                                    print("\033[38;2;0;255;0mMoved macro["+a[1]+"] with arguments["+",".join(varlist)+"to:"+str(x)+"\033[0m")
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
                                                        print("\033[38;2;0;255;0mMacro["+a[1]+"] removed\033[0m")
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
                                                    try:
                                                        index=self.in_files.index(direct+a[1]+".header")
                                                        b=open(a[1]+".header")
                                                        tm=b.read()
                                                        arr[x]=tm[:-1]
                                                        b.close()
                                                        self.in_files+=[direct+a[1]+".header"]
                                                        print("\033[38;2;0;255;0mHeader["+direct+a[1]+"]included\033[0m")
                                                    except:
                                                        arr[x]=''
                                                    temp='\n'.join(arr)
                                                    arr=temp.split('\n')
                                                    return arr
                                                elif t[8]=="_":
                                                    if t[9]=="e":
                                                        if t[10]=="x":
                                                            a=t.split(" ")
                                                            try:
                                                                index=self.in_files.index(direct+a[1])
                                                                b=open(a[1])
                                                                tm=b.read()
                                                                arr[x]=tm[:-1]
                                                                b.close()
                                                                self.in_files+=[a[1]]
                                                                print("\033[38;2;0;255;0mFile["+direct+a[1]+"]included\033[0m")
                                                            except:
                                                                arr[x]=''
                                                            temp='\n'.join(arr)
                                                            arr=temp.split('\n')
                                                            return arr
                        elif t[2]=="f":
                            if t[3]=="_":
                                if t[4]=="d":
                                    if t[5]=="e":
                                        if t[6]=="f":
                                            if t[7]==" ":
                                                y=0
                                                a=t.split(" ")
                                                while True:
                                                    try:
                                                        print("finding macro")
                                                        tm=self.macros[y]
                                                        if tm.check(a[1]):
                                                            print("placing macro")
                                                            arr[x]=tm.content
                                                            arr="\n".join(arr).split("\n")
                                                            self.macros.remove(y)
                                                            return arr
                                                        else:
                                                            y+=1
                                                    except:
                                                        break
                                                arr.remove(x)
                                                arr="\n".join(arr).split("\n")
                    elif t[1]=="c":
                        if t[2]=="p":
                            if t[3]=="p":
                                if t[4]==" ":
                                    if lang=="c_plus_plus":
                                        ts=t.split(" ")
                                        ts.remove(0)
                                        t=" ".join(ts)
                                        arr[x]=t
                                        return arr
                                    arr.remove(x)
                                    arr="\n".join(arr).split("\n")
                                elif t[4]=="_":
                                    if t[5]=="h":
                                        if t[6]=="e":
                                            if t[7]=="a":
                                                if t[8]=="d":
                                                    if t[9]=="e":
                                                        if[10]=="r":
                                                            if t[11]==" ":
                                                                if lang=="c_plus_plus_header":
                                                                    ts=t.split(" ")
                                                                    ts.remove(0)
                                                                    t=" ".join(ts)
                                                                    arr[x]=t
                                                                    return arr
                                                                arr.remove(x)
                                                                arr="\n".join(arr).split("\n")
                    elif t[1]=="z":
                        if t[2]=="d":
                            if t[3]=="r":
                                if t[4]=="i":
                                    if t[5]=="n":
                                        if t[6]=="g":
                                            if test:
                                                arr[x]=="sysout << \"zdring_test line:"+str(x)+",run:"+str(self.runs)+"\" ;"
                                            else:
                                                arr.remove(x)
                                            arr="\n".join(arr).split("\n")
                elif t[0]=="!":
                    arr.remove(x)
                    return arr
                x+=1
            except:
                a=open(direct+name+"."+self.out_name,"w")
                a.write("\n".join(arr))
                a.close()
                print("\033[38;2;0;255;0mPreprocessing finished\033[0m")
                return 456
    def opt_parse(self,arr,name,lang,direct,test):
        return self.directive_parse(arr,name,lang,direct,test)
        tempstring=""
        index=0
        """
                                                            y=1
                                                            tm=""
                                                            nm=t.split(" ")
                                                            varlist=nm
                                                            varlist.remove(0)
                                                            varlist.remove(0)
                                                            while True:
                                                                a=arr[x+y]
                                                                if a=="#end_def":
                                                                    self.macros+=[macro(nm[1],tm,varlist)]
                                                                    temp=""
                                                                    z=0
                                                                    while True:
                                                                        try:
                                                                            if not z==0:
                                                                                temp+="\n"
                                                                            if z==x:
                                                                                z+=y+1
                                                                            temp+=arr[z]
                                                                            z+=1
                                                                        except:
                                                                            break
                                                                    print("\033[38;2;0;255;0mMacro["+nm[1]+"] defined\033[0m")
                                                                    break
                                                                else:
                                                                    if not y==1:
                                                                        tm+="\n"
                                                                    tm+=a
                                                                    y+=1
                                                            arr=temp.split("\n")
                                                            return arr
        """
        while True:
            try:
                temp=arr[index]
                match temp[0]:
                    case "#":
                        match temp[1]:
                            case "p":
                                match temp[2]:
                                    case "u":
                                        match temp[3]:
                                            case "t":
                                                match temp[4]:
                                                    case " ":
                                                        x=0
                                                        a=arr.split(" ")
                                                        varlist=a
                                                        varlist.remove(0)
                                                        varlist.remove(0)
                                                        while True:
                                                            try:
                                                                tm=self.macros[x]
                                                                if tm.check(a[1]):
                                                                    arr[index]=tm.get_content(varlist)
                                                                    arr=("\n".join(arr)).split("\n")
                                                                    print("\033[38;2;0;255;0mPlaced macro["+a[1]+"] on line:"+str(index)+"\033[0m")
                                                                    return arr
                                                                x+=1
                                                            except:
                                                                break
                                                    case _:
                                                        pass
                                            case _:
                                                pass
                                    case _:
                                        pass
                            case "m":
                                match temp[2]:
                                    case "o":
                                        match temp[3]:
                                            case "v":
                                                match temp[4]:
                                                    case "e":
                                                        match temp[5]:
                                                            case " ":
                                                                x=0
                                                                a=arr.split(" ")
                                                                varlist=a
                                                                varlist.remove(0)
                                                                varlist.remove(0)
                                                                while True:
                                                                    try:
                                                                        tm=self.macros[x]
                                                                        if tm.check(a[1]):
                                                                            arr[index]=tm.get_content(varlist)
                                                                            arr=("\n".join(arr)).split("\n")
                                                                            self.macros.remove(tm)
                                                                            print("\033[38;2;0;255;0mMoved macro["+a[1]+"] to line:"+str(index)+"\033[0m")
                                                                            return arr
                                                                        x+=1
                                                                    except:
                                                                        break
                                                            case _:
                                                                pass
                                                    case _:
                                                        pass
                                            case _:
                                                pass
                                    case _:
                                        pass
                            case "c":
                                pass
                            case "i":
                                pass
                            case "s":
                                match temp[2]:
                                    case "t":
                                        match temp[3]:
                                            case "a":
                                                match temp[4]:
                                                    case "r":
                                                        match temp[5]:
                                                            case "t":
                                                                match temp[6]:
                                                                    case "_":
                                                                        match temp[7]:
                                                                            case "d":
                                                                                match temp[8]:
                                                                                    case "e":
                                                                                        match temp[9]:
                                                                                            case "f":
                                                                                                match temp[10]:
                                                                                                    case " ":
                                                                                                        x=1
                                                                                                        tm=""
                                                                                                        nm=temp.split(" ")
                                                                                                        varlist=nm
                                                                                                        varlist.remove(0)
                                                                                                        varlist.remove(0)
                                                                                                        while True:
                                                                                                            pass
                                                                                                    case _:
                                                                                                        pass
                                                                                            case _:
                                                                                                pass
                                                                                    case _:
                                                                                        pass
                                                                            case _:
                                                                                pass
                                                                    case _:
                                                                        pass
                                                            case _:
                                                                pass
                                                    case _:
                                                        pass
                                            case _:
                                                pass
                                    case _:
                                        pass
                            case "u":
                                pass
                            case "z":
                                pass
                            case _:
                                pass
                    case "!":
                        arr.remove(index)
                        return arr
                    case _:
                        pass
                index+=1
            except:
                file=open(direct+name+"."+self.out_name,"w")
                file.write("\n".join(arr))
                file.close()
                print("\033[38;2;0;255;0mPreprocessing finished\033[0m")
                return 456
    def directives(self,inp,obj,lang,direct,opt,test):
        name=inp
        a=self.read(direct+name)
        self.runs=-1
        while True:
            a=self.directive_parse(a,name,lang,direct,test)
            if obj:
                if not a==456:
                    b=open(direct+name+"."+self.mid_name,"w")
                    b.write("\n".join(a))
                    b.close()
                    input()
                    os.remove(direct+name+"."+self.mid_name)
            if a==456:
                break
if __name__=="__main__":
    a=preprocessor("jpp","jobj","java")
    a.directives(input(),(input()=="obj"),"java","",(input()=="test"))