import os
class Package:
    def __init__(self,name,location):
        self.files=[]
        self.loc=location
        self.nomen=name
        self.cf=0
        self.version=0
    def add_File(self,name):
        self.files+=[name]
        self.cf+=1
    def copy_Files(self,build_Directory,project_name):
        count=0
        while count<self.cf:
            name=self.files[count]
            namloc=self.loc+name
            fin=open(namloc)
            fcons=fin.read()
            fin.close()
            namloc=build_Directory+self.nomen+"."+name
            fout=open(namloc,"w+")
            fout.write(fcons)
            fout.close()
            count+=1
        print("\033[38;2;0;255;0mProject["+project_name+"] successfully uses package["+self.nomen+"] with version:"+str(self.version)+"\033[0m")
    def remove_File(self,name):
        index=findin(self.files,name)
        if index==len(self.files):
            return 1
        self.files.remove(index)
    def clear_Files(self):
        self.files=[]
        self.cf=0
    def deactivate_Files(self,build_Directory,project_name):
        count=0
        while count<self.cf:
            name=self.files[count]
            namloc=build_Directory+self.nomen+"."+name
            os.remove(namloc)
            count+=1
        print("\033[38;2;0;255;0mRemoved package["+self.nomen+"] with version: "+str(self.version)+"files from project["+project_name+"]\033[0m")
class Manager:
    def __init__(self,location):
        self.packages=[]
        self.loc=location
        metadata_File=open(self.loc+"karot.metadata")
        self.metadata=metadata_File.read().split("\n")
        metadata_File.close()
        self.cp=int(self.metadata[0])
        count=0
        while count<self.cp:
            package_Name=self.metadata[count+1]
            metadata_File=open(self.loc+package_Name+".metadata")
            metadata_Temp=metadata_File.read().split("\n")
            metadata_File.close()
            package_Files=int(metadata_Temp[0])
            self.packages+=[Package(package_Name,metadata_Temp[1])]
            self.packages[count].version=int(metadata_Temp[2])
            package_Count=0
            while package_Count<package_Files:
                self.packages[count].add_File(metadata_Temp[package_Count+3])
                package_Count+=1
            count+=1
    def find_Package(self,name):
        count=0
        while count<self.cp:
            if name==self.packages[count].nomen:
                return count
            count+=1
        return self.cp
    def is_Package(self,name):
        if self.find_Package(name)==self.cp:
            return False
        return True
    def add_Package(self,name,location):
        if not self.is_Package(name):
            self.metadata+=[name]
            metadata_File=open(self.loc+name+".metadata","w+")
            metadata_File.write("0\n"+location+"\n0")
            self.packages+=[Package(name,location)]
            self.cp+=1
    def insert_File(self,package,name,location):
        if not self.is_Package(package):
            self.add_Package(package,location)
        self.packages[self.find_Package(package)].add_File(name)
        metadata_File=open(self.loc+package+".metadata")
        metadata_Temp=metadata_File.read().split("\n")
        metadata_File.close()
        metadata_Files=int(metadata_Temp[0])+1
        metadata_Temp[0]=str(metadata_Files)
        metadata_Temp+=[name]
        metadata_File=open(self.loc+package+".metadata","w")
        metadata_File.write("\n".join(metadata_Temp))
        metadata_File.close()
    def update_Package(self,name):
        index=self.find_Package(name)
        self.packages[index].clear_Files()
        temp_Loc=self.packages[index].loc
        metadata_File=open(temp_Loc+"package.metadata")
        metadata_Temp=metadata_File.read().split("\n")
        metadata_File.close()
        file_Amount=int(metadata_Temp[0])
        self.packages[index].version=int(metadata_Temp[1])
        file_Count=0
        while file_Count<file_Amount:
            self.insert_File(name,metadata_Temp[file_Count+2],temp_Loc)
            file_Count+=1
    def create_Package(self,name,location):
        self.add_Package(name,location)
        self.update_Package(name)
    def set_Up_Package(self,name,location):
        self.add_Package(name,location)
        metadata_File=open(location+"package.metadata","w+")
        metadata_File.write("0\n0")
        metadata_File.close()
    def reset_Package(self,name):
        location=self.packages[self.find_Package(name)].loc
        metadata_File=open(location+"package.metadata","w+")
    def use_Package(self,name,location,project=""):
        self.packages[self.find_Package(name)].copy_Files(location,project)
    def deactivate_Package(self,name,location,project=""):
        self.packages[self.find_Package(name)].deactivate_Files(location,project)
    def __del__(self):
        metadata=[str(self.cp)]
        count=0
        while count<self.cp:
            metadata+=[self.packages[count].nomen]
            count+=1
        metadata_File=open(self.loc+"karot.metadata","w+")
        metadata_File.write("\n".join(metadata))
        metadata_File.close()
        