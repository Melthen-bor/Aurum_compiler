import os
class compilerGold():
    def __init__(self,kernel,linux):
        self.count=0
        self.strlist=[]
        self.templist=[]
        self.consts={}
        self.stack={}
        self.heap={}
        self.varlist={}
        self.func={}
        self.types={}
        self.scopes={}
        self.counter_o=0
        self.auto_point=True
        self.show=False
        self.impl={}
        self.flags=[False,False,False,kernel,linux]
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
        self.flags=[False,False,False,False]
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
                    if not self.flags[0]:
                        self.flags[0]=True
                case "sysin":
                    self.strlist+=["SYSTEMIN_TOKEN_GOLD"]
                    if not self.flags[0]:
                        self.flags[0]=True
                #case "file":
                #    self.strlist+=["FILESTREAM_TOKEN_GOLD"]
                case "=":
                    self.strlist+=["ASSIGNMENT_TOKEN_GOLD"]
                case "inputhandler":
                    self.strlist+=["SYSTEMIN_TOKEN_GOLD"]
                    if not self.flags[0]:
                        self.flags[0]=True
                case "class":
                    self.strlist+=["CLASS_TOKEN_GOLD"]
                case "function":
                    self.strlist+=["FUNCTION_TOKEN_GOLD"]
                #case "use":
                #    self.strlist+=["USE_TOKEN_GOLD"]
                case "return":
                    self.strlist+=["RETURN_TOKEN_GOLD"]
                case "elf":
                    self.strlist+=["ELIF_TOKEN_GOLD"]
                case "bool":
                    self.strlist+=["BOOL_TOKEN_GOLD"]
                case "s64":
                    self.strlist+=["INT_TOKEN_GOLD"]
                #case "close":
                #    self.strlist+=["CLOSE_TOKEN_GOLD"]
                #case "try":
                #    self.strlist+=["TRY_TOKEN_GOLD"]
                #case "except":
                #    self.strlist+=["EXCEPT_TOKEN_GOLD"]
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
                    if not self.flags[2]:
                        self.flags[2]=True
                case "[!":
                    self.strlist+=["BEGINCOMMENT_TOKEN_GOLD"]
                case "!]":
                    self.strlist+=["ENDCOMMENT_TOKEN_GOLD"]
                case "program":
                    self.strlist+=["PROGRAM_TOKEN_GOLD"]
                case "%_":
                    self.strlist+=["SPACE_TOKEN_GOLD"]
                case "%~":
                    self.strlist+=["NONE_TOKEN_GOLD"]
                case "contains":
                    self.strlist+=["CONTAINS_TOKEN_GOLD"]
                case "&*":
                    self.strlist+=["POINTER_TOKEN_GOLD"]
                case "&>":
                    self.strlist+=["GETATTRIBUTE_TOKEN_GOLD"]
                case "->":
                    self.strlist+=["POINTERATTRIBUTE_TOKEN_GOLD"]
                case "-=":
                    self.strlist+=["SUBTRACTIONASSIGNMENT_TOKEN_GOLD"]
                #case "@STACK_TO_HEAP":
                #    self.strlist+=["STACK_TO_HEAP_TOKEN_GOLD_COMPILER"]
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
                #case "@HEAP_TO_STACK":
                #    self.strlist+=["HEAP_TO_STACK_TOKEN_GOLD_COMPILER"]
                case "decons":
                    self.strlist+=["DECONSTRUCTOR_TOKEN_GOLD"]
                case "&!":
                    self.strlist+=["NOT_TOKEN_GOLD"]
                #case "access":
                #    self.strlist+=["ACCESS_TOKEN_GOLD"]
                case "{":
                    self.strlist+=["STARTEXPRESSION_TOKEN_GOLD"]
                case "}":
                    self.strlist+=["ENDEXPRESSION_TOKEN_GOLD"]
                case "is":
                    self.strlist+=["EQUALS_TOKEN_GOLD"]
                #case "@CHECK_HEAP":
                #    self.strlist+=["CHECK_HEAP_TOKEN_GOLD_COMPILER"]
                case "@DO_NOT_DISCARD":
                    self.strlist+=["DO_NOT_DISCARD_TOKEN_GOLD_COMPILER"]
                case "named_class":
                    self.strlist+=["NAMEDCLASS_TOKEN_GOLD"]
                case "procedure":
                    self.strlist+=["PROCEDURE_TOKEN_GOLD"]
                case "u64":
                    self.strlist+=["NATURAL_TOKEN_GOLD"]
                case "impl":
                    self.strlist+=["IMPL_TOKEN_GOLD"]
                case "typedef":
                    self.strlist+=["TYPEDEF_TOKEN_GOLD"]
                case ",":
                    self.strlist+=["SEPERATER_TOKEN_GOLD"]
                case "(":
                    self.strlist+=["POINTEROFFSETSTART_TOKEN_GOLD"]
                case ")":
                    self.strlist+=["POINTEROFFSETEND_TOKEN_GOLD"]
                case "@POINTER_FUNCTION":
                    self.strlist+=["POINTER_FUNCTION_TOKEN_GOLD_COMPILER"]
                case "let":
                    self.strlist+=["CONSTANT_TOKEN_GOLD"]
                case "\"":
                    self.strlist+=["STRINGMARK_TOKEN_GOLD"]
                case "@ARRAY_POINTER":
                    self.strlist+=["ARRAY_POINTER_FUNCTION_TOKEN_GOLD_COMPILER"]
                case "@RETURN_POINTER":
                    self.strlist+=["RETURN_POINTER_MARKER_TOKEN_GOLD_COMPILER"]
                case "load":
                    self.strlist+=["IMPORTLIB_TOKEN_GOLD"]
                case "$STACK":
                    self.strlist+=["STACK_MOD_TOKEN_GOLD_COMPILER"]
                case "$HEAP":
                    self.strlist+=["HEAP_MOD_TOKEN_GOLD_COMPILER"]
                case "@MOVE":
                    self.strlist+=["MOVE_TOKEN_GOLD_COMPILER"]
                case "$DIRECT":
                    self.strlist+=["DIRECT_MOD_TOKEN_GOLD_COMPILER"]
                case "@MANUAL":
                    self.strlist+=["DISABLE_AUTO_POINTER_TOKEN_GOLD_COMPILER"]
                case "@AUTO":
                    self.strlist+=["ENABLE_AUTO_POINTER_TOKEN_GOLD_COMPILER"]
                case "input":
                    self.strlist+=["INFILESTREAM_TOKEN_GOLD"]
                    if not self.flags[1]:
                        self.flags[1]=True
                case "output":
                    self.strlist+=["OUTFILESTREAM_TOKEN_GOLD"]
                    if not self.flags[1]:
                        self.flags[1]=True
                case "char":
                    self.strlist+=["CHARACTER_TOKEN_GOLD"]
                case "'":
                    self.strlist+=["CHARACTERMARK_TOKEN_GOLD"]
                case "@START_SCOPE":
                    self.strlist+=["START_SCOPE_TOKEN_GOLD_COMPILER"]
                case "@END_SCOPE":
                    self.strlist+=["END_SCOPE_TOKEN_GOLD_COMPILER"]
                #case "@CHECK_STACK":
                #    self.strlist+=["CHECK_STACK_TOKEN_GOLD_COMPILER"]
                case "@CHECK":
                    self.strlist+=["CHECK_TOKEN_GOLD_COMPILER"]
                case "$VARS":
                    self.strlist+=["VARS_MOD_TOKEN_GOLD_COMPILER"]
                case "$TYPES":
                    self.strlist+=["TYPES_MOD_TOKEN_GOLD_COMPILER"]
                case "$FUNCS":
                    self.strlist+=["FUNC_MOD_TOKEN_GOLD_COMPILER"]
                case "$CONSTS":
                    self.strlist+=["CONSTANT_MOD_TOKEN_GOLD_COMPILER"]
                case "byte":
                    self.strlist+=["BYTE_TOKEN_GOLD"]
                case "unless":
                    self.strlist+=["UNLESS_TOKEN_GOLD"]
                case "until":
                    self.strlist+=["UNTIL_TOKEN_GOLD"]
                case "letter":
                    self.strlist+=["LETTER_TOKEN_GOLD"]
                case "syserr":
                    self.strlist+=["SYSTEMERR_TOKEN_GOLD"]
                    if not self.flags[0]:
                        self.flags[0]=True
                case "syslog":
                    self.strlist+=["SYSTEMLOG_TOKEN_GOLD"]
                    if not self.flags[0]:
                        self.flags[0]=True
                case "errorHandler":
                    self.strlist+=["SYSTEMERR_TOKEN_GOLD"]
                    if not self.flags[0]:
                        self.flags[0]=True
                case "logger":
                    self.strlist+=["SYSTEMLOG_TOKEN_GOLD"]
                    if not self.flags[0]:
                        self.flags[0]=True
                case "unsigned":
                    if self.flags[4] and self.flags[3]:
                        self.strlist+=["UNSIGNED_TOKEN_GOLD"]
                    else:
                        self.strlist+=["unsigned"]
                case "signed":
                    if self.flags[4] and self.flags[3]:
                        self.strlist+=["SIGNED_TOKEN_GOLD"]
                    else:
                        self.strlist+=["signed"]
                case "long":
                    if self.flags[4] and self.flags[3]:
                        self.strlist+=["LONG_TOKEN_GOLD"]
                    else:
                        self.strlist+=["long"]
                case "int":
                    if self.flags[4] and self.flags[3]:
                        self.strlist+=["KERNEL_INT_TOKEN_GOLD"]
                    else:
                        self.strlist+=["INT_TOKEN_GOLD"]
                case "short":
                    if self.flags[4] and self.flags[3]:
                        self.strlist+=["SHORT_TOKEN_GOLD"]
                    else:
                        self.strlist+=["short"]
                case "break":
                    self.strlist+=["BREAK_TOKEN_GOLD"]
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
    def find_vars(self,varis,var):
        a=0
        while 1==1:
            try:
                b=varis[a]
                if b==var:
                    return a
                a+=1
            except:
                break
        return "death"
    def compileCpp(self,file,st,kernal):
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
        func=[]
        func_type=[]
        no_discard=False
        after_assign=False
        within_class=""
        before_stream=""
        if kernal:
            outstring="typedef long long Int;\ntypedef unsigned long long nat;\n"
        else:
            outstring="#include <iostream>\n#include <fstream>\n#include <string>\nusing namespace std;\ntypedef long long Int;\ntypedef unsigned long long nat;\n"
        while counter<count:
            if st:
                print(counter)
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
                    outstring+="return 0;\n"
                    counter_o-=1
                    outstring+=self.indentGold(counter_o)
                    outstring+="}\n"
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
                    ls=list(outstring)
                    ls.pop()
                    ls.pop()
                    outstring="".join(ls)
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
                    ls=list(outstring)
                    ls.pop()
                    ls.pop()
                    outstring="".join(ls)
                    outstring+="}\n"
                    counter_o-=1
                    outstring+=self.indentGold(counter_o)
                elif tempstring=="function":
                    tl=list(outstring)
                    tl.pop()
                    tl.pop()
                    outstring="".join(tl)
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
                elif tempstring=="procedure":
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
                    tl=list(outstring)
                    tl.pop()
                    tl.pop()
                    outstring="".join(tl)
                    counter_o-=1
                    outstring+="}\n"
                    outstring+=self.indentGold(counter_o)
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
                if before_stream=="GOLD_DEFAULT_OUTSTREAM":
                    counter_temp=counter+1
                    tempstring=lists[counter_temp]
                    if tempstring=="SYSTEMOUT_TOKEN_GOLD":
                        counter_temp+=1
                        tempstring=lists[couter_temp]
                        if not (tempstring=="OUTSTREAM_TOKEN_GOLD"):
                            outstring+=";\n"
                            outstring+=self.indentGold(counter_o)
                            before_stream=""
                    else:
                        outstring+=";\n"
                        outstring+=self.indentGold(counter_o)
                        before_stream=""
                else:
                    outstring+=";\n"
                    outstring+=self.indentGold(counter_o)
            elif tempstring=="PROGRAM_TOKEN_GOLD":
                outstring+="int main()"
                blocks+=["program"]
            elif tempstring=="IF_TOKEN_GOLD":
                outstring+="if("
                counter+=1
                tempstring=lists[counter]
                if tempstring=="STARTEXPRESSION_TOKEN_GOLD":
                    while True:
                        counter+=1
                        tempstring=lists[counter]
                        if tempstring=="ENDEXPRESSION_TOKEN_GOLD":
                            outstring+=")"
                            break
                        elif tempstring=="POINTERATTRIBUTE_TOKEN_GOLD":
                            outstring+="->"
                        elif tempstring=="POINTER_TOKEN_GOLD":
                            outstring+="*"
                        elif tempstring=="GETATTRIBUTE_TOKEN_GOLD":
                            outstring+="this->"
                        elif tempstring=="NOT_TOKEN_GOLD":
                            outstring+="!"
                        elif tempstring=="NONE_TOKEN_GOLD":
                            pass
                        elif tempstring=="SPACE_TOKEN_GOLD":
                            outstring+=" "
                        elif tempstring=="EQUALS_TOKEN_GOLD":
                            outstring+="=="
                        else:
                            outstring+=tempstring
                elif tempstring=="STARTBLOCK_TOKEN_GOLD":
                    outstring+="true){\n"
                    counter_o+=1
                    outstring+=self.indentGold(counter_o)
                else:
                    tlist=tempstring.split("&>")
                    tempstring="this->".join(tlist)
                    tlist=tempstring.split("&!")
                    tempstring="!".join(tlist)
                    tlist=tempstring.split("&*")
                    tempstring="*".join(tlist)
                    outstring+=tempstring
                    outstring+=")"
                blocks+=["if"]
            elif tempstring=="SYSTEMOUT_TOKEN_GOLD":
                if kernal:
                    return 5
                counter+=1
                tempstring=lists[counter]
                if tempstring=="OUTSTREAM_TOKEN_GOLD":
                    if before_stream=="GOLD_DEFAULT_OUTSTREAM":
                        counter+=1
                        tempstring=lists[counter]
                        tlist=tempstring.split("%_")
                        tempstring=" ".join(tlist)
                        tlist=tempstring.split("%~")
                        tempstring="".join(tlist)
                        outstring+=" << "
                        outstring+=tempstring
                    else:
                        counter+=1
                        tempstring=lists[counter]
                        tlist=tempstring.split("%_")
                        tempstring=" ".join(tlist)
                        tlist=tempstring.split("%~")
                        tempstring="".join(tlist)
                        outstring+="cout << "
                        outstring+=tempstring
                        before_stream="GOLD_DEFAULT_OUTSTREAM"
                else:
                    return 1
            elif tempstring=="SYSTEMIN_TOKEN_GOLD":
                if kernal:
                    return 5
                counter+=1
                tempstring=lists[counter]
                if tempstring=="INSTREAM_TOKEN_GOLD":
                    counter+=1
                    tempstring=lists[counter]
                    outstring+="cin >> "
                    outstring+=tempstring
                else:
                    return 1
            elif tempstring=="CLASS_TOKEN_GOLD":
                outstring+="class "
                outstring+=cname
                within_class=cname
                blocks+=["class"]
            elif tempstring=="FUNCTION_TOKEN_GOLD":
                counter+=1
                tempstring=lists[counter]
                if tempstring=="BOOL_TOKEN_GOLD":
                    tempstring="bool"
                elif tempstring=="NONE_TOKEN_GOLD":
                    tempstring="void"
                elif tempstring=="INT_TOKEN_GOLD":
                    tempstring="Int"
                elif tempstring=="STRING_TOKEN_GOLD":
                    if kernal:
                        return 5
                    tempstring=="string"
                elif tempstring=="NATURAL_TOKEN_GOLD":
                    tempstring=="nat"
                else:
                    tlist=tempstring.split("str")
                    tempstring="string".join(tlist)
                    tlist=tempstring.split("&*")
                    tempstring="*".join(tlist)
                outstring+=tempstring
                counter+=1
                tempstring=lists[counter]
                if tempstring=="POINTER_TOKEN_GOLD":
                    outstring+="*"
                    counter+=1
                    tempstring=lists[counter]
                outstring+=" "
                func+=[tempstring]
                if no_discard:
                    func_type+=["noDiscard"]
                else:
                    func_type+=["normal"]
                no_discard=False
                outstring+=tempstring
                outstring+="("
                counter+=1
                tempstring=lists[counter]
                if tempstring=="STARTEXPRESSION_TOKEN_GOLD":
                    while True:
                        counter+=1
                        tempstring=lists[counter]
                        if tempstring=="ENDEXPRESSION_TOKEN_GOLD":
                            outstring+=")"
                            break
                        elif tempstring=="NONE_TOKEN_GOLD":
                            pass
                        elif tempstring=="SPACE_TOKEN_GOLD":
                            outstring+=" "
                        elif tempstring=="INT_TOKEN_GOLD":
                            outstring+="Int"
                            counter_temp=counter+1
                            tempstring=lists[counter_temp]
                            if not (tempstring=="POINTER_TOKEN_GOLD"):
                                outstring+=" "
                        elif tempstring=="STRING_TOKEN_GOLD":
                            if kernal:
                                return 5
                            outstring+="string"
                            counter_temp=counter+1
                            tempstring=lists[counter_temp]
                            if not (tempstring=="POINTER_TOKEN_GOLD"):
                                outstring+=" "
                        elif tempstring=="BOOL_TOKEN_GOLD":
                            outstring+="bool"
                            counter_temp=counter+1
                            tempstring=lists[counter_temp]
                            if not (tempstring=="POINTER_TOKEN_GOLD"):
                                outstring+=" "
                        elif tempstring=="NATURAL_TOKEN_GOLD":
                            outstring+="nat"
                            counter_temp=counter+1
                            tempstring=lists[counter_temp]
                            if not (tempstring=="POINTER_TOKEN_GOLD"):
                                outstring+=" "
                        elif tempstring=="POINTER_TOKEN_GOLD":
                            outstring+="* "
                        elif tempstring=="SEPERATER_TOKEN_GOLD":
                            outstring+=", "
                        else:
                            outstring+=tempstring
                elif tempstring=="STARTBLOCK_TOKEN_GOLD":
                    outstring+="){\n"
                    counter_o+=1
                    outstring+=self.indentGold(counter_o)
                else:
                    if tempstring=="NONE_TOKEN_GOLD":
                        tempstring=""
                    else:
                        tlist=tempstring.split("%_")
                        tempstring=" ".join(tlist)
                        tlist=tempstring.split("%~")
                        tempstring="".join(tlist)
                    outstring+=tempstring
                    outstring+=")"
                blocks+=["function"]
            elif tempstring=="PROCEDURE_TOKEN_GOLD":
                outstring+="void "
                counter+=1
                tempstring=lists[counter]
                func+=[tempstring]
                func_type+=["normal"]
                no_discard=False
                outstring+=tempstring
                outstring+="("
                counter+=1
                tempstring=lists[counter]
                if tempstring=="STARTEXPRESSION_TOKEN_GOLD":
                    while True:
                        counter+=1
                        tempstring=lists[counter]
                        if tempstring=="ENDEXPRESSION_TOKEN_GOLD":
                            outstring+=")"
                            break
                        elif tempstring=="NONE_TOKEN_GOLD":
                            pass
                        elif tempstring=="SPACE_TOKEN_GOLD":
                            outstring+=" "
                        elif tempstring=="INT_TOKEN_GOLD":
                            outstring+="Int"
                            temp_counter=counter+1
                            tempstring=lists[temp_counter]
                            if not (tempstring=="POINTER_TOKEN_GOLD"):
                                outstring+=" "
                        elif tempstring=="STRING_TOKEN_GOLD":
                            if kernal:
                                return 5
                            outstring+="string"
                            temp_counter=counter+1
                            tempstring=lists[temp_counter]
                            if not (tempstring=="POINTER_TOKEN_GOLD"):
                                outstring+=" "
                        elif tempstring=="BOOL_TOKEN_GOLD":
                            outstring+="bool"
                            temp_counter=counter+1
                            tempstring=lists[temp_counter]
                            if not (tempstring=="POINTER_TOKEN_GOLD"):
                                outstring+=" "
                        elif tempstring=="NATURAL_TOKEN_GOLD":
                            outstring+="nat"
                            temp_counter=counter+1
                            tempstring=lists[temp_counter]
                            if not (tempstring=="POINTER_TOKEN_GOLD"):
                                outstring+=" "
                        elif tempstring=="POINTER_TOKEN_GOLD":
                            outstring+="* "
                        elif tempstring=="SEPERATER_TOKEN_GOLD":
                            outstring+=", "
                        else:
                            outstring+=tempstring
                elif tempstring=="STARTBLOCK_TOKEN_GOLD":
                    outstring+="){\n"
                    counter_o+=1
                    outstring+=self.indentGold(counter_o)
                else:
                    if tempstring=="NONE_TOKEN_GOLD":
                        tempstring=""
                    else:
                        tlist=tempstring.split("%_")
                        tempstring=" ".join(tlist)
                        tlist=tempstring.split("%~")
                        tempstring="".join(tlist)
                    outsting+=tempstring
                    outstring+=")"
                blocks+=["procedure"]
            elif tempstring=="ELIF_TOKEN_GOLD":
                tl=list(outstring)
                tl.pop()
                tl.pop()
                outstring="".join(tl)
                outstring+="} else if("
                counter+=1
                tempstring=lists[counter]
                if tempstring=="STARTEXPRESSION_TOKEN_GOLD":
                    while True:
                        counter+=1
                        tempstring=lists[counter]
                        if tempstring=="ENDEXPRESSION_TOKEN_GOLD":
                            outstring+=")"
                            break
                        elif tempstring=="POINTERATTRIBUTE_TOKEN_GOLD":
                            outstring+="->"
                        elif tempstring=="POINTER_TOKEN_GOLD":
                            outstring+="*"
                        elif tempstring=="GETATTRIBUTE_TOKEN_GOLD":
                            outstring+="this->"
                        elif tempstring=="NOT_TOKEN_GOLD":
                            outstring+="!"
                        elif tempstring=="NONE_TOKEN_GOLD":
                            pass
                        elif tempstring=="SPACE_TOKEN_GOLD":
                            outstring+=" "
                        elif tempstring=="EQUALS_TOKEN_GOLD":
                            outstring+="=="
                        else:
                            outstring+=tempstring
                else:
                    tlist=tempstring.split("&>")
                    tempstring="this->".join(tlist)
                    tlist=tempstring.split("&!")
                    tempstring="!".join(tlist)
                    tlist=tempstring.split("&*")
                    tempstring="*".join(tlist)
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
                if tempstring=="STARTEXPRESSION_TOKEN_GOLD":
                    outstring+="("
                    counter+=1
                    tempstring=lists[counter]
                if tempstring=="GETATTRIBUTE_TOKEN_GOLD":
                    outstring+="this->"
                    counter+=1
                    tempstring=lists[counter]
                tl=tempstring.split("{")
                tempstring="(".join(tl)
                tl=tempstring.split("}")
                tempstring=")".join(tl)
                tl=tempstring.split("&*")
                tempstring="*".join(tl)
                tl=tempstring.split("->")
                tempstring="->".join(tl)
                tl=tempstring.split("%_")
                tempstring=" ".join(tl)
                tl=tempstring.split("%~")
                tempstring="".join(tl)
                outstring+=tempstring
                counter+=1
                tempstring=lists[counter]
                if tempstring=="ACCESS_TOKEN_GOLD":
                    outstring+="["
                    counter+=1
                    tempstring=lists[counter]
                    if tempstring=="POINTER_TOKEN_GOLD":
                        outstring+="*"
                        counter+=1
                        tempstring=lists[counter]
                    elif tempstring=="GETATTRIBUTE_TOKEN_GOLD":
                        outstring+="this->"
                        counter+=1
                        tempstring=lists[counter]
                    outstring+=tempstring
                    outstring+="]"
                if tempstring=="ENDEXPRESSION_TOKEN_GOLD":
                    outstring+=")."
                    counter+=1
                    tempstring=lists[counter]
                    outstring+=tempstring
                counter+=1
                tempstring=lists[counter]
                tempint=self.find_vars(func,tempstring)
                if tempint=="death":
                    return 4
                else:
                    tempstr=func_type[tempint]
                    if not tempstr == "normal":
                        if tempstr=="noDiscard":
                            if not after_assign:
                                return 4
                            else:
                                after_assign=False
                outstring+="("
                if tempstring=="POINTER_TOKEN_GOLD":
                    outstring+="*"
                    counter+=1
                    tempstring=lists[counter]
                if tempstring=="ENDSTATEMENT_TOKEN_GOLD":
                    outstring+=");\n"
                    outstring+=self.indentGold(counter_o)
                elif tempstring=="STARTEXPRESSION_TOKEN_GOLD":
                    while True:
                        counter+=1
                        tempstring=lists[counter]
                        if tempstring=="ENDEXPRESSION_TOKEN_GOLD":
                            outstring+=")"
                            break
                        elif tempstring=="POINTERATTRIBUTE_TOKEN_GOLD":
                            outstring+="->"
                        elif tempstring=="GETATTRIBUTE_TOKEN_GOLD":
                            outstring+="this->"
                        elif tempstring=="POINTER_TOKEN_GOLD":
                            outstring+="*"
                        elif tempstring=="ACCESS_TOKEN_GOLD":
                            outstring+="["
                            counter+=1
                            tempstring=lists[counter]
                            outstring+=tempstring
                            outstring+="]"
                        elif tempstring=="SEPERATER_TOKEN_GOLD":
                            outstring+=", "
                        else:
                            outstring+=tempstring
                else:
                    if tempstring=="NONE_TOKEN_GOLD":
                        tempstring=""
                    else:
                        tl=tempstring.split("&>")
                        tempstring="this->".join(tl)
                        tl=tempstring.split("->")
                        tempstring="->".join(tl)
                        tl=tempstring.split("&*")
                        tempstring="*".join(tl)
                        tl=tempstring.split("%_")
                        tempstring=" ".join(tl)
                        tl=tempstring.split("%~")
                        tempstring="".join(tl)
                    outstring+=tempstring
                    outstring+=")"
            elif tempstring=="STRING_TOKEN_GOLD":
                if kernal:
                    return 5
                outstring+="string "
            elif tempstring=="INCREMENT_TOKEN_GOLD":
                outstring+="++"
            elif tempstring=="DECREMENT_TOKEN_GOLD":
                outstring+="--"
            elif tempstring=="ADDASI_TOKEN_GOLD":
                outstring+="+="
            elif tempstring=="ASSIGNMENT_TOKEN_GOLD":
                outstring+="="
                after_assign=True
            elif tempstring=="FALSE_TOKEN_GOLD":
                outstring+="false"
            elif tempstring=="TRUE_TOKEN_GOLD":
                outstring+="true"
            elif tempstring=="TRY_TOKEN_GOLD":
                if kernal:
                    return 5
                outstring+="try"
                blocks+=["try"]
            elif tempstring=="EXCEPT_TOKEN_GOLD":
                if kernal:
                    return 5
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
                            outstring+=self.indentGold(counter_o)
                        elif tempstring=="array":
                            outstring+="delete[] "
                            outstring+=stack.pop()
                            outstring+=";\n"
                            outstring+=self.indentGold(counter_o)
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
                if kernal:
                    return 5
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
                outstring+="Int "
            elif tempstring=="CONTAINS_TOKEN_GOLD":
                ls=list(outstring)
                ls.pop()
                ls.pop()
                outstring="".join(ls)
                outstring+="public:\n"
                outstring+=self.indentGold(counter_o)
                blocks+=["contains"]
                counter+=1
            elif tempstring=="MEMBER_TOKEN_GOLD":
                pass
            elif tempstring=="CONSTRUCTOR_TOKEN_GOLD":
                outstring+=within_class
                outstring+="("
                counter+=1
                tempstring=lists[counter]
                if tempstring=="STARTEXPRESSION_TOKEN_GOLD":
                    while True:
                        counter+=1
                        tempstring=lists[counter]
                        if tempstring=="ENDEXPRESSION_TOKEN_GOLD":
                            outstring+=")"
                            break
                        elif tempstring=="NONE_TOKEN_GOLD":
                            pass
                        elif tempstring=="SPACE_TOKEN_GOLD":
                            outstring+=" "
                        elif tempstring=="STRING_TOKEN_GOLD":
                            if kernal:
                                return 5
                            outstring+="string"
                            counter_temp=counter+1
                            tempstring=lists[counter_temp]
                            if not (tempstring=="POINTER_TOKEN_GOLD"):
                                outstring+=" "
                        elif tempstring=="INT_TOKEN_GOLD":
                            outstring+="Int"
                            counter_temp=counter+1
                            tempstring=lists[counter_temp]
                            if not (tempstring=="POINTER_TOKEN_GOLD"):
                                outstring+=" "
                        elif tempstring=="BOOL_TOKEN_GOLD":
                            outstring+="bool"
                            counter_temp=counter+1
                            tempstring=lists[counter_temp]
                            if not (tempstring=="POINTER_TOKEN_GOLD"):
                                outstring+=" "
                        elif tempstring=="NATURAL_TOKEN_GOLD":
                            outstring+="nat"
                            counter_temp=counter+1
                            tempstring=lists[counter_temp]
                            if not (tempstring=="POINTER_TOKEN_GOLD"):
                                outstring+=" "
                        elif tempstring=="POINTER_TOKEN_GOLD":
                            outstring+="* "
                        elif tempstring=="SEPERATER_TOKEN_GOLD":
                            outstring+=", "
                        else:
                            outstring+=tempstring
                elif tempstring=="STARTBLOCK_TOKEN_GOLD":
                    outstring+="){\n"
                    outstring+=self.indentGold(counter_o)
                else:
                    if tempstring=="NONE_TOKEN_GOLD":
                        tempstring=""
                    else:
                        tlist=tempstring.split("str")
                        tempstring="string".join(tlist)
                        tlist=tempstring.split("%_")
                        tempstring=" ".join(tlist)
                        tlist=tempstring.split("%~")
                        tempstring="".join(tlist)
                    outstring+=tempstring
                    outstring+=")"
                blocks+=["constructor"]
            elif tempstring=="WHILE_TOKEN_GOLD":
                outstring+="while("
                counter+=1
                tempstring=lists[counter]
                if tempstring=="STARTEXPRESSION_TOKEN_GOLD":
                    while True:
                        counter+=1
                        tempstring=lists[counter]
                        if tempstring=="ENDEXPRESSION_TOKEN_GOLD":
                            outstring+=")"
                            break
                        elif tempstring=="NONE_TOKEN_GOLD":
                            pass
                        elif tempstring=="SPACE_TOKEN_GOLD":
                            outstring+=" "
                        elif tempstring=="NOT_TOKEN_GOLD":
                            outstring+="!"
                        elif tempstring=="POINTERATTRIBUTE_TOKEN_GOLD":
                            outstring+="->"
                        elif tempstring=="GETATTRIBUTE_TOKEN_GOLD":
                            outstring+="this->"
                        elif tempstring=="POINTER_TOKEN_GOLD":
                            outstring+="*"
                        elif tempstring=="EQUALS_TOKEN_GOLD":
                            outstring+="=="
                        else:
                            outstring+=tempstring
                elif tempstring=="STARTBLOCK_TOKEN_GOLD":
                    outstring+="true){\n"
                    counter_o+=1
                    outstring+=self.indentGold(counter_o)
                else:
                    tlist=tempstring.split("&>")
                    tempstring="this->".join(tlist)
                    tlist=tempstring.split("&!")
                    tempstring="!".join(tlist)
                    tlist=tempstring.split("&*")
                    tempstring="*".join(tlist)
                    outstring+=tempstring
                    outstring+=")"
                blocks+=["while"]
            elif tempstring=="CREATE_TOKEN_GOLD":
                if kernal:
                    return 5
                counter+=1
                tempstring=lists[counter]
                if tempstring=="GETATTRIBUTE_TOKEN_GOLD":
                    outstring+="this->"
                    counter+=1
                    tempstring=lists[counter]
                outstring+=tempstring
                stack.append(tempstring)
                stack_type.append("scaler")
                outstring+="=new "
                counter+=1
                tempstring=lists[counter]
                if tempstring=="INT_TOKEN_GOLD":
                    tempstring="Int"
                elif tempstring=="BOOL_TOKEN_GOLD":
                    tempstring="bool"
                elif tempstring=="STRING_TOKEN_GOLD":
                    tempstring="string"
                elif tempstring=="NATURAL_TOKEN_GOLD":
                    tempstring="nat"
                outstring+=tempstring
                outstring+="("
                counter+=1
                tempstring=lists[counter]
                if tempstring=="NONE_TOKEN_GOLD":
                    tempstring=""
                elif tempstring=="TRUE_TOKEN_GOLD":
                    tempstring="true"
                elif tempstring=="FALSE_TOKEN_GOLD":
                    tempstring="false"
                else:
                    tlist=tempstring.split("%_")
                    tempstring=" ".join(tlist)
                    tlist=tempstring.split("%~")
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
                if kernal:
                    return 5
                heap+=[stack.pop()]
                heap_type+=[stack_type.pop()]
            elif tempstring=="SUBTRACTION_TOKEN_GOLD":
                outstring+="-"
            elif tempstring=="CREATEARRAY_TOKEN_GOLD":
                if kernal:
                    return 5
                counter+=1
                tempstring=lists[counter]
                if tempstring=="GETATTRIBUTE_TOKEN_GOLD":
                    outstring+="this->"
                    counter+=1
                    tempstring=lists[counter]
                outstring+=tempstring
                stack.append(tempstring)
                stack_type.append("array")
                outstring+="=new "
                counter+=1
                tempstring=lists[counter]
                if tempstring=="INT_TOKEN_GOLD":
                    tempstring="Int"
                elif tempstring=="STRING_TOKEN_GOLD":
                    tempstring="string"
                elif tempstring=="BOOL_TOKEN_GOLD":
                    tempstring="bool"
                elif tempstring=="NATURAL_TOKEN_GOLD":
                    tempstring="nat"
                outstring+=tempstring
                temp=tempstring
                outstring+="["
                counter+=1
                tempstring=lists[counter]
                if tempstring=="GETATTRIBUTE_TOKEN_GOLD":
                    outstring+="this->"
                    counter+=1
                    tempstring=lists[counter]
                elif tempstring=="POINTER_TOKEN_GOLD":
                    outstring+="*"
                    counter+=1
                    tempstring=lists[counter]
                outstring+=tempstring
                counter+=1
                tempstring=lists[counter]
                if tempstring=="ENDSTATEMENT_TOKEN_GOLD":
                    outstring+="];\n"
                    outstring+=self.indentGold(counter_o)
                else:
                    outstring+="]{"
                    outstring+=temp
                    outstring+="("
                    if tempstring=="NONE_TOKEN_GOLD":
                        tempstring=""
                    else:
                        tl=tempstring.split("%_")
                        tempstring=" ".join(tl)
                        tl=tempstring.split("%~")
                        tempstring="".join(tl)
                    outstring+=tempstring
                    outstring+=")}"
            elif tempstring=="DESTROY_TOKEN_GOLD":
                if kernal:
                    return 5
                counter+=1
                tempstring=lists[counter]
                temp=""
                if tempstring=="GETATTRIBUTE_TOKEN_GOLD":
                    temp+="this->"
                    counter+=1
                    tempstring=lists[counter]
                temp+=tempstring
                temp=self.find_vars(heap,temp)
                if temp=="death":
                    return 3
                tstr=heap_type.pop(temp)
                if tstr=="scaler":
                    outstring+="delete "
                elif tstr=="array":
                    outstring+="delete[] "
                outstring+=heap.pop(temp)
            elif tempstring=="DELETE_TOKEN_GOLD":
                if kernal:
                    return 5
                counter+=1
                tempstring=lists[counter]
                temp=""
                if tempstring=="GETATTRIBUTE_TOKEN_GOLD":
                    temp+="this->"
                    counter+=1
                    tempstring=lists[counter]
                temp+=tempstring
                tstr=self.find_vars(heap,temp)
                if not(temp=="death"):
                    heap.pop(tstr)
                    heap_type.pop(tstr)
                outstring+="delete[] "
                outstring+=temp
            elif tempstring=="DELETEARRAY_TOKEN_GOLD":
                if kernal:
                    return 5
                counter+=1
                tempstring=lists[counter]
                temp=""
                if tempstring=="GETATTRIBUTE_TOKEN_GOLD":
                    temp+="this->"
                    counter+=1
                    tempstring=lists[counter]
                temp+=tempstring
                tstr=self.find_vars(heap,temp)
                if not(temp=="death"):
                    heap.pop(tstr)
                    heap_stack.pop(tstr)
                outstring+="delete "
                outstring+=temp
            elif tempstring=="HEAP_TO_STACK_TOKEN_GOLD_COMPILER":
                if kernal:
                    return 5
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
                outstring+=within_class
                outstring+="()"
                blocks+=["deconstructor"]
            elif tempstring=="NOT_TOKEN_GOLD":
                outstring+="!"
            elif tempstring=="ACCESS_TOKEN_GOLD":
                outstring+="["
                counter+=1
                tempstring=lists[counter]
                if tempstring=="POINTER_TOKEN_GOLD":
                    outstring+="*"
                    counter+=1
                    tempstring=lists[counter]
                elif tempstring=="GETATTRIBUTE_TOKEN_GOLD":
                    outstring+="this->"
                    counter+=1
                    tempstring=lists[counter]
                tl=tempstring.split("{")
                tempstring="(".join(tlist)
                tl=tempstring.split("}")
                tempstring=")".join(tlist)
                tl=tempstring.split("%_")
                tempstring=" ".join(tl)
                tl=tempstring.split("%~")
                tempstring="".join(tl)
                outstring+=tempstring
                outstring+="]"
            elif tempstring=="SPACE_TOKEN_GOLD":
                outstring+=" "
            elif tempstring=="STARTEXPRESSION_TOKEN_GOLD":
                outstring+="("
            elif tempstring=="ENDEXPRESSION_TOKEN_GOLD":
                outstring+=")"
            elif tempstring=="IMPORT_TOKEN_GOLD":
                outstring+="#include \""
                counter+=1
                tempstring=lists[counter]
                outstring+=tempstring
                outstring+="\""
            elif tempstring=="CHECK_HEAP_TOKEN_GOLD_COMPILER":
                if kernal:
                    return 5
                a=len(heap)
                print(a)
                b=0
                while b<a:
                    c=heap[b]
                    c+=":"
                    c+=heap_type[b]
                    b+=1
            elif tempstring=="DO_NOT_DISCARD_TOKEN_GOLD_COMPILER":
                no_discard=True
            elif tempstring=="NAMEDCLASS_TOKEN_GOLD":
                outstring+="class "
                counter+=1
                tempstring=lists[counter]
                if tempstring=="STARTEXPRESSION_TOKEN_GOLD":
                    tstr=""
                    while True:
                        counter+=1
                        tempstring=lists[counter]
                        if tempstring=="ENDEXPRESSION_TOKEN_GOLD":
                            break
                        elif tempstring=="STRING_TOKEN_GOLD":
                            tstr+="str"
                        elif tempstring=="INT_TOKEN_GOLD":
                            tstr+="Int"
                        elif tempstring=="BOOL_TOKEN_GOLD":
                            tstr+="bool"
                        elif tempstring=="NATURAL_TOKEN_GOLD":
                            tstr+="nat"
                        else:
                            tstr+=tempstring
                else:
                    tstr=tempstring
                outstring+=tstr
                within_class=tempstring
                blocks+=["class"]
            elif tempstring=="EQUALS_TOKEN_GOLD":
                outstring+="=="
            elif tempstring=="NATURAL_TOKEN_GOLD":
                outstring+="nat "
            elif tempstring=="OUTSTREAM_TOKEN_GOLD":
                outstring+=" << "
            elif tempstring=="SEPERATER_TOKEN_GOLD":
                outstring+=", "
            elif tempstring=="POINTEROFFSETSTART_TOKEN_GOLD":
                outstring+="["
            elif tempstring=="POINTEROFFSETEND_TOKEN_GOLD":
                outstring+="]"
            else:
                outstring+=tempstring
                after_assign=False
            counter+=1
        outfile=open(file,mode="w+")
        outfile.write(outstring)
        outfile.close()
        return 0
    def compileString(self,outstring,counter):
        outstring+="\""
        while True:
            counter+=1
            tempstring=self.strlist[counter]
            match tempstring:
                case "STRINGMARK_TOKEN_GOLD":
                    outstring+="\""
                    return [outstring,counter]
                case "SPACE_TOKEN_GOLD":
                    outstring+=" "
                case "NONE_TOKEN_GOLD":
                    pass
                case "CHARACTERMARK_TOKEN_GOLD":
                    outstring+="'"
                case _:
                    outstring+=tempstring
    def compileChar(self,outstring,counter):
        outstring+="'"
        while True:
            counter+=1
            tempstring=self.strlist[counter]
            match tempstring:
                case "CHARACTERMARK_TOKEN_GOLD":
                    outstring+="'"
                    return [outstring,counter]
                case "SPACE_TOKEN_GOLD":
                    outstring+=" "
                case "NONE_TOKEN_GOLD":
                    pass
                case "STRINGMARK_TOKEN_GOLD":
                    outstring+="\""
                case _:
                    outstring+=tempstring
    def compileCppEx(self,outstring,counter,block,last_var):
        outstring+="("
        while True:
            counter+=1
            tempstring=self.strlist[counter]
            match tempstring:
                case "STARTEXPRESSION_TOKEN_GOLD":
                    temp=self.compileCppEx(outstring,counter,kernel,block,last_var)
                    if len(temp)==1:
                        return [temp[0]]
                    outstring=temp[0]
                    counter=temp[1]
                    last_var=temp[2]
                case "ENDEXPRESSION_TOKEN_GOLD":
                    outstring+=")"
                    return [outstring,counter,last_var]
                case "POINTERATTRIBUTE_TOKEN_GOLD":
                    if block=="FUNCTION":
                        return [7]
                    outstring+="->"
                case "GETATTRIBUTE_TOKEN_GOLD":
                    if block=="FUNCTION":
                        return [7]
                    outstring+="this->"
                case "EQUALS_TOKEN_GOLD":
                    if block=="FUNCTION":
                        return [7]
                    outstring+="=="
                case "NOT_TOKEN_GOLD":
                    if block=="FUNCTION":
                        return [7]
                    outstring+="!"
                case "NONE_TOKEN_GOLD":
                    pass
                case "SPACE_TOKEN_GOLD":
                    outstring+=" "
                case "INT_TOKEN_GOLD":
                    match block:
                        case "CONTROL":
                            return [6]
                        case "USE":
                            return [4]
                        case "ALLOC":
                            return [12]
                        case _:
                            pass
                    outstring+="Int"
                    if not self.strlist[counter+1]=="POINTER_TOKEN_GOLD":
                        outstring+=" "
                case "BOOL_TOKEN_GOLD":
                    match block:
                        case "CONTROL":
                            return [6]
                        case "USE":
                            return [4]
                        case "ALLOC":
                            return [12]
                        case _:
                            pass
                    outstring+="bool"
                    if not self.strlist[counter+1]=="POINTER_TOKEN_GOLD":
                        outstring+=" "
                case "STRING_TOKEN_GOLD":
                    match block:
                        case "CONTROL":
                            return [6]
                        case "USE":
                            return [4]
                        case "ALLOC":
                            return [12]
                        case _:
                            pass
                    if self.flags[3]:
                        return [5]
                    outstring+="string"
                    if not self.strlist[counter+1]=="POINTER_TOKEN_GOLD":
                        outstring+=" "
                case "NATURAL_TOKEN_GOLD":
                    match block:
                        case "CONTROL":
                            return [6]
                        case "USE":
                            return [4]
                        case "ALLOC":
                            return [12]
                        case _:
                            pass
                    outstring+="nat"
                    if not self.strlist[counter+1]=="POINTER_TOKEN_GOLD":
                        outstring+=" "
                case "SEPERATER_TOKEN_GOLD":
                    if block=="CONTROL":
                        return [6]
                    outstring+=", "
                case "STRINGMARK_TOKEN_GOLD":
                    temp=self.compileString(outstring,counter)
                    outstring=temp[0]
                    counter=temp[1]
                case "DISABLE_AUTO_POINTER_TOKEN_GOLD_COMPILER":
                    self.auto_point=False
                case "ENABLE_AUTO_POINTER_TOKEN_GOLD_COMPILER":
                    self.auto_point=True
                case "CHARACTERMARK_TOKEN_GOLD":
                    temp=self.compileChar(outstring,counter)
                    outstring=temp[0]
                    counter=temp[1]
                case "CHARACTER_TOKEN_GOLD":
                    match block:
                        case "CONTROL":
                            return [6]
                        case "USE":
                            return [4]
                        case "ALLOC":
                            return [12]
                        case _:
                            pass
                    outstring+="char"
                    if not self.strlist[counter+1]=="POINTER_TOKEN_GOLD":
                        outstring+=" "
                case _:
                    temp=self.compileCppNames(outstring,counter,last_var,"",tempstring)
                    if len(temp)==1:
                        return [temp[0]]
                    outstring=temp[0]
                    counter=temp[1]
                    last_var=temp[2]
    def compileCppNames(self,outstring,counter,last_var,on,name):
        if name=="exit":
            if self.auto_point:
                return 16
        index=self.find_vars(list(self.func.keys()),name)
        if not index=="death":
            temp=self.compileCppFunc(outstring,counter,name,on=on,last_var=last_var)
            if len(temp)==1:
                return [temp[0]]
            outstring=temp[0]
            counter=temp[1]
            last_var=temp[2]
        else:
            index=self.find_vars(list(self.varlist.keys()),name)
            if not index=="death":
                temp=self.compileCppVar(outstring,counter,name)
                if len(temp)==1:
                    return [temp[0]]
                outstring=temp[0]
                counter=temp[1]
                last_var=temp[2]
            else:
                index=self.find_vars(list(self.const.keys()),name)
                if not index=="death":
                    outstring+=self.const[name]
                else:
                    index=self.find_vars(list(self.types.keys()),name)
                    if not index=="death":
                        temp=self.compileCppTypes(outstring,counter,name)
                        if len(temp)==1:
                            return [temp[0]]
                        outstring=temp[0]
                        counter=temp[1]
                    else:
                        return 13
        return [outstring,counter,last_var]
    def loadLibFunc(self,funclist,typ=""):
        num=len(funclist)
        counter=0
        while counter<num:
            ls=funclist[counter].split(" ")
            name=ls[0]
            discard=(ls[1]=="no-discard")
            pointer=(ls[2]=="pointer")
            tpe=ls[3]
            ptype="void"
            if pointer:
                ptype=ls[4]
            if typ=="":
                self.func.update({name:[discard,pointer,tpe,ptype]})
            else:
                self.types[typ][0].update({name:[discard,pointer,tpe,ptype]})
            counter+=1
    def loadLibType(self,typelist,direct):
        num=len(typelist)
        counter=0
        while counter<num:
            ls=typelist[counter].split(" ")
            name=ls[0]
            file=open(direct+ls[1]+".func")
            cons=file.read().split("\n")
            file.close()
            self.types.update({name:[{},{}]})
            loadLibFunc(cons,typ=ls[0])
            counter+=1
    def loadLibConst(self,constlist):
        num=len(constlist)
        counter=0
        while count<num:
            ls=constlist[counter].split(" ")
            self.const.update({ls[0]:ls[1]})
            counter+=1
    def compileCppFunc(self,outstring,counter,name,last_var=[""],on=[""]):
        if on=="":
            func=self.func[name]
        else:
            func=self.types[on[2]][name]
        if func[0]:
            if self.show:
                print("func[0] is true")
            if last_var[0]=="":
                if self.show:
                    print("last_var[0] is \"\"")
                return [4]
            if not func[2]==last_var[2]:
                if self.show:
                    print("func[2] is not last_var[2]")
                return [4]
            if func[1]:
                if not last_var[1]:
                    return [10]
                if func[3]=="void":
                    return [4]
                if last_var[3]:
                    return [10]
                self.stack.update(last_var[0],func[3])
                self.varlist[last_var[0]][2]=True
        else:
            if self.show:
                print("func[0] is false")
            if not last_var[0]=="":
                if self.show:
                    print("last_var[0] is \"\"")
                if (not(func[2]==last_var[2]))and(not(func[2]=="")):
                if self.show:
                    print("func[2] is not last_var[2] nor \"\"")
                    return [4]
                if func[1]:
                    if not last_var[1]:
                        return [10]
                    if func[3]=="void":
                        return [4]
                    if last_var[3]:
                        return [1]
                    self.stack.update(last_var[0],func[3])
                    self.varlist[last_var[0]][2]=True
        outstring+=name
        counter+=1
        tempstring=self.strlist[counter]
        match tempstring:
            case "STARTEXPRESSION_TOKEN_GOLD":
                temp=self.compileCppEx(outstring,counter,"USE",last_var)
                if len(temp)==1:
                    return [temp[0]]
                outstring=temp[0]
                counter=temp[1]
                last_var=temp[2]
            case "ENDSTATEMENT_TOKEN_GOLD":
                outstring+="();\n"
                outstring+=self.indentGold(self.counter_o)
            case "NONE_TOKEN_GOLD":
                outstring+="()"
            case _:
                outstring+="("
                temp=self.compileCppNames(outstring,counter,last_var,"",tempstring)
                if len(temp)==1:
                    return [temp[0]]
                outstring=temp[0]
                counter=temp[1]
                last_var=temp[2]
                outstring+=")"
        return [outstring,counter,last_var]
    def compileCppVar(self,outstring,counter,name):
        var=self.varlist[name]
        if var[0]:
            if self.auto_point:
                if var[2]:
                    index=self.find_vars(list(self.stack.keys()),name)
                    if not index=="death":
                        vtype=self.stack[name]
                        if vtype=="array":
                            counter+=1
                            outstring+=name
                            outstring+="["
                            outstring+=self.strlist[counter]
                            outstring+="]"
                        elif vtype=="scaler":
                            outstring+="*"
                            outstring+=name
                        else:
                            return [2]
                    else:
                        index=self.find_vars(list(self.heap.keys()),name)
                        if not index=="death":
                            vtype=self.heap[name]
                            if vtype=="array":
                                counter+=1
                                outstring+=name
                                outstring+="["
                                outstring+=self.strlist[counter]
                                outstring+="]"
                            elif vtype=="scaler":
                                outstring+="*"
                                outstring+=name
                            else:
                                return [3]
                        else:
                            temp=counter+1
                            temp=self.strlist[temp]
                            if temp=="POINTEROFFSETSTART_TOKEN_GOLD":
                                counter+=2
                                outstring+=name
                                outstring+="["
                                outstring+=self.strlist[counter]
                                counter+=1
                                if self.strlist[counter]=="POINTEROFFSETEND_TOKEN_GOLD":
                                    outstring+="]"
                                else:
                                    return [13]
                            else:
                                outstring+="*"
                                outstring+=name
                else:
                    return [10]
            else:
                temp=counter+1
                temp=self.strlist[temp]
                if temp=="POINTEROFFSETSTART_TOKEN_GOLD":
                    counter+=2
                    outstring+=name
                    outstring+="["
                    outstring+=self.strlist[counter]
                    counter+=1
                    if self.strlist[counter]=="POINTEROFFSETEND_TOKEN_GOLD":
                        outstring+="]"
                    else:
                        return [13]
                elif temp=="POINTER_TOKEN_GOLD":
                    counter+=1
                    outstring+="*"
                    outstring+=name
        else:
            temp=counter+1
            temp=self.strlist[temp]
            if temp=="POINTEROFFSETSTART_TOKEN_GOLD":
                counter+=2
                outstring+=name
                outstring+="["
                outstring+=self.strlist[counter]
                counter+=1
                if self.strlist[counter]=="POINTEROFFSETEND_TOKEN_GOLD":
                    outstring+="]"
                else:
                    return [13]
        return [outstring,counter,var]
    def compileCppTypes(self,outstring,counter,name):
        outstring+=name
        counter+=1
        pointer=False
        tempstring=self.strlist[counter]
        if tempstring=="POINTER_TOKEN_GOLD":
            outstring+="*"
            pointer=True
            counter+=1
            tempstr=self.strlist[counter]
        outstring+=" "
        outstring+=tempstring
        self.varlist.update({tempstring:[pointer,name,False]})
        return [outstring,counter]
    def compileCppBetter(self,file,show,direct):
        count=self.count
        lists=self.strlist
        counter=0
        clist=file.split(".")
        clist=clist[:-1]
        cname=".".join(clist)
        self.counter_o=0
        blocks=[]
        self.stack={}
        self.heap={}
        self.const={}
        self.varlist={}
        self.show=show
        prime_type=[{},{}]
        str_type=[{"push_back":[False,False,"void","void"],"clear":[False,False,"void","void"]},{}]
        infile_type=[{"open":[False,False,"void","void"],"close":[False,False,"void","void"]},{}]
        outfile_type=[{"open":[False,False,"void","void"],"close":[False,False,"void","void"]},{}]
        self.auto_point=True
        no_discard=False
        pointer_func=False
        after_assign=False
        array_func=False
        within_class=""
        before_stream=""
        next_block=""
        within_func=""
        counter_c=0
        member_var=False
        self.scopes={}
        self.func={}
        scope_counter=0
        last_var=["",False,"",False]
        character_func={"isalpha":[False,False,"bool","void"],"isdigit":[False,False,"bool","void"],"isalnum":[False,False,"bool","void"],"isspace":[False,False,"bool","void"]}
        system_func={"system":[False,False,"void","void"],"exit":[False,False,"void","void"]}
        outstring=""
        if self.flags[3]:
            if self.flags[4]:
                self.types={"int":prime_type,"bool":prime_type,"char":prime_type}
                self.impl={"b":"bool","B":"byte","c":"char","i":"int"}
            else:
                outstring+="typedef long long Int;\ntypedef unsigned long long nat;\ntypedef unsigned char byte;\n"
                self.types={"Int":prime_type,"nat":prime_type,"bool":prime_type,"char":prime_type,"byte":prime_type}
                self.impl={"b":"bool","B":"byte","c":"char","s":"Int","u":"nat"}
        else:
            self.func.update(system_func)
            self.func.update(character_func)
            self.impl={"b":"bool","B":"byte","c":"char","i":"ifstream","o":"ofstream","s":"Int","S":"string","u":"nat"}
            self.types={"Int":prime_type,"string":str_type,"nat":prime_type,"bool":prime_type,"char":prime_type,"byte":prime_type,"ifstream":infile_type,"ofstream":outfile_type}
            if self.flags[0]:
                outstring+="#include <iostream>\n"
            if self.flags[1]:
                outstring+="#include <fstream>\n"
            if self.flags[2]:
                outstring+="#include <string>\n"
            outstring+="#include <cstdlib>\nusing namespace std;\ntypedef long long Int;\ntypedef unsigned long long nat;\ntypedef unsigned char byte;\n"
        while counter<count:
            if show:
                print(counter)
            tempstring=lists[counter]
            match tempstring:
                case "ENDBLOCK_TOKEN_GOLD":
                    block=blocks.pop()
                    match block:
                        case "PROGRAM":
                            while len(self.stack)>0:
                                tempVar=self.stack.popitem()
                                tempstr=tempVar[1]
                                match tempstr:
                                    case "scaler":
                                        outstring+="delete "
                                    case "array":
                                        outstring+="delete[] "
                                    case _:
                                        return 2
                                outstring+=tempVar[0]
                                outstring+=";\n"
                                outstring+=self.IndentGold(self.counter_o)
                            tl=list(outstring)
                            tl.pop()
                            tl.pop()
                            outstring="".join(tl)
                            self.counter_o-=1
                            outstring+="}\n"
                            outstring+=self.indentGold(self.counter_o)
                        case "CONTAINS":
                            pass
                        case "PROCEDURE":
                            while len(self.stack)>0:
                                tempVar=self.stack.popitem()
                                tempstr=tempVar[1]
                                match tempstr:
                                    case "scaler":
                                        outstring+="delete "
                                    case "array":
                                        outstring+="delete[] "
                                    case _:
                                        return 2
                                outstring+=tempVar[0]
                                outstring+=";\n"
                                outstring+=self.IndentGold(self.counter_o)
                            tl=list(outstring)
                            tl.pop()
                            tl.pop()
                            outstring="".join(tl)
                            self.counter_o-=1
                            outstring+="}\n"
                            outstring+=self.indentGold(self.counter_o)
                        case "DECONSTRUCTOR":
                            while len(self.stack)>0:
                                tempVar=self.stack.popitem()
                                tempstr=tempVar[1]
                                match tempstr:
                                    case "scaler":
                                        outstring+="delete "
                                    case "array":
                                        outstring+="delete[] "
                                    case _:
                                        return 2
                                outstring+=tempVar[0]
                                outstring+=";\n"
                                outstring+=self.IndentGold(self.counter_o)
                            tl=list(outstring)
                            tl.pop()
                            tl.pop()
                            outstring="".join(tl)
                            self.counter_o-=1
                            outstring+="}\n"
                            outstring+=self.indentGold(self.counter_o)
                        case "CONSTRUCTOR":
                            while len(self.stack)>0:
                                tempVar=self.stack.popitem()
                                tempstr=tempVar[1]
                                match tempstr:
                                    case "scaler":
                                        outstring+="delete "
                                    case "array":
                                        outstring+="delete[] "
                                    case _:
                                        return 2
                                outstring+=tempVar[0]
                                outstring+=";\n"
                                outstring+=self.IndentGold(self.counter_o)
                            tl=list(outstring)
                            tl.pop()
                            tl.pop()
                            outstring="".join(tl)
                            self.counter_o-=1
                            outstring+="}\n"
                            outstring+=self.indentGold(self.counter_o)
                        case "FUNCTION":
                            tl=list(outstring)
                            tl.pop()
                            tl.pop()
                            outstring="".join(tl)
                            self.counter_o-=1
                            outstring+="}\n"
                            outstring+=self.indentGold(self.counter_o)
                        case "CLASS":
                            tl=list(outstring)
                            tl.pop()
                            tl.pop()
                            outstring="".join(tl)
                            self.counter_o-=1
                            outstring+="};\n"
                            outstring+=self.indentGold(self.counter_o)
                            within_class=""
                        case _:
                            self.counter_o-=1
                            tl=list(outstring)
                            tl.pop()
                            tl.pop()
                            outstring="".join(tl)
                            outstring+="}\n"
                            outstring+=self.indentGold(self.counter_o)
                case "STARTBLOCK_TOKEN_GOLD":
                    outstring+="{\n"
                    self.counter_o+=1
                    outstring+=self.indentGold(self.counter_o)
                    blocks+=[next_block]
                case "ENDSTATEMENT_TOKEN_GOLD":
                    match before_stream:
                        case "GOLD_DEFAULT_OUTSTREAM":
                            counter_temp=counter+1
                            tempstr=lists[counter_temp]
                            match tempstr:
                                case "SYSTEMOUT_TOKEN_GOLD":
                                    counter_temp+=1
                                    tstr=lists[counter_temp]
                                    match tstr:
                                        case "OUTSTREAM_TOKEN_GOLD":
                                            counter+=3
                                            outstring+=" << "
                                            tstring=lists[counter]
                                            outstring+=tstring
                                        case _:
                                            return 1
                                case _:
                                    outstring+=";\n"
                                    outstring+=self.indentGold(self.counter_o)
                                    before_stream=""
                        case _:
                            outstring+=";\n"
                            outstring+=self.indentGold(self.counter_o)
                            before_stream=""
                case "PROGRAM_TOKEN_GOLD":
                    outstring+="int main()"
                    next_block="PROGRAM"
                case "IF_TOKEN_GOLD":
                    outstring+="if"
                    counter+=1
                    tempstr=lists[counter]
                    next_block="IF"
                    match tempstr:
                        case "STARTEXPRESSION_TOKEN_GOLD":
                            temp=self.compileCppEx(outstring,counter,"CONTROL",last_var)
                            if len(temp==1:
                                return temp[0]
                            outstring=temp[0]
                            counter=temp[1]
                            last_var=temp[2]
                        case _:
                            return 13
                case "STRINGMARK_TOKEN_GOLD":
                    temp=self.compileString(outstring,counter)
                    outstring=temp[0]
                    counter=temp[1]
                case "DECONSTRUCTOR_TOKEN_GOLD":
                    if within_class=="":
                        return 9
                    outstring+="~"
                    outstring+=within_class
                    outstring+="()"
                    next_block="DECONSTRUCTOR"
                case "CONSTRUCTOR_TOKEN_GOLD":
                    if within_class=="":
                        return 9
                    outstring+=within_class
                    temp=self.compileCppEx(outstring,counter,"FUNCTION",last_var)
                    if len(temp)==1:
                        return temp[0]
                    outstring=temp[0]
                    counter=temp[1]
                    last_var=temp[2]
                    next_block="CONSTRUCTOR"
                case "PROCEDURE_TOKEN_GOLD":
                    outstring+="void "
                    counter+=1
                    tempstr=lists[counter]
                    outstring+=tempstr
                    if within_class=="":
                        self.func.update({tempstr:[False,False,"void","void"]})
                    else:
                        self.types[within_class][0].update({tempstr:[False,False,"void","void"]})
                    counter+=1
                    tempstr=lists[counter]
                    next_block="PROCEDURE"
                    match tempstr:
                        case "STARTEXPRESSION_TOKEN_GOLD":
                            temp=self.compileCppEx(outstring,counter,"FUNCTION",last_var)
                            if len(temp)==1:
                                return temp[0]
                            outstring=temp[0]
                            counter=temp[1]
                            last_var=temp[2]
                        case "STARTBLOCK_TOKEN_GOLD":
                            outstring+="(true){\n"
                            self.counter_o+=1
                            outstring+=self.indentGold(self.counter_o)
                            blocks+=[next_block]
                        case _:
                            outstring+="("
                            outstring+=tempstr
                            outstring+=")"
                case "FUNCTION_TOKEN_GOLD":
                    counter+=1
                    tempstr=lists[counter]
                    match tempstr:
                        case "STRING_TOKEN_GOLD":
                            if kernel:
                                return 5
                            ret_type="string"
                        case "INT_TOKEN_GOLD":
                            ret_type="Int"
                        case "NONE_TOKEN_GOLD":
                            ret_type="void"
                        case "NATURAL_TOKEN_GOLD":
                            ret_type="nat"
                        case "BOOL_TOKEN_GOLD":
                            ret_type="bool"
                        case "KERNEL_INT_TOKEN_GOLD":
                            ret_type="int"
                        case _:
                            ret_type=tempstr
                    outstring+=ret_type
                    if pointer_func:
                        outstring+="*"
                    outstring+=" "
                    if array_func:
                        point_type="array"
                    else:
                        point_type="scaler"
                    counter+=1
                    tempstr=lists[counter]
                    if within_class=="":
                        self.func.update({tempstr:[no_discard,pointer_func,ret_type,point_type]})
                    else:
                        self.types[within_class[0]].update({tempstr:[no_discard,pointer_func,ret_type,point_type]})
                    no_discard=False
                    pointer_func=False
                    array_func=False
                    ret_type=""
                    point_type=""
                    counter+=1
                    tempstr=lists[counter]
                    next_block="FUNCTION"
                    match tempstr:
                        case "STARTEXPRESSION_TOKEN_GOLD":
                            temp=self.compileCppEx(outstring,counter,"FUNCTION",last_var)
                            if len(temp)==1:
                                return temp[0]
                            outstring=temp[0]
                            counter=temp[1]
                            last_var=temp[2]
                        case "STARTBLOCK_TOKEN_GOLD":
                            outstring+="(){\n"
                            self.counter_o+=1
                            outstring+=self.indentGold(self.counter_o)
                            blocks+=[next_block]
                        case "ENDSTATEMENT_TOKEN_GOLD":
                            outstring+="();\n"
                            outstring+=self.indentGold(counter_o)
                        case _:
                            outstring+="("
                            outstring+=tempstr
                            outstring+=")"
                case "INT_TOKEN_GOLD":
                    counter+=1
                    tempstr=lists[counter]
                    outstring+="Int"
                    pointer=False
                    if tempstr=="POINTER_TOKEN_GOLD":
                        outstring+="*"
                        pointer=True
                        counter+=1
                        tempstr=lists[counter]
                    outstring+=" "
                    outstring+=tempstr
                    if member_var:
                        if not self.find_vars(list(self.typelist[within_class][1].keys()),tempstr)=="death":
                            return 11
                        self.typelist[within_class][1].update({tempstr:[pointer,"Int",False]})
                    else:
                        if not self.find_vars(list(self.varlist.keys()),tempstr)=="death":
                            return 11
                        self.varlist.update({tempstr:[pointer,"Int",False]})
                        if not scope_counter==0:
                            self.scopes[list(self.scopes.keys())[-1]]+=[tempstr]
                    member_var=False
                case "NATURAL_TOKEN_GOLD":
                    counter+=1
                    tempstr=lists[counter]
                    outstring+="nat"
                    pointer=False
                    if tempstr=="POINTER_TOKEN_GOLD":
                        outstring+="*"
                        pointer=True
                        counter+=1
                        tempstr=lists[counter]
                    outstring+=" "
                    outstring+=tempstr
                    if member_var:
                        if not self.find_vars(list(self.typelist[within_class][1].keys()),tempstr)=="death":
                            return 11
                        self.typelist[within_class][1].update({tempstr:[pointer,"nat",False]})
                    else:
                        if not self.find_vars(list(self.varlist.keys()),tempstr)=="death":
                            return 11
                        self.varlist.update({tempstr:[pointer,"nat",False]})
                        if not scope_counter==0:
                            self.scopes[list(self.scopes.keys())[-1]]+=[tempstr]
                    member_var=False
                case "STRING_TOKEN_GOLD":
                    if self.flags[3]:
                        return 5
                    counter+=1
                    tempstr=lists[counter]
                    outstring+="string"
                    pointer=False
                    if tempstr=="POINTER_TOKEN_GOLD":
                        outstring+="*"
                        pointer=True
                        counter+=1
                        tempstr=lists[counter]
                    outstring+=" "
                    outstring+=tempstr
                    if member_var:
                        if not self.find_vars(list(self.typelist[within_class][1].keys()),tempstr)=="death":
                            return 11
                        self.typelist[within_class][1].update({tempstr:[pointer,"string",False]})
                    else:
                        if not self.find_vars(list(self.varlist.keys()),tempstr)=="death":
                            return 11
                        self.varlist.update({tempstr:[pointer,"string",False]})
                        if not scope_counter==0:
                            self.scopes[list(self.scopes.keys())[-1]]+=[tempstr]
                    member_var=False
                case "BOOL_TOKEN_GOLD":
                    counter+=1
                    tempstr=lists[counter]
                    outstring+="bool"
                    pointer=False
                    if tempstr=="POINTER_TOKEN_GOLD":
                        outstring+="*"
                        pointer=True
                        counter+=1
                        tempstr=lists[counter]
                    outstring+=" "
                    outstring+=tempstr
                    if member_var:
                        if not self.find_vars(list(self.typelist[within_class][1].keys()),tempstr)=="death":
                            return 11
                        self.typelist[within_class][1].update({tempstr:[pointer,"bool",False]})
                    else:
                        if not self.find_vars(list(self.varlist.keys()),tempstr)=="death":
                            return 11
                        self.varlist.update({tempstr:[pointer,"bool",False]})
                        if not scope_counter==0:
                            self.scopes[list(self.scopes.keys())[-1]]+=[tempstr]
                    member_var=False
                case "CREATE_TOKEN_GOLD":
                    counter+=1
                    tempstr=lists[counter]
                    member=False
                    if tempstr=="GETATTRIBUTE_TOKEN_GOLD":
                        outstring+="this->"
                        counter+=1
                        tempstr=lists[counter]
                        member=True
                    outstring+=tempstr
                    if member:
                        if self.find_var(list(self.typelist[within_class][1].keys()),tempstr)=="death":
                            return 11
                        var=self.typelist[within_class][1][tempstr]
                    else:
                        if self.find_var(list(self.varlist.key()),tempstr)=="death":
                            return 11
                        var=self.varlist[tempstr]
                    if not var[0]:
                        return 10
                    if var[2]:
                        return 12
                    var[2]=True
                    if member:
                        self.typelist[within_class][1][tempstr]=var
                    else:
                        self.varlist[tempstr]=var
                    self.stack.update({tempstr:"scaler"})
                    outstring+="=new "
                    outstring+=var[1]
                    counter+=1
                    tempstr=lists[counter]
                    match tempstr:
                        case "STARTEXPRESSION_TOKEN_GOLD":
                            temp=self.compileCppEx(outstring,counter,"ALLOC",last_var)
                            if not len(temp)==2:
                                return temp[0]
                            outstring=temp[0]
                            counter=temp[1]
                            last_var=temp[2]
                        case "STRINGMARK_TOKEN_GOLD":
                            temp=self.compileString(outstring,counter)
                            outstring=temp[0]
                            counter=temp[1]
                        case _:
                            outstring+="("
                            outstring+=tempstr
                            outstring+=")"
                case "CREATEARRAY_TOKEN_GOLD":
                    counter+=1
                    tempstr=lists[counter]
                    member=False
                    if tempstr=="GETATTRIBUTE_TOKEN_GOLD":
                        outstring+="this->"
                        counter+=1
                        tempstr=lists[counter]
                        member=True
                    outstring+=tempstr
                    if member:
                        if self.find_vars(list(self.typelist[within_class][1].keys()),tempstr)=="death":
                            return 11
                        var=self.typelist[within_class][1][tempstr]
                    else:
                        if self.find_var(list(self.varlist.keys()),tempstr)=="death":
                            return 11
                        var=self.varlist[tempstr]
                    if not var[0]:
                        return 10
                    if var[2]:
                        return 12
                    var[2]=True
                    if member:
                        self.typelist[within_class][1][tempstr]=var
                    else:
                        self.varlist[tempstr]=var
                    self.stack.update({tempstr:"array"})
                    outstring+="=new "
                    outstring+=var[1]
                    outstring+="["
                    match tempstr:
                        case "STARTEXPRESSION_TOKEN_GOLD":
                            temp=self.compileCppEx(outstring,counter,"ALLOC",last_var)
                            if len(temp)==1:
                                return temp[0]
                            outstring=temp[0]
                            counter=temp[1]
                            last_var=temp[2]
                        case "STRINGMARK_TOKEN_GOLD":
                            return 12
                        case _:
                            outstring+="]"
                    outstring+="]{"
                    outstring+=var[1]
                    counter+=1
                    tempstr=lists[counter]
                    match tempstr:
                        case "STARTEXPRESSION_TOKEN_GOLD":
                            temp=self.compileCppEx(outstring,counter,kernel)
                            if len(temp)==1:
                                return temp[0]
                            outstring=temp[0]
                            counter=temp[1]
                        case "STRINGMARK_TOKEN_GOLD":
                            outstring+="("
                            temp=self.compileString(outstring,counter)
                            outstring=temp[0]
                            counter=temp[1]
                            outstring+=")"
                        case _:
                            outstring+="("
                            outstring+=tempstr
                            outstring+=")"
                    outstring+="}"
                #case "STACK_TO_HEAP_TOKEN_GOLD_COMPILER":
                #    self.heap.insert(self.stack.popitem())
                # case "HEAP_TO_STACK_TOKEN_GOLD_COMPILER":
                #    counter+=1
                #    tempstr=lists[counter]
                #    var_dat=self.heap.pop(tempstr,"INTERNAL_GOLD_COMPILER_ISSUE")
                #    if var_dat=="INTERNAL_GOLD_COMPILER_ISSUE":
                #        return 3
                #    self.stack.update({tempstr:var_dat})
                case "IMPORT_TOKEN_GOLD":
                    counter+=1
                    tempstr=lists[counter]
                    outstring+="#include \""
                    outstring+=tempstr
                    outstring+="\""
                    counter+=1
                    tempstr=lists[counter]
                    if tempstr=="ENDSTATEMENT_TOKEN_GOLD":
                        outstring+="\n"
                        outstring+=self.indentGold(counter_o)
                    else:
                        return 13
                case "IMPORTLIB_TOKEN_GOLD":
                    counter+=1
                    tempstr=lists[counter]
                    drc=""
                    if tempstr=="DIRECT_MOD_TOKEN_GOLD_COMPILER":
                        drc=direct
                        counter+=1
                        tempstr=lists[counter]
                    libfile=open(drc+tempstr+".func")
                    libcons=libfile.read().split("\n")
                    libfile.close()
                    self.loadLibFunc(libcons)
                    libfile=open(drc+tempstr+".types")
                    libcons=libfile.read().spilt("\n")
                    libfile.close()
                    self.loadLibType(libcons,drc)
                    libfile=open(drc+tempstr+".const")
                    libcons=libfile.read().split("\n")
                    libfile.close()
                    self.loadLibConst(libcons)
                    counter+=1
                    tempstr=lists[counter]
                    if not tempstr=="ENDSTATEMENT_TOKEN_GOLD":
                        return 13
                case "DISABLE_AUTO_POINTER_TOKEN_GOLD_COMPILER":
                    self.auto_point=False
                case "ENABLE_AUTO_POINTER_TOKEN_GOLD_COMPILER":
                    self.auto_point=True
                case "MOVE_TOKEN_GOLD_COMPILER":
                    counter+=1
                    tempstr=lists[counter]
                    match tempstr:
                        case "STACK_MOD_TOKEN_GOLD_COMPILER":
                            loc=0
                        case "HEAP_MOD_TOKEN_GOLD_COMPILER":
                            loc=1
                        case _:
                            return 10
                    match loc:
                        case 0:
                            counter+=1
                            tstr=lists[counter]
                            var_dat=self.heap.pop(tstr,"INTERNAL_GOLD_COMPILER_ISSUE")
                            if var_dat=="INTERNAL_GOLD_COMPILER_ISSUE":
                                return 3
                            self.stack.update({tstr:var_dat})
                        case 1:
                            self.heap.update(self.stack.popitem())
                        case _:
                            return 14
                case "RETURN_POINTER_MARKER_TOKEN_GOLD_COMPILER":
                    counter+=1
                    tempstr=lists[counter]
                    match tempstr:
                        case "STACK_MOD_TOKEN_GOLD_COMPILER":
                            loc=0
                        case "HEAP_MOD_TOKEN_GOLD_COMPILER":
                            loc=1
                        case _:
                            return 14
                    match loc:
                        case 0:
                            counter+=1
                            tstr=lists[counter]
                            var_dat=self.heap.pop(tstr,"INTERNAL_GOLD_COMPILER_ISSUE")
                            if var_dat=="INTERNAL_GOLD_COMPILER_ISSUE":
                                return 3
                        case 1:
                            self.stack.popitem()
                        case _:
                            return 14
                case "POINTER_FUNCTION_TOKEN_GOLD_COMPILER":
                    pointer_func=True
                case "ARRAY_POINTER_FUNCTION_TOKEN_GOLD_COMPILER":
                    array_func=True
                case "ASSIGNMENT_TOKEN_GOLD":
                    counter+=1
                    tempstr=lists[counter]
                    index=self.find_vars(list(self.varlist.keys()),tempstr)
                    self.after_assign=True
                    if index=="death":
                        index=self.find_vars(list(self.func.keys()),tempstr)
                        if index=="death":
                            return 11
                        temp=self.compileCppFunc(outstring,counter,tempstr,last_var=last_var,on="")
                        if len(temp)==1:
                            return temp[0]
                        outstring=temp[0]
                        counter=temp[1]
                        last_var=temp[2]
                    else:
                        var=self.varlist[tempstr]
                        outstring+=tempstr
                        temon=tempstr
                        tempstr=lists[counter+1]
                        if tempstr=="POINTERATTRIBUTE_TOKEN_GOLD":
                            if var[0]:
                                outstring+="->"
                            else:
                                outstring+="."
                            counter+=2
                            tempstr=lists[counter]
                            temp=self.compileCppNames(outstring,counter,last_var,"",tempstr)
                            if len(temp)==1:
                                return temp[0]
                            outstring=temp[0]
                            counter=temp[1]
                            last_var=temp[2]
                case "DESTROY_TOKEN_GOLD":
                    counter+=1
                    tempstr=lists[counter]
                    member=False
                    if tempstr=="GETATTRIBUTE_TOKEN_GOLD":
                        member=True
                        counter+=1
                        tempstr=lists[counter]
                    if self.auto_point:
                        point=self.heap.pop(tempstr,"INTERNAL_GOLD_COMPILER_ISSUE")
                        if point=="INTERNAL_GOLD_COMPILER_ISSUE":
                            return 10
                        if point=="scaler":
                            outstring+="delete "
                        elif point=="array":
                            outstring+="delete[] "
                        else:
                            return 3
                        if member:
                            outstring+="this->"
                        outstring+=tempstr
                        self.heap.pop(tempstr)
                    else:
                        return 10
                case "DELETE_TOKEN_GOLD":
                    counter+=1
                    tempstr=lists[counter]
                    member=False
                    if tempstr=="GETATTRIBUTE_TOKEN_GOLD":
                        member=True
                        counter+=1
                        tempstr=lists[counter]
                    if self.auto_point:
                        point=self.heap.pop(tempstr,"INTERNAL_GOLD_COMPILER_ISSUE")
                        if not point=="scaler":
                            return 10
                    outstring+="delete "
                    if member:
                        outstring+="this->"
                    outstring+=tempstr
                case "DELETEARRAY_TOKEN_GOLD":
                    counter+=1
                    tempstr=lists[counter]
                    member=False
                    if tempstr=="GETATTRIBUTE_TOKEN_GOLD":
                        member=True
                        counter+=1
                        tempstr=lists[counter]
                    if self.auto_point:
                        point=self.heap.pop(tempstr,"INTERNAL_GOLD_COMPILER_ISSUE")
                        if not point=="array":
                            return 10
                    outstring+="delete[] "
                    if member:
                        outstring+="this->"
                    outstring+=tempstr
                case "STARTEXPRESSION_TOKEN_GOLD":
                    temp=self.compileCppEx(outstring,counter,"ALL",last_var)
                    if len(temp)==1:
                        return temp[0]
                    outstring=temp[0]
                    counter=temp[1]
                    last_var=temp[2]
                case "CONSTANT_TOKEN_GOLD":
                    counter+=1
                    tempstr=lists[counter]
                    counter+=1
                    tstr=lists[counter]
                    self.const.update({tempstr:tstr})
                case "BEGINCOMMENT_TOKEN_GOLD":
                    while True:
                        counter+=1
                        tempstr=lists[counter]
                        if tempstr=="ENDCOMMENT_TOKEN_GOLD":
                            break
                case "POINTEROFFSETSTART_TOKEN_GOLD":
                    outstring+="["
                    while True:
                        counter+=1
                        tempstr=lists[counter]
                        if tempstr=="POINTEROFFSETEND_TOKEN_GOLD":
                            outstring+="]"
                            break
                        elif tempstr=="STARTEXPRESSION_TOKEN_GOLD":
                            temp=self.compileCppEx(outstring,counter,"ALL",last_var)
                            if len(temp)==1:
                                return temp[0]
                            outstring=temp[0]
                            counter=temp[1]
                            last_var=temp[2]
                        elif tempstr=="ENDSTATEMENT_TOKEN_GOLD":
                            outstring+="0]"
                            break
                        else:
                            temp=self.compileCppNames(outstring,counter,last_var,"",tempstring)
                            if len(temp)==1:
                                return temp[0]
                            outstring=temp[0]
                            counter=temp[1]
                            last_var=temp[2]
                case "SYSTEMOUT_TOKEN_GOLD":
                    if self.flags[3]:
                        return 5
                    outstring+="cout"
                    before_stream="GOLD_DEFAULT_OUTSTREAM"
                case "OUTSTREAM_TOKEN_GOLD":
                    if before_stream=="GOLD_DEFAULT_INSTREAM":
                        return 1
                    outstring+=" << "
                case "INSTREAM_TOKEN_GOLD":
                    if before_stream=="GOLD_DEFAULT_OUTSTREAM" or before_stream=="GOLD_DEFAULT_ERRORSTREAM" or before_stream=="GOLD_DEFAULT_ERRORLOGGER":
                        return 1
                    outstring+=" >> "
                case "CHARACTER_TOKEN_GOLD":
                    counter+=1
                    tempstr=lists[counter]
                    outstring+="char"
                    pointer=False
                    if tempstr=="POINTER_TOKEN_GOLD":
                        outstring+="*"
                        pointer=True
                        counter+=1
                        tempstr=lists[counter]
                    outstring+=" "
                    outstring+=tempstr
                    if member_var:
                        if not self.find_vars(list(self.typelist[within_class][1].keys()),tempstr)=="death":
                            return 11
                        self.typelist[within_class][1].update({tempstr:[pointer,"char",False]})
                    else:
                        if not self.find_vars(list(self.varlist.keys()),tempstr)=="death":
                            return 11
                        self.varlist.update({tempstr:[pointer,"char",False]})
                        if not scope_counter==0:
                            self.scopes[list(self.scopes.keys())[-1]]+=[tempstr]
                    member_var=False
                case "END_SCOPE_TOKEN_GOLD_COMPILER":
                    temp=self.scopes[list(self.scopes.key())[-1]]
                    scope_counter-1
                    sc=0
                    cm=len(max)
                    while sc<cm:
                        self.varlist.pop(temp[sc])
                        sc+=1
                case "START_SCOPE_TOKEN_GOLD_COMPILER":
                    self.scopes.update({("scope"+str(scope_counter)):[]})
                    scope_counter+=1
                case "MEMBER_TOKEN_GOLD":
                    member_var=True
                case "INFILESTREAM_TOKEN_GOLD":
                    if self.flags[3]:
                        return 5
                    counter+=1
                    tempstr=lists[counter]
                    outstring+="ifstream"
                    pointer=False
                    if tempstr=="POINTER_TOKEN_GOLD":
                        outstring+="*"
                        pointer=True
                        counter+=1
                        tempstr=lists[counter]
                    outstring+=" "
                    outstring+=tempstr
                    if member_var:
                        if not self.find_vars(list(self.typelist[within_class][1].keys()),tempstr)=="death":
                            return 11
                        self.typelist[within_class][1].update({tempstr:[pointer,"ifstream",False]})
                    else:
                        if not self.find_vars(list(self.varlist.keys()),tempstr)=="death":
                            return 11
                        self.varlist.update({tempstr:[pointer,"ifstream",False]})
                        if not scope_counter==0:
                            self.scopes[list(self.scopes.key())[-1]]+=[tempstr]
                    member_var=False
                case "OUTFILESTREAM_TOKEN_GOLD":
                    if self.flags[3]:
                        return 5
                    counter+=1
                    tempstr=lists[counter]
                    outstring+="ofstream"
                    pointer=False
                    if tempstr=="POINTER_TOKEN_GOLD":
                        outstring+="*"
                        pointer=True
                        counter+=1
                        tempstr=lists[counter]
                    outstring+=" "
                    outstring+=tempstr
                    if member_var:
                        if not self.find_vars(list(self.typelist[within_class][1].keys()),tempstr)=="death":
                            return 11
                        self.typelist[within_class][1].update({tempstr:[pointer,"ofstream",False]})
                    else:
                        if not self.find_vars(list(self.varlist.keys()),tempstr)=="death":
                            return 11
                        self.varlist.update({tempstr:[pointer,"ofstream",False]})
                        if not scope_counter==0:
                            self.scopes[list(self.scopes.keys())[-1]]+=[tempstr]
                case "DO_NOT_DISCARD_TOKEN_GOLD_COMPILER":
                    no_discard=True
                #case "CHECK_HEAP_TOKEN_GOLD_COMPILER":
                #    check_count=0
                #    check_amount=len(list(self.heap.keys()))
                #    while check_count<check_amount:
                #        print(list(self.heap.keys())[check_count]+list(self.heap.values())[check_count])
                #        check_count+=1
                #case "CHECK_STACK_TOKEN_GOLD_COMPILER":
                #    check_count=0
                #    check_amount=len(list(self.stack.keys()))
                #    while check_count<check_amount:
                #        print(list(self.stack.keys())[check_count]+":"+list(self.stack.values())[check_count])
                #        check_count+=1
                case "CHECK_TOKEN_GOLD_COMPILER":
                    counter+=1
                    tempstr=lists[counter]
                    match tempstr:
                        case "STACK_MOD_TOKEN_GOLD_COMPILER":
                            temp=self.stack
                        case "HEAP_MOD_TOKEN_GOLD_COMPILER":
                            temp=self.heap
                        case "VARS_MOD_TOKEN_GOLD_COMPILER":
                            temp=self.varlist
                        case "CONSTANT_MOD_TOKEN_GOLD_COMPILER":
                            temp=self.const
                        case "TYPES_MOD_TOKEN_GOLD_COMPILER":
                            temp=self.typelist
                        case "FUNC_MOD_TOKEN_GOLD_COMPILER":
                            temp=self.func
                        case _:
                            return 10
                    check_amount=len(list(temp.keys()))
                    while check_count<check_amount:
                        print(f"{list(temp.keys())[check_amount]}:{list(temp.values())[check_amount]}")
                        check_count+=1
                case "CLASS_TOKEN_GOLD":
                    counter+=1
                    tempstr=lists[counter]
                    temp=tempstr
                    if tempstr=="STARTEXPRESSION_TOKEN_GOLD":
                        temp=""
                        while True:
                            counter+=1
                            tempstr=lists[counter]
                            if tempstr=="ENDEXPRESSION_TOKEN_GOLD":
                                break
                            else:
                                temp+=tempstr
                    outstring+="class "
                    outstring+=temp
                    within_class=temp
                    next_block="CLASS"
                case "NAMEDCLASS_TOKEN_GOLD":
                    outstring+="class "
                    outstring+=cname
                    outstring+=str(counter_c)
                    within_class=cname+str(counter_c)
                    counter_c+=1
                case "CONTAINS_TOKEN_GOLD":
                    ls=list(outstring)
                    ls.pop()
                    ls.pop()
                    outstring="".join(ls)
                    outstring+="public:\n"
                    outstring+=self.indentGold(counter_o)
                    counter+=1
                    tempstr=lists[counter]
                    if not tempstr=="STARTBLOCK_TOKEN_GOLD":
                        return 13
                    blocks+=["CONTAINS"]
                case "SYSTEMIN_TOKEN_GOLD":
                    if self.flags[3]:
                        return 5
                    outstring+="cin"
                    before_stream="GOLD_DEFAULT_INSTREAM"
                case "ELIF_TOKEN_GOLD":
                    ls=list(outstring)
                    ls.pop()
                    ls.pop()
                    outstring="".join(ls)
                    outstring+="}else if"
                    counter+=1
                    tempstr=lists[counter]
                    if tempstr=="STARTEXPRESSION_TOKEN_GOLD":
                        temp=self.compileCppEx(outstring,compiler,"CONTROL",last_var)
                        if len(temp)==1:
                            return temp[0]
                        outstring=temp[0]
                        counter=temp[1]
                        last_var=temp[2]
                    else:
                        return 13
                    counter+=1
                    tempstr=lists[counter]
                    if tempstr=="STARTBLOCK_TOKEN_GOLD":
                        outstring+="{\n"
                        outstring+=self.indentGold(counter_o)
                    else:
                        return 13
                case "ELSE_TOKEN_GOLD":
                    ls=list(outstring)
                    ls.pop()
                    ls.pop()
                    outstring="".join(ls)
                    outstring+="}else"
                    counter+=1
                    tempstr=lists[counter]
                    if tempstr=="STARTBLOCK_TOKEN_GOLD":
                        outstring+="{\n"
                        outstring+=self.indentGold(counter_o)
                    else:
                        return 13
                case "TRUE_TOKEN_GOLD":
                    outstring+="true"
                case "FALSE_TOKEN_GOLD":
                    outstring+="false"
                case "TYPEDEF_TOKEN_GOLD":
                    outstring+="typedef"
                    while True:
                        counter+=1
                        tempstr=lists[counter]
                        if tempstr=="ENDSTATEMENT_TOKEN_GOLD":
                            outstring+=";\n"
                            outstring+=self.indentGold(counter_o)
                            break
                        else:
                            outstring+=" "
                            outstring+=tempstr
                case "WHILE_TOKEN_GOLD":
                    outstring+="while"
                    counter+=1
                    tempstr=lists[counter]
                    if tempstr=="STARTEXPRESSION_TOKEN_GOLD":
                        temp=self.compileCppEx(outstring,counter,"CONTROL",last_var)
                        if len(temp)==1:
                            return temp[0]
                        outstring=temp[0]
                        counter=temp[1]
                        last_var=temp[2]
                    else:
                        return 13
                    next_block="WHILE"
                case "INCREMENT_TOKEN_GOLD":
                    outstring+="++"
                case "DECREMENT_TOKEN_GOLD":
                    outstring+="--"
                case "ADDASI_TOKEN_GOLD":
                    outstring+="+="
                    counter+=1
                    tempstr=lists[counter]
                    match tempstr:
                        case "STRINGMARK_TOKEN_GOLD":
                            temp=self.compileString(outstring,counter)
                            if len(temp)==1:
                                return temp[0]
                            outstring=temp[0]
                            counter=temp[1]
                        case "STARTEXPRESSION_TOKEN_GOLD":
                            temp=self.compileCppEx(outstring,counter,"ALLOC",last_var)
                            if len(temp)==1:
                                return temp[0]
                            outstring=temp[0]
                            counter=temp[1]
                            last_var=temp[2]
                        case _:
                            temp=self.compileCppNames(outstring,counter,last_var,"",tempstr)
                            if len(temp)==1:
                                return temp[0]
                            outstring=temp[0]
                            counter=temp[1]
                            last_var=temp[2]
                case "SUBTRACTIONASSIGNMENT_TOKEN_GOLD":
                    outstring+="-="
                    counter+=1
                    tempstr=lists[counter]
                    match tempstr:
                        case "STRINGMARK_TOKEN_GOLD":
                            temp=self.compileString(outstring,counter)
                            if len(temp)==1:
                                return temp[0]
                            outstring=temp[0]
                            counter=temp[1]
                        case "STARTEXPRESSION_TOKEN_GOLD":
                            temp=self.compileCppEx(outstring,counter,"ALLOC",last_var)
                            if len(temp)==1:
                                return temp[0]
                            outstring=temp[0]
                            counter=temp[1]
                            last_var=temp[2]
                        case _:
                            temp=self.compileCppNames(outstring,counter,last_var,"",tempstr)
                            if len(temp)==1:
                                return temp[0]
                            outstring=temp[0]
                            counter=temp[1]
                            last_var=temp[2]
                case "BYTE_TOKEN_GOLD":
                    if self.flags[3] and self.flags[4]:
                        return 17
                    counter+=1
                    tempstr=lists[counter]
                    outstring+="byte"
                    pointer=False
                    if tempstr=="POINTER_TOKEN_GOLD":
                        outstring+="*"
                        pointer=True
                        counter+=1
                        tempstr=lists[counter]
                    outstring+=" "
                    outstring+=tempstr
                    if member_var:
                        if not self.find_vars(list(self.typelist[within_class][1].keys()),tempstr)=="death":
                            return 11
                        self.typelist[within_class][1].update({tempstr:[pointer,"byte",False]})
                    else:
                        if not self.find_vars(list(self.varlist.keys()),tempstr)=="death":
                            return 11
                        self.varlist.update({tempstr:[pointer,"byte",False]})
                        if not scope_count==0:
                            self.scopes[list(self.scopes.keys())[-1]]+=[tempstr]
                case "SUBTRACTION_TOKEN_GOLD":
                    outstring+="-"
                case "IMPL_TOKEN_GOLD":
                    counter+=1
                    tempstr=lists[counter]
                    pointer=False
                    if tempstr=="POINTER_TOKEN_GOLD":
                        pointer=True
                        counter+=1
                        tempstr=lists[counter]
                    var_type="Int"
                    if not self.find_vars(list(self.impl.keys()),tempstr[0])=="death":
                        var_type=self.impl[tempstr[0]]
                    outstring+=var_type
                    if pointer:
                        outstring+="*"
                    outstring+=" "
                    if member_var:
                        if not self.find_vars(list(self.typelist[within_class][1].keys()),tempstr)=="death":
                            return 11
                        self.typelist[within_class][1].update({tempstr:[pointer,var_type,False]})
                    else:
                        if not self.find_vars(list(self.varlist.keys()),tempstr)=="death":
                            return 11
                        self.varlist.update({tempstr:[pointer,var_type,False]})
                        if not scope_count==0:
                            self.scopes[list(self.scopes.keys())[-1]]+=[tempstr]
                case "LETTER_TOKEN_GOLD":
                    counter+=1
                    tempstr=lists[counter]
                    if not (self.find_vars(list(self.impl.keys()),tempstr)=="death" or len(tempstr)==1):
                        return 13
                    if not self.find_vars(list(self.impl.values()),within_class)=="death":
                        return 15
                    self.impl.update({tempstr:within_class})
                    counter+=1
                    tempstr=lists[counter]
                    if not tempstr=="ENDSTATEMENT_TOKEN_GOLD":
                        return 13
                case "UNLESS_TOKEN_GOLD":
                    outstring+="if(!"
                    counter+=1
                    tempstr=lists[counter]
                    next_block="IF"
                    if not tempstr=="STARTEXPRESSION_TOKEN_GOLD":
                        return 13
                    temp=self.compileCppEx(outstring,counter,"CONTROL",last_var)
                    if len(temp)==1:
                        return temp[0]
                    outstring=temp[0]
                    counter=temp[1]
                    last_var=temp[2]
                    outstring+=")"
                case "UNTIL_TOKEN_GOLD":
                    outstring+="while(!"
                    counter+=1
                    tempstr=lists[counter]
                    if not tempstr=="STARTEXPRESSION_TOKEN_GOLD":
                        return 13
                    temp=self.compileCppEx(outstring,counter,"CONTROL",last_var)
                    if len(temp)==1:
                        return temp[0]
                    outstring=temp[0]
                    counter=temp[1]
                    last_var=temp[2]
                    outstring+=")"
                    next_block="WHILE"
                case "RETURN_TOKEN_GOLD":
                    while len(self.stack)>0:
                        temp_var=self.stack.popitem()
                        match temp_var[1]:
                            case "scaler":
                                outstring+="delete "
                            case "array":
                                outstring+="delete[] "
                            case _:
                                return 2
                        outstring+=temp_var[0]
                        outstring+=";\n"
                    outstring+="return "
                    counter+=1
                    tempstr=lists[counter]
                    temp=self.compileCppNames(outstring,counter,last_var,"",tempstring)
                    if len(temp)==1:
                        return temp[0]
                    outstring=temp[0]
                    counter=temp[1]
                    last_var=temp[2]
                    outstring+=";"
                case "SYSTEMERR_TOKEN_GOLD":
                    if self.flags[3]:
                        return 5
                    outstring+="cerr"
                    before_stream="GOLD_DEFAULT_ERRORSTREAM"
                case "SYSTEMLOG_TOKEN_GOLD":
                    if self.flags[3]:
                        return 5
                    outstring+="clog"
                    before_stream="GOLD_DEFAULT_ERRORLOGGER"
                case "KERNEL_INT_TOKEN_GOLD":
                    outstring+="int"
                    counter+=1
                    tempstr=lists[counter]
                    pointer=False
                    if tempstr=="POINTER_TOKEN_GOLD":
                        pointer=True
                        counter+=1
                        outstring+="*"
                        tempstr=lists[counter]
                    outstring+=" "
                    if member_var:
                        if not self.find_vars(list(self.typelist[within_class][1].keys()),tempstr)=="death":
                            return 11
                        self.typelist[within_class][1].update({tempstr:[pointer,"int",False]})
                    else:
                        if not self.find_var(list(self.varlist.keys()),tempstr)=="death":
                            return 11
                        self.varlist.update({tempstr:[pointer,"int",False]})
                case "UNSIGNED_TOKEN_GOLD":
                    outstring+="unsigned "
                case "SIGNED_TOKEN_GOLD":
                    outstring+="signed "
                case "LONG_TOKEN_GOLD":
                    outstring+="long "
                case "SHORT_TOKEN_GOLD":
                    outstring+="short "
                case "BREAK_TOKEN_GOLD":
                    outstring+="break"
                case "TRY_TOKEN_GOLD":
                    outstring+="try"
                    next_block="TRY"
                case "EXCEPT_TOKEN_GOLD":
                    ls=list(outstring)
                    ls.pop()
                    ls.pop()
                    outstring="".join(ls)
                    outstring+="}except(...)"
                    counter+=1
                    tempstr=lists[counter]
                    if not tempstr=="STARTEXPRESSION_TOKEN_GOLD":
                        return 13
                    outstring+="{\n"
                    outstring+=self.indentGold(counter_o)
                case _:
                    if self.flags[3] and self.flags[4]:
                        outstring+=tempstring
                    else:
                        temp=self.compileCppNames(outstring,counter,last_var,"",tempstring)
                        if len(temp)==1:
                            return temp[0]
                        outstring=temp[0]
                        counter=temp[1]
                        last_var=temp[2]
                        after_assign=False
            counter+=1
        outfile=open(file,mode="w+")
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
                    tlist=tempstring.split("%_")
                    tempstring=" ".join(tlist)
                    tlist=tempstring.split("%~")
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
                    tlist=tempstring.split("%_")
                    tempstring=" ".join(tlist)
                    tlist=tempstring.split("%~")
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
                    ts=tempstring.split("%_")
                    tempstring=" ".join(ts)
                    ts=tempstring.split("%~")
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
                    tlist=tempstr.split("%_")
                    tempstr=" ".join(tlist)
                    tlist=tempstr.split("%~")
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
                    tlist=tempstrt.split("%_")
                    tempstrt=" ".join(tlist)
                    tlist=tempstrt.split("%~")
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
                tlist=tstr.split("%_")
                tstr=" ".join(tlist)
                tlist=tstr.split("%~")
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
                tlist=tempstring.split("%_")
                tempstring=" ".join(tlist)
                tlist=tempstring.split("%~")
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
                    tlist=tempstring.split("%_")
                    tempstring=" ".join(tlist)
                    tlist=tempstring.split("%~")
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
                    tlist=tstrt.split("%_")
                    tstrt=" ".join(tlist)
                    tlist=tstrt.split("%~")
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
                tlist=tempstring.split("%_")
                tempstring=" ".join(tlist)
                tlist=tempstring.split("%~")
                tempstring="".join(tlist)
                outstring+=tempstring
            counter+=1
        outfile.write(outstring)
        outfile.close()
        return 0
    def run(self,direct,file,lang,st,km,manual,better):
        infile=direct+file+".aur_gold"
        self.tokenizeGold(infile)
        if not manual:
            os.remove(infile)
            print("\033[38;2;0;255;0mRemoved preprocess file["+file+"]\033[0m")
        match lang:
            case "java":
                outfile=direct+file+".java"
                error=self.compileJava(outfile)
            case "fortran":
                outfile=direct+file+".f90"
                error=self.compileFort(outfile)
            case "c_plus_plus":
                outfile=direct+file+".cpp"
                if better:
                    error=self.compileCppBetter(outfile,st,direct)
                else:
                    error=self.compileCpp(outfile,st,km)
            case "c_plus_plus_header":
                outfile=direct+file+".hpp"
                if better:
                    error=self.compileCppBetter(outfile,st,direct)
                else:
                    error=self.compileCpp(outfile,st,km)
            case _:
                error=(0-1)
        match error:
            case -1:
                print("\033[38;2;0;255;0mNot a compiler option\033[0m")
            case 0:
                print("\033[38;2;0;255;0mSuccessful compilation of file["+file+"]\033[0m")
            case 1:
                print("\033[38;2;255;0;0mStream error in file["+file+"]\033[0m")
            case 2:
                print("\033[38;2;255;0;0mStack error in file["+file+"]\033[0m")
            case 3:
                print("\033[38;2;255;0;0mHeap error in file["+file+"]\033[0m")
            case 4:
                print("\033[38;2;255;0;0mFunction usage error in file["+file+"]\033[0m")
            case 5:
                print("\033[38;2;255;0;0mKernel mode error in file["+file+"]\033[0m")
            case 6:
                print("\033[38;2;255;0;0mControl flow error in file["+file+"]\033[0m")
            case 7:
                print("\033[38;2;255;0;0mFunction definition error in file["+file+"\033[0m")
            case 8:
                print("\033[38;2;255;0;0mAccess error in file["+file+"]\033[0m")
            case 9:
                print("\033[38;2;255;0;0mClass error in file["+file+"]\033[0m")
            case 10:
                print("\033[38;2;255;0;0mPointer error in file["+file+"]\033[0m")
            case 11:
                print("\033[38;2;255;0;0mVariable error in file["+file+"]\033[0m")
            case 12:
                print("\033[38;2;255;0;0mAllocation error in file["+file+"]\033[0m")
            case 13:
                print("\033[38;2;255;0;0mSyntax error in file["+file+"]\033[0m")
            case 14:
                print("\033[38;2;255;0;0mCompiler data corrupted during compilation of file["+file+"]\033[0m")
            case 15:
                print("\033[38;2;255;0;0mAlready has a letter in file["+file+"]\033[0m")
            case 16:
                print("\033[38;2;255;0;0mReally unsafe code in file["+file+"]\033[0m")
            case 17:
                print("\033[38;2;255;0;0mLinux-kernel mode error in file["+file+"]\033[0m")
            case _:
                pass
if __name__=="__main__":
    comp=compilerGold()
    a=input()
    b=input()
    c=(input()=="show")
    d=(input()=="kernel")
    e=(input()=="best")
    comp.run("",a,b,c,d,True,e)
