import os 
# /////////////getting current dir//////////////////
class Main:
    def __init__(self,main_path):
        self.search_path = main_path         #the path we have to clone
                                             #from where we are running this file that dir path
        self.saving_path = os.path.join(main_path,"1_directory_structure")
    
        if os.path.exists(self.saving_path):
            pass
        else:
            os.mkdir("1_directory_structure")

    def dir_blueprint_creater(self): 
        for path,dirs,files in os.walk(self.search_path): #os.walk will iterate 
            try:
                if  "dnf_script.py" in files and "1_directory_structure" in dirs: #just ignoring our original script and folder 
                    files.remove("dnf_script.py")
                    dirs.remove("1_directory_structure")
                path = path.partition(self.search_path)[-1].lstrip('\\')
                if path:
                    os.mkdir(os.path.join(self.saving_path,path))
                if(files):
                    # files = [fn + '\n' for fn in files]
                    with open(os.path.join(self.saving_path,path,"1_directory_filelist.txt"),'w') as f:
                        for file in files:
                            fi = str(file.encode("utf-8"))+"\n"
                            f.write(fi.strip('b'))
                                   
            except FileExistsError:
               pass
            
            
          
            


if __name__ == '__main__':
    obj = Main(os.getcwd())
    obj.dir_blueprint_creater()
