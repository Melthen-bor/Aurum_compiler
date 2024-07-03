import compiler as cmp
import preprocessor as pp
import package_manager as pm
while 1==1:
    cmd=input()
    flags=cmd.split(" ")
    flag_pack=False
    flag_redo=False
    flag_setup=False
    flag_show=False
    flag_lang="java"
    flag_obj=False
    flag_kernel=False
    flag_exit=False
    flag_impr=False
    flag_test=False
    flags_linux=False
    pack_name=flags[0]
    manager=pm.Manager(flags[1])
    pack_loc=flags[2]
    count=3
    while count<len(flags):
        if flags[count]=="-java":
            flag_lang="java"
        elif flags[count]=="-fort":
            flag_lang="fortran"
        elif flags[count]=="-cpp":
            flag_lang="c_plus_plus"
        elif flags[count]=="-cpp_h":
            flag_lang="c_plus_plus_header"
        elif flags[count]=="-show":
            flag_show=True
        elif flags[count]=="-kernel":
            flag_kernel=True
        elif flags[count]=="-update":
            flag_redo=True
        elif flags[count]=="-new":
            flag_setup=True
        elif flags[count]=="-old":
            flag_setup=False
        elif flags[count]=="-complete":
            flag_redo=False
        elif flags[count]=="-package":
            flag_pack=True
        elif flags[count]=="-compile":
            flag_pack=False
        elif flags[count]=="-obj":
            flag_obj=True
        elif flags[count]=="-noObj":
            flag_obj=False
        elif flags[count]=="-app":
            flag_kernel=False
        elif flags[count]=="-hide":
            flag_show=False
        elif flags[count]=="-last":
            flag_exit=True
        elif flags[count]=="-continue":
            flag_exit=False
        elif flags[count]=="-test":
            flag_impr=True
        elif flags[count]=="-stable":
            flag_impr=False
        elif flags[count]=="-debug":
            flag_test=True
        elif flags[count]=="-release":
            flag_test=False
        elif flags[count]=="-linux":
            flags_linux=True
        elif flags[count]=="-other":
            flags_linux=False
        count+=1
    if flag_pack:
        if flag_setup:
            if flag_redo:
                manager.reset_Package(pack_name)
            else:
                manager.set_Up_Package(pack_name,pack_loc)
        else:
            if flag_redo:
                manager.update_Package(pack_name)
            else:
                manager.use_Package(pack_name,pack_loc)
    else:
        if flag_setup:
            files_metadata=open(pack_loc+pack_name+".compile.metadata","w+")
            files_metadata.write("main")
            files_metadata.close()
            files_metadata=open(pack_loc+pack_name+".packages.metadata","w+")
            if not flag_kernel:
                files_metadata.write("std")
            files_metadata.close()
        else:
            files_metadata=open(pack_loc+pack_name+".packages.metadata")
            packages=files_metadata.read().split("\n")
            files_metadata.close()
            amount=len(packages)
            count=0
            while count<amount:
                manager.use_Package(packages[count],pack_loc,project=pack_name)
                count+=1
            compiler=cmp.compilerGold(flag_kernel,flag_linux)
            preprocessor=pp.preprocessor("aur","aurobj","aur_gold")
            files_metadata=open(pack_loc+pack_name+".compile.metadata")
            files=files_metadata.read().split("\n")
            amount=len(files)
            count=0
            while count<amount:
                if not flag_redo:
                    print("\033[38;2;0;255;0mStarting preprocessing of "+files[count]+"\033[0m")
                    preprocessor.directives(files[count],flag_obj,flag_lang,pack_loc,flag_impr,flag_test)
                print("\033[38;2;0;255;0mStarting compilation of "+files[count]+"\033[0m")
                compiler.run(pack_loc,files[count],flag_lang,flag_show,flag_kernel,False,flag_impr)
                count+=1
            #count=0
            #amount=len(packages)
            #while count<amount:
                #manager.deactivate_Package(packages[count],pack_loc,project=pack_name)
                #count+=1
    if flag_exit:
        break