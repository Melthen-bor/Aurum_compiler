class compilerGold():
    def __init__(self):
        self.count=0
        self.strlist=[]
        self.templist=[]
    def read(self,file):
        inpfile=open(file)
        strtemp=inpfile.read()
        inpfile.close()
        tlist=strtemp.split("\n");
        strtemp=" ".join(tlist)
        return strtemp
    def tokenizeGold(self,file):
        strtemp=self.read(file)
        self.templist=strtemp.split(" ")
        self.count=len(self.templist)
        counter=0
        count=self.count
        while counter<count:
            strtemp=self.templist[counter]
            match strtemp:
                case "if":
                    self.strlist+=["IF_TOKEN_GOLD"]
                case "else":
                    self.strlist+=["ELSE_TOKEN_GOLD"]
                case ";":
                    self.strlist+=["ENDSTATEMENT_TOKEN_GOLD"]
                case "start":
                    self.strlist+=["STARTBLOCK_TOKEN_GOLD"]
                case "end":
                    self.strlist+=["ENDBLOCK_TOKEN_GOLD"]
                case "while":
                    self.strlist+=["WHILE_TOKEN_GOLD"]
                case "+=":
                    self.strlist+=["ADDASI_TOKEN_GOLD"]
                case "<<":
                    self.strlist+=["OUTSTREAM_TOKEN_GOLD"]
                case ">>":
                    self.strlist+=["INSTREAM_TOKEN_GOLD"]
                case "sysout":
                    self.strlist+=["SYSTEMOUT_TOKEN_GOLD"]
                case "sysin":
                    self.strlist+=["SYSTEMIN_TOKEN_GOLD"]
                case "file":
                    self.strlist+=["FILESTREAM_TOKEN_GOLD"]
                case "=":
                    self.strlist+=["ASSIGNMENT_TOKEN_GOLD"]
                case "inputhandler":
                    self.strlist+=["SYSTEMIN_TOKEN_GOLD"]
                case "class":
                    self.strlist+=["CLASS_TOKEN_GOLD"]
                case "function":
                    self.strlist+=["FUNCTION_TOKEN_GOLD"]
                case "initIO":
                    self.strlist+=["INITIO_TOKEN_GOLD"]
                case "use":
                    self.strlist+=["USE_TOKEN_GOLD"]
                case "return":
                    self.strlist+=["RETURN_TOKEN_GOLD"]
                case "elf":
                    self.strlist+=["ELIF_TOKEN_GOLD"]
                case "bool":
                    self.strlist+=["BOOL_TOKEN_GOLD"]
                case "int":
                    self.strlist+=["INT_TOKEN_GOLD"]
                case "close":
                    self.strlist+=["CLOSE_TOKEN_GOLD"]
                case "try":
                    self.strlist+=["TRY_TOKEN_GOLD"]
                case "except":
                    self.strlist+=["EXCEPT_TOKEN_GOLD"]
                case "cons":
                    self.strlist+=["CONSTRUCTOR_TOKEN_GOLD"]
                case "member":
                    self.strlist+=["MEMBER_TOKEN_GOLD"]
                case "import":
                    self.strlist+=["IMPORT_TOKEN_GOLD"]
                case "create":
                    self.strlist+=["CREATE_TOKEN_GOLD"]
                case "++":
                    self.strlist+=["INCREMENT_TOKEN_GOLD"]
                case "--":
                    self.strlist+=["DECREMENT_TOKEN_GOLD"]
                case "false":
                    self.strlist+=["FALSE_TOKEN_GOLD"]
                case "true":
                    self.strlist+=["TRUE_TOKEN_GOLD"]
                case "str":
                    self.strlist+=["STRING_TOKEN_GOLD"]
                case "[!":
                    self.strlist+=["BEGINCOMMENT_TOKEN_GOLD"]
                case "!]":
                    self.strlist+=["ENDCOMMENT_TOKEN_GOLD"]
                case "program":
                    self.strlist+=["PROGRAM_TOKEN_GOLD"]
                case "\_":
                    self.strlist+=["SPACE_TOKEN_GOLD"]
                case "\~":
                    self.strlist+=["NONE_TOKEN_GOLD"]
                case "contains":
                    self.strlist+=["CONTAINS_TOKEN_GOLD"]
                case "&*":
                    self.strlist+=["POINTER_TOKEN_GOLD"]
                case "access":
                    self.strlist+=["GETATTRIBUTE_TOKEN_GOLD"]
                case "&>":
                    self.strlist+=["GETATTRIBUTE_TOKEN_GOLD"]
                case "->":
                    self.strlist+=["POINTERATTRIBUTE_TOKEN_GOLD"]
                case "-=":
                    self.strlist+=["SUBTRACTIONASSIGNMENT_TOKEN_GOLD"]
                case "@STACK_TO_HEAP":
                    self.strlist+=["STACK_TO_HEAP_TOKEN_GOLD_COMPILER"]
                case "-":
                    self.strlist+=["SUBTRACTION_TOKEN_GOLD"]
                case "create[]":
                    self.strlist+=["CREATEARRAY_TOKEN_GOLD"]
                case "destroy":
                    self.strlist+=["DESTROY_TOKEN_GOLD"]
                case "delete":
                    self.strlist+=["DELETE_TOKEN_GOLD"]
                case "delete[]":
                    self.strlist+=["DELETEARRAY_TOKEN_GOLD"]
                case "@HEAP_TO_STACK":
                    self.strlist+=["HEAP_TO_STACK_TOKEN_GOLD_COMPILER"]
                case "decons":
                    self.strlist+=["DECONSTRUCTOR_TOKEN_GOLD"]
                case _:
                    self.strlist+=[strtemp]
            counter+=1
        self.templist=[]
    def indentGold(self,amount):
        counter=0
        ret=""
        while counter<amount:
            ret+="  "
            counter+=1
        return ret
    def find_var(self,varis,var):
        a=0
        while 1==1:
            b=varis[a]
            if b==var:
                return a
            b+=1
        return "death"
    def compileCpp(self,file):
        outfile=open(file,mode="w+")
        count=self.count
        lists=self.strlist
        counter=0
        clist=file.split(".")
        clist=clist[:-1]
        cname=".".join(clist)
        counter_o=0
        blocks=[]
        stack=[]
        stack_type=[]
        heap=[]
        heap_type=[]
        outstring="#include <iostream>\n#include <fstream>\n#include <string>\nusing namespace std;\n"
        while counter<count:
            tempstring=lists[counter]
            if tempstring=="ENDBLOCK_TOKEN_GOLD":
                tempstring=blocks.pop()
                if tempstring=="program":
                    while 1==1:
                        if len(stack)==0:
                            break
                        else:
                            tempstring=stack_type.pop()
                            if tempstring=="scaler":
                                outstring+="delete "
                                outstring+=stack.pop()
                                outstring+=";\n"
                                outstring+=self.indentGold(counter_o)
                            elif tempstring=="array":
                                outstring+="delete[] "
                                outstring+=stack.pop()
                                outstring+=";\n"
                                outstring+=self.indentGold(counter_o)
                            else:
                                return 2
                    outstring+="return 0\n"
                    outstring+=self.indentGold(counter_o)
                    outstring+="}\n"
                    counter_o-=1
                    outstring+=self.indentGold(counter_o)
                elif tempstring=="constructor":
                    while 1==1:
                        if len(stack)==0:
                            break;
                        else:
                            tempstring=stack_type.pop()
                            if tempstring=="scaler":
                                outstring+="delete "
                                outstring+=stack.pop()
                                outstring+=";\n"
                                outstring+=self.indentGold(counter_o)
                            elif tempstring=="array":
                                outstring+="delete[] "
                                outstring+=stack.pop()
                                outstring+=";\n"
                                outstring+=self.indentGold(counter_o)
                            else:
                                return 2
                    outstring+="}\n"
                    counter_o-=1
                    outstring+=self.indentGold(counter_o)
                elif tempstring=="deconstructor":
                    while 1==1:
                        if len(stack)==0:
                            break
                        else:
                            tempstring=stack_type.pop()
                            if tempstring=="scaler":
                                outstring+="delete "
                                outstring+=stack.pop()
                                outstring+=";\n"
                                outstring+=self.indentGold(counter_o)
                            elif tempstring=="array":
                                outstring+="delete[] "
                                outstring+=stack.pop()
                                outstring+=";\n"
                                outstring+=self.indentGold(counter_o)
                            else:
                                return 2
                    outstring+="}\n"
                    counter_o-=1
                    outstring+=self.indentGold(counter_o)
                elif tempstring=="function":
                    counter_o-=1
                    outstring+="}\n"
                    outstring+=self.indentGold(counter_o)
                elif tempstring=="class":
                    tl=list(outstring)
                    tl.pop()
                    tl.pop()
                    outstring="".join(tl)
                    outstring+="};\n"
                    counter_o-=1
                    outstring+=self.indentGold(counter_o)
                elif tempstring=="contains":
                    pass
                else:
                    counter_o-=1
                    tl=list(outstring)
                    tl.pop()
                    tl.pop()
                    outstring="".join(tl)
                    outstring+="}\n"
                    outstring+=self.indentGold(counter_o)
            elif tempstring=="STARTBLOCK_TOKEN_GOLD":
                counter_o+=1
                outstring+="{\n"
                outstring+=self.indentGold(counter_o)
            elif tempstring=="ENDSTATEMENT_TOKEN_GOLD":
                outstring+=";\n"
                outstring+=self.indentGold(counter_o)
            elif tempstring=="PROGRAM_TOKEN_GOLD":
                outstring+="int main()"
                blocks+=["program"]
            elif tempstring=="IF_TOKEN_GOLD":
                counter+=1
                tempstring=lists[counter]
                outstring+="if("
                outstring+=tempstring
                outstring+=")"
            elif tempstring=="SYSTEMOUT_TOKEN_GOLD":
                counter+=1
                tempstring=lists[counter]
                if tempstring=="OUTSTREAM_TOKEN_GOLD":
                    counter+=1
                    tempstring=lists[counter]
                    tlist=tempstring.split("\_")
                    tempstring=" ".join(tlist)
                    tlist=tempstring.split("\~")
                    tempstring="".join(tlist)
                    outstring+="cout << "
                    outstring+=tempstring
                else:
                    outfile.close()
                    return 1
            elif tempstring=="SYSTEMIN_TOKEN_GOLD":
                counter+=1
                tempstring=lists[counter]
                if tempstring=="INSTREAM_TOKEN_GOLD":
                    counter+=1
                    tempstring=lists[counter]
                    outstring+="cin >> "
                    outstring+=tempstring
                else:
                    outfile.close()
                    return 1
            elif tempstring=="INITIO_TOKEN_GOLD":
                counter+=1
            elif tempstring=="CLASS_TOKEN_GOLD":
                outstring+="class "
                outstring+=cname
            elif tempstring=="FUNCTION_TOKEN_GOLD":
                counter+=1
                tempstring=lists[counter]
                if tempstring=="BOOL_TOKEN_GOLD":
                    tempstring="bool"
                elif tempstring=="NONE_TOKEN_GOLD":
                    tempstring="void"
                elif tempstring=="INT_TOKEN_GOLD":
                    tempstring="int"
                elif tempstring=="STRING_TOKEN_GOLD":
                    tempstring=="string"
                else:
                    tlist=tempstring.split("str")
                    tempstring="string".join(tlist)
                    tlist=tempstring.split("&*")
                    tempstring="*".join(tlist)
                outstring+=tempstring
                outstring+=" "
                counter+=1
                tempstring=lists[counter]
                outstring+=tempstring
                outstring+="("
                counter+=1
                tempstring=lists[counter]
                tlist=tempstring.split("\_")
                tempstring=" ".join(tlist)
                tlist=tempstring.split("\~")
                tempstring="".join(tlist)
                outstring+=tempstring
                outstring+=")"
                blocks+=["function"]
            elif tempstring=="ELIF_TOKEN_GOLD":
                tl=list(outstring)
                tl.pop()
                tl.pop()
                outstring="".join(tl)
                outstring+="} else if("
                counter+=1
                tempstring=lists[counter]
                outstring+=tempstring
                outstring+=")"
                counter_o-=1
            elif tempstring=="ELSE_TOKEN_GOLD":
                tl=list(outstring)
                tl.pop()
                tl.pop()
                outstring="".join(tl)
                outstring+="} else"
                counter_o-=1
            elif tempstring=="USE_TOKEN_GOLD":
                counter+=1
                tempstring=lists[counter]
                outstring+=tempstring
                outstring+="("
                counter+=1
                tempstring=lists[counter]
                tl=tempstring.split("&>")
                tempstring="this->".join(tl)
                tl=tempstring.split("->")
                tempstring="->".join(tl)
                tl=tempstring.split("\_")
                tempstring=" ".join(tl)
                tl=tempstring.split("\~")
                tempstring=tl.join(tl)
                outstring+=tempstring
                outstring+=")"
            elif tempstring=="STRING_TOKEN_GOLD":
                outstring+="string "
            elif tempstring=="INCREMENT_TOKEN_GOLD":
                outstring+="++"
            elif tempstring=="DECREMENT_TOKEN_GOLD":
                outstring+="--"
            elif tempstring=="ADDASI_TOKEN_GOLD":
                outstring+="+="
            elif tempstring=="ASSIGNMENT_TOKEN_GOLD":
                outstring+="="
            elif tempstring=="FALSE_TOKEN_GOLD":
                outstring+="false"
            elif tempstring=="TRUE_TOKEN_GOLD":
                outstring+="true"
            elif tempstring=="TRY_TOKEN_GOLD":
                outstring+="try"
                blocks+=["try"]
            elif tempstring=="EXCEPT_TOKEN_GOLD":
                counter+=1
                ls=list(outstring)
                ls.pop()
                ls.pop()
                outstring="".join(ls)
                outstring+="} catch(...)"
            elif tempstring=="RETURN_TOKEN_GOLD":
                while 1==1:
                    if len(stack)==0:
                        break
                    else:
                        tempstring=stack_type.pop()
                        if tempstring=="scaler":
                            outstring+="delete "
                            outstring+=stack.pop()
                            outstring+=";\n"
                            outstring+=self.indentGold()
                        elif tempstring=="array":
                            outstring+="delete[] "
                            outstring+=stack.pop()
                            outstring+=";\n"
                            outstring+=self.indentGold()
                        else:
                            return 2
                outstring+="return "
            elif tempstring=="BEGINCOMMENT_TOKEN_GOLD":
                while 1==1:
                    counter+=1
                    tempstring=lists[counter]
                    if tempstring=="ENDCOMMENT_TOKEN_GOLD":
                        break
            elif tempstring=="FILESTREAM_TOKEN_GOLD":
                counter+=1
                tempstring=lists[counter]
                counter+=1
                tstr=lists[counter]
                counter+=1
                tempstr=lists[counter]
                tstrIn=tempstring+"IN"
                tstrOut=tempstring+"OUT"
                if tstr=="ASSIGNMENT_TOKEN_GOLD":
                    outstring+="ifstream "
                    outstring+=tstrIn
                    outstring+="("
                    outstring+=tstrt
                    outstring+=");\n"
                    outstring+=self.indentGold(counter_o)
                    outstring+="ofstream "
                    outstring+=tstrOut
                    outstring+="("
                    outstring+=tstrt
                    outstring+=")"
                elif tstr=="OUTSTREAM_TOKEN_GOLD":
                    outstring+=tstrOut
                    outstring+="<<"
                    outstring+=tstrt
                elif tstr=="INSTREAM_TOKEN_GOLD":
                    outstring+=tstrIn
                    outstring+=">>"
                    outstring+=tstrt
                elif tstr=="CLOSE_TOKEN_GOLD":
                    outstring+=tstrOut
                    outstring+=".close();\n"
                    outstring+=self.indentGold(counter_o)
                    outstring+=tstrIn
                    outstring+=".close()"
            elif tempstring=="BOOL_TOKEN_GOLD":
                outstring+="bool "
            elif tempstring=="INT_TOKEN_GOLD":
                outstring+="int "
            elif tempstring=="CONTAINS_TOKEN_GOLD":
                ls=list(outstring)
                ls.pop()
                ls.pop()
                outstring="".join(ls)
                outstring+="public:"
                counter_o-=1
                blocks+=["contains"]
            elif tempstring=="MEMBER_TOKEN_GOLD":
                pass
            elif tempstring=="CONSTRUCTOR_TOKEN_GOLD":
                outstring+=cname
                outstring+="("
                counter+=1
                tempstring=lists[counter]
                if tempstring=="NONE_TOKEN_GOLD":
                    tempstring=""
                else:
                    tlist=tempstring.split("str")
                    tempstring="string".join(tempstring)
                    tlist=tempstring.split("\_")
                    tempstring=" ".join(tempstring)
                    tlist=tempstring.split("\~")
                    tempstring="".join(tlist)
                outstring+=tempstring
                outstring+=")"
                blocks+=["constructor"]
            elif tempstring=="WHILE_TOKEN_GOLD":
                outstring+="while("
                counter+=1
                tempstring=lists[counter]
                outstring+=tempstring
                outstring+=")"
                blocks+=["while"]
            elif tempstring=="CREATE_TOKEN_GOLD":
                counter+=1
                tempstring=lists[counter]
                tlist=tempstring.split("&>")
                tempstring="this->".join(tlist)
                outstring+=tempstring
                stack+=[tempstring]
                stack_type+=["scaler"]
                outstring+="=new "
                counter+=1
                tempstring=lists[counter]
                outstring+=tempstring
                outstring+="("
                counter+=1
                tempstring=lists[counter]
                if tempstring=="NONE_TOKEN_GOLD":
                    tempstring=""
                else:
                    tlist=tempstring.split("\_")
                    tempstring=" ".join(tlist)
                    tlist=tempstring.split("\~")
                    tempstring="".join(tlist)
                outstring+=tempstring
                outstring+=")"
            elif tempstring=="POINTER_TOKEN_GOLD":
                outstring+="*"
            elif tempstring=="GETATTRIBUTE_TOKEN_GOLD":
                outstring+="this->"
            elif tempstring=="POINTERATTRIBUTE_TOKEN_GOLD":
                outstring+="->"
            elif tempstring=="SUBTRACTIONASSIGNMENT_TOKEN_GOLD":
                outstring+="-="
            elif tempstring=="STACK_TO_HEAP_TOKEN_GOLD_COMPILER":
                heap+=[stack.pop()]
                heap_type+=[stack_type.pop()]
            elif tempstring=="SUBTRACTION_TOKEN_GOLD":
                outstring+="-"
            elif tempstring=="CREATEARRAY_TOKEN_GOLD_TOKEN_GOLD":
                counter+=1
                tempstring=lists[counter]
                tlist=tempstring.split("&>")
                tempstring="this->".join(tlist)
                outstring+=tempstring
                stack+=[tempstring]
                stack_type+=["array"]
                outstring+="=new "
                counter+=1
                tempstring=lists[counter]
                if tempstring=="INT_TOKEN_GOLD":
                    tempstring="int"
                elif tempstring=="STRING_TOKEN_GOLD":
                    tempstring="string"
                elif tempstring=="BOOL_TOKEN_GOLD":
                    tempstring="bool"
                outstring+=tempstring
                temp=tempstring
                outstring+="["
                counter+=1
                tempstring=lists[counter]
                tlist=tempstring.split("&>")
                tempstring="this->".join(tlist)
                tlist=tempstring.split("&*")
                tempstring="*".join(tlist)
                outstring+=tempstring
                outstring+="]{"
                outstring+=temp
                outstring+="("
                counter+=1
                tempstring=lists[counter]
                if tempstring=="NONE_TOKEN_GOLD":
                    tempstring=""
                else:
                    tl=tempstring.split("\_")
                    tempstring=" ".join(tl)
                    tl=tempstring.split("\~")
                    tempstring="".join(tl)
                outstring+=tempstring
                outstring+=")}"
            elif tempstring=="DESTROY_TOKEN_GOLD":
                counter+=1
                tempstring=lists[counter]
                tlist=tempstring.split("&>")
                tempstring="this->".join(tlist)
                temp=self.find_vars(heap,tempstring)
                if temp=="death":
                    return 3
                heap.pop(temp)
                tstr=heap_type.pop(temp)
                if tstr=="scaler":
                    outstring+="delete "
                elif tstr=="array":
                    outstring+="delete[] "
                outstring+=tempstring
            elif tempstring=="DELETE_TOKEN_GOLD":
                counter+=1
                tempstring=lists[counter]
                tlist=tempstring.split("&>")
                tempstring="this->".join(tlist)
                temp=self.find_vars(heap,tempstring)
                if not(temp=="death"):
                    heap.pop(temp)
                    heap_type.pop(temp)
                outstring+="delete[] "
                outstring+=tempstring
            elif tempstring=="DELETEARRAY_TOKEN_GOLD":
                counter+=1
                tempstring=lists[counter]
                tlist=tempstring.split("&>")
                tempstring="this->".join(tlist)
                temp=self.find_vars(heap,tempstring)
                if not(temp=="death"):
                    heap.pop(temp)
                    heap_stack.pop(temp)
                outstring+="delete "
                outstring+=tempstring
            elif tempstring=="HEAP_TO_STACK_TOKEN_GOLD_COMPILER":
                counter+=1
                tempstring=lists[counter]
                tlist=tempstring.split("&>")
                tempstring="this->".join(tlist)
                temp=self.find_vars(heap,tempstring)
                if temp=="death":
                    return 3
                stack+=[heap.pop(temp)]
                stack_type+=[heap_type.pop(temp)]
            elif tempstring=="DECONSTRUCTOR_TOKEN_GOLD":
                outstring+="~"
                outstring+=cname
                outstring+="()"
                blocks+=["deconstructor"]
            else:
                outstring+=tempstring
            counter+=1
        outfile.write(outstring)
        outfile.close()
        return 0
    def compileFort(self,file):
        outfile=open(file,mode="w+")
        count=self.count
        lists=self.strlist
        tempstring=""
        tempstr=""
        counter=0
        clist=file.split(".")
        clist=clist[:-1]
        cname=".".join(clist)
        counter_o=0
        counter_c=0
        blocks=[]
        streams=["","","","","","",""]
        outstring=""
        while counter<count:
            tempstring=lists[counter]
            if tempstring=="ENDBLOCK_TOKEN_GOLD":
                counter_o-=1
                tl=list(outstring)
                tl.pop()
                tl.pop()
                outstring="".join(tl)
                outstring+="end "
                outstring+=blocks.pop()
                outstring+="\n"
                outstring+=self.indentGold(counter_o)
            elif tempstring=="STARTBLOCK_TOKEN_GOLD":
                counter_o+=1
                outstring+="\n"
                outstring+=self.indentGold(counter_o)
            elif tempstring=="ENDSTATEMENT_TOKEN_GOLD":
                outstring+="\n"
                outstring+=self.indentGold(counter_o)
            elif tempstring=="SYSTEMOUT_TOKEN_GOLD":
                counter+=1
                tempstring=lists[counter]
                if tempstring=="OUTSTREAM_TOKEN_GOLD":
                    counter+=1
                    tempstring=lists[counter]
                    tlist=tempstring.split("\_")
                    tempstring=" ".join(tlist)
                    tlist=tempstring.split("\~")
                    tempstring="".join(tlist)
                    outstring+="write(*,*) "
                    outstring+=tempstring
                else:
                    outfile.close()
                    return 1
            elif tempstring=="SYSTEMIN_TOKEN_GOLD":
                counter+=1
                tempstring=lists[counter]
                if tempstring=="INSTREAM_TOKEN_GOLD":
                    counter+=1
                    tempstring=lists[counter]
                    tlist=tempstring.split("\_")
                    tempstring=" ".join(tlist)
                    tlist=tempstring.split("\~")
                    tempstring="".join(tlist)
                    outstring+="read(*,*) "
                    outstring+=tempstring
                else:
                    outfile.close()
                    return 1
            elif tempstring=="INITIO_TOKEN_GOLD":
                counter+=1
            elif tempstring=="CLASS_TOKEN_GOLD":
                outstring+="type::"
                outstring+=cname
                outstring+="_"
                outstring+=str(counter_c)
                counter_c+=1
                blocks+=["type"]
            elif tempstring=="FUNCTION_TOKEN_GOLD":
                counter+=1
                tempstring=lists[counter]
                outstring+="function "
                outstring+=tempstring
                counter+=1
                tempstring=lists[counter]
                outstring+="("
                outstring+=tempstring
                outstring+=")"
                blocks+=["function"]
            elif tempstring=="INT_TOKEN_GOLD":
                counter+=1
                tempstring=lists[counter]
                outstring+="integer::"
                outstring+=tempstring
            elif tempstring=="IF_TOKEN_GOLD":
                counter+=1
                tempstring=lists[counter]
                outstring+="if ("
                outstring+=tempstring
                outstring+=") then"
                blocks+=["if"]
            elif tempstring=="WHILE_TOKEN_GOLD":
                counter+=1
                tempstring=lists[counter]
                outstring+="do while ("
                outstring+=tempstring
                outstring+= ")"
                blocks+=["do"]
            elif tempstring=="BEGINCOMMENT_TOKEN_GOLD":
                while 1==1:
                    counter+=1
                    tempstring=lists[counter]
                    if tempstring=="ENDCOMMENT_TOKEN_GOLD":
                        break
            elif tempstring=="PROGRAM_TOKEN_GOLD":
                tempstring="program "
                tempstring+=cname
                outstring+=tempstring
                blocks+=[tempstring]
            else:
                count=counter+1
                ts=list[count]
                if ts=="ADDASI_TOKEN_GOLD":
                    counter+=2
                    outstring+=tempstring
                    outstring+=" = "
                    outstring+=tempstring
                    outstring+=" + "
                    tempstring=list[counter]
                    outstring+=tempstring
                elif ts=="INCREMENT_TOKEN_GOLD":
                    counter+=1
                    outstring+=tempstring
                    outstring+=" = "
                    outstring+=tempstring
                    outstring+=" + 1"
                elif ts=="DECREMENT_TOKEN_GOLD":
                    counter+=1
                    outstring+=tempstring
                    outstring+=" = "
                    outstring+=tempstring
                    outstring+=" - 1"
                else:
                    ts=tempstring.split("\_")
                    tempstring=" ".join(ts)
                    ts=tempstring.split("\~")
                    tempstring="".join(ts)
                    outfile+=tempstring
            counter+=1
        outfile.write(outstring)
        outfile.close()
        return 0
    def compileJava(self,file):
        outfile=open(file,mode="w+")
        count=self.count
        lists=self.strlist
        tempstring=""
        tempstr=""
        counter=0
        outstring="import java.util.Scanner;\nimport java.io.File;\nimport java.io.FileWriter;\n"
        counter_o=0
        clist=file.split(".")
        clist=clist[:-1]
        cname=".".join(clist)
        blocks=[]
        while counter<count:
            tempstring=lists[counter]
            if tempstring=="STARTBLOCK_TOKEN_GOLD":
                counter_o+=1
                outstring+="{\n"
                outstring+=self.indentGold(counter_o)
            elif tempstring=="ENDBLOCK_TOKEN_GOLD":
                temp=blocks.pop()
                if not (temp=="contains"):
                    counter_o-=1
                    tl=list(outstring)
                    tl.pop()
                    tl.pop()
                    outstring="".join(tl)
                    outstring+="}\n"
                    outstring+=self.indentGold(counter_o)
                    if temp=="program":
                        counter_o-=1
                        tl=list(outstring)
                        tl.pop()
                        tl.pop()
                        outstring="".join(tl)
                        outstring+="}\n"
                        outstring+=self.indentGold(counter_o)
            elif tempstring=="ENDSTATEMENT_TOKEN_GOLD":
                outstring+=";\n"
                outstring+=self.indentGold(counter_o)
            elif tempstring=="SYSTEMOUT_TOKEN_GOLD":
                counter+=1
                tempstr=lists[counter]
                if tempstr=="OUTSTREAM_TOKEN_GOLD":
                    counter+=1
                    tempstr=lists[counter]
                    tlist=tempstr.split("\_")
                    tempstr=" ".join(tlist)
                    tlist=tempstr.split("\~")
                    tempstr="".join(tlist)
                    outstring+="System.out.print("
                    outstring+=tempstr
                    outstring+=")"
                else:
                    outfile.close()
                    return 1
            elif tempstring=="SYSTEMIN_TOKEN_GOLD":
                counter+=1
                tempstr=lists[counter]
                if tempstr=="INSTREAM_TOKEN_GOLD":
                    counter+=1
                    tempstr=lists[counter]
                    outstring+=tempstr
                    outstring+="=inputhandler.nextLine()"
                else:
                    outfile.close()
                    return 1
            elif tempstring=="CLASS_TOKEN_GOLD":
                outstring+="public class "
                outstring+=cname
                blocks+=["class"]
            elif tempstring=="FUNCTION_TOKEN_GOLD":
                counter+=1
                tempstr=lists[counter]
                if tempstr=="NONE_TOKEN_GOLD":
                    tempstr="void"
                counter+=1
                tstr=lists[counter]
                counter+=1
                tempstrt=lists[counter]
                blocks+=["function"]
                if tempstrt=="NONE_TOKEN_GOLD":
                    tempstrt=""
                else:
                    tlist=tempstrt.split("bool")
                    tempstrt="boolean".join(tlist)
                    tlist=tempstrt.split("str")
                    tempstrt="String".join(tlist)
                    tlist=tempstrt.split("\_")
                    tempstrt=" ".join(tlist)
                    tlist=tempstrt.split("\~")
                    tempstrt="".join(tlist)
                outstring+="public static "
                outstring+=tempstr
                outstring+=" "
                outstring+=tstr
                outstring+="("
                outstring+=tempstrt
                outstring+=")"
            elif tempstring=="INITIO_TOKEN_GOLD":
                outstring+="Scanner inputhandler=new Scanner(System.in)"
            elif tempstring=="USE_TOKEN_GOLD":
                counter+=1
                tempstr=lists[counter]
                counter+=1
                tstr=lists[counter]
                tlist=tstr.split("&>")
                tstr="this.".join(tlist)
                tlist=tstr.split("->")
                tstr=".".join(tlist)
                tlist=tstr.split("\_")
                tstr=" ".join(tlist)
                tlist=tstr.split("\~")
                tstr="".join(tlist)
                outstring+=tempstr
                outstring+="("
                outstring+=tstr
                outstring+=")"
            elif tempstring=="RETURN_TOKEN_GOLD":
                counter+=1
                tempstring=lists[counter]
                outstring+="return "
                outstring+=tempstring
            elif tempstring=="IF_TOKEN_GOLD":
                counter+=1
                tempstring=lists[counter]
                outstring+="if("
                outstring+=tempstring
                outstring+=")"
                blocks+=["if"]
            elif tempstring=="ELIF_TOKEN_GOLD":
                outstring=outstring[:-2]
                counter_o-=1
                outstring+="} else if("
                counter+=1
                tempstring=lists[counter]
                outstring+=tempstring
                outstring+=")"
            elif tempstring=="ELSE_TOKEN_GOLD":
                counter_o-=1
                outstring=outstring[:-2]
                outstring+="} else"
            elif tempstring=="FILESTREAM_TOKEN_GOLD":
                counter+=1
                tempstring=lists[counter]
                counter+=1
                tstr=lists[counter]
                counter+=1
                tstrt=lists[counter]
                tstrIn=tempstring+"IN"
                tstrOut=tempstring+"OUT"
                tstrMain=tempstring+"MAIN"
                if tstr=="ASSIGNMENT_TOKEN_GOLD":
                    outstring+="File "
                    outstring+=tstrMain
                    outstring+="=new File("
                    outstring+=tstrt
                    outstring+=");\n"
                    outstring+=self.indentGold(counter_o)
                    outstring+="Scanner "
                    outstring+=tstrIn
                    outstring+="=new Scanner("
                    outstring+=tempstring
                    outstring+=");\n"
                    outstring+=self.indentGold(counter_o)
                    outstring+="FileWriter "
                    outstring+=tstrOut
                    outstring+="=new FileWriter("
                    outstring+=tstrt
                    outstring+=")"
                elif tstr=="INSTREAM_TOKEN_GOLD":
                    outstring+=tstrt
                    outstring+="="
                    outstring+=tstrIn
                    outstring+=".nextLine()"
                elif tstr=="OUTSTREAM_TOKEN_GOLD":
                    outstring+=tstrOut
                    outstring+=".write("
                    outstring+=tstrt
                    outstring+=")"
                elif tstr=="CLOSE_TOKEN_GOLD":
                    outstring+=tstrIn
                    outstring+=".close();\n"
                    outstring+=self.indentGold(counter_o)
                    outstring+=tstrOut
                    outstring+=".close()"
                else:
                    outfile.close()
                    return 1
            elif tempstring=="BOOL_TOKEN_GOLD":
                counter+=1
                tempstring=lists[counter]
                outstring+="boolean "
                outstring+=tempstring
            elif tempstring=="INT_TOKEN_GOLD":
                counter+=1
                tempstring=lists[counter]
                outstring+="int "
                outstring+=tempstring
            elif tempstring=="STRING_TOKEN_GOLD":
                counter+=1
                tempstring=lists[counter]
                outstring+="String "
                outstring+=tempstring
            elif tempstring=="ASSIGNMENT_TOKEN_GOLD":
                outstring+="="
            elif tempstring=="WHILE_TOKEN_GOLD":
                counter+=1
                tempstring=lists[counter]
                outstring+="while("
                outstring+=tempstring
                outstring+=")"
                blocks+=["while"]
            elif tempstring=="TRY_TOKEN_GOLD":
                outstring+="try"
                blocks+=["try"]
            elif tempstring=="EXCEPT_TOKEN_GOLD":
                counter+=1
                tempstring=lists[counter]
                outstring=outstring[:-2]
                outstring+="}catch(Exception "
                outstring+=tempstring
                outstring+=")"
            elif tempstring=="ADDASI_TOKEN_GOLD":
                counter+=1
                tempstring=lists[counter]
                tlist=tempstring.split("\_")
                tempstring=" ".join(tlist)
                tlist=tempstring.split("\~")
                tempstring="".join(tlist)
                outstring+="+="
                outstring+=tempstring
            elif tempstring=="CONSTRUCTOR_TOKEN_GOLD":
                counter+=1
                tempstring=lists[counter]
                if tempstring=="NONE_TOKEN_GOLD":
                    tempstring=""
                else:
                    tlist=tempstring.split("str")
                    tempstring="String".join(tlist)
                    tlist=tempstring.split("bool")
                    tempstring="boolean".join(tlist)
                    tlist=tempstring.split("\_")
                    tempstring=" ".join(tlist)
                    tlist=tempstring.split("\~")
                    tempstring="".join(tlist)
                outstring+="public "
                outstring+=cname
                outstring+="("
                outstring+=tempstring
                outstring+=")"
                ends+=["constructor"]
            elif tempstring=="MEMBER_TOKEN_GOLD":
                outstring+="private static "
            elif tempstring=="CREATE_TOKEN_GOLD":
                counter+=1
                tempstring=lists[counter]
                counter+=1
                tstr=lists[counter]
                counter+=1
                tstrt=lists[counter]
                if tstrt=="NONE_TOKEN_GOLD":
                    tstrt=""
                else:
                    tlist=tstrt.split("\_")
                    tstrt=" ".join(tlist)
                    tlist=tstrt.split("\~")
                    tstrt="".join(tlist)
                outstring+=tempstring
                outstring+="=new "
                outstring+=tstr
                outstring+="("
                outstring+=tstrt
                outstring+=")"
            elif tempstring=="IMPORT_TOKEN_GOLD":
                counter+=1
                tempstring=lists[counter]
                outstring+="import "
                outstring+=tempstring
            elif tempstring=="INCREMENT_TOKEN_GOLD":
                outstring+="+=1"
            elif tempstring=="DECREMENT_TOKEN_GOLD":
                outstring+="-=1"
            elif tempstring=="TRUE_TOKEN_GOLD":
                outstring+="true"
            elif tempstring=="FALSE_TOKEN_GOLD":
                outstring+="false"
            elif tempstring=="BEGINCOMMENT_TOKEN_GOLD":
                while 1==1:
                    counter+=1
                    tempstring=lists[counter]
                    if tempstring=="ENDCOMMENT_TOKEN_GOLD":
                        break
            elif tempstring=="PROGRAM_TOKEN_GOLD":
                outstring+="public class "
                outstring+=cname
                outstring+="{\n"
                counter_o+=1
                outstring+=self.indentGold(counter_o)
                outstring+="public void main(String[] args)"
                blocks+=["program"]
            elif tempstring=="SPACE_TOKEN_GOLD":
                outstring+=" "
            elif tempstring=="CONTAINS_TOKEN_GOLD":
                counter_o-=1
                blocks+=["contains"]
            elif tempstring=="POINTER_TOKEN_GOLD":
                pass
            elif tempstring=="GETATTRIBUTE_TOKEN_GOLD":
                outstring+="this."
            elif tempstring=="POINTERATTRIBUTE_TOKEN_GOLD":
                outstring+="."
            elif tempstring=="SUBTRACTIONASSIGNMENT_TOKEN_GOLD":
                outstring+="-="
            elif tempstring=="STACK_TO_HEAP_TOKEN_GOLD_COMPILER":
                pass
            elif tempstring=="SUBTRACTION_TOKEN_GOLD":
                outstring+="-"
            else:
                tlist=tempstring.split("\_")
                tempstring=" ".join(tlist)
                tlist=tempstring.split("\~")
                tempstring="".join(tlist)
                outstring+=tempstring
            counter+=1
        outfile.write(outstring)
        outfile.close()
        return 0
    def run(self,file,lang):
        infile=file+".gold_com"
        self.tokenizeGold(infile)
        if lang=="java":
            outfile=file+".java"
            error=self.compileJava(outfile)
        elif lang=="fortran":
            outfile=file+".f90"
            error=self.compileFort(outfile)
        elif lang=="c_plus_plus":
            outfile=file+".cpp"
            error=self.compileCpp(outfile)
        elif lang=="c_plus_plus_header":
            outfile=file+".h"
            error=self.compileCpp(outfile)
        if error==0:
            print("compiled properly")
        elif error==1:
            print("stream error")
        elif error==2:
            print("stack type error")
        elif error==3:
            print("heap error")
if __name__=="__main__":
    comp=compilerGold()
    a=input()
    b=input()
    comp.run(a,b)
