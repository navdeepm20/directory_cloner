import os 
# /////////////getting current dir//////////////////
class Main:
    def __init__(self,main_path):
        self.search_path = main_path         #the path we have to clone
                                             #from where we are running this file that dir path
        self.saving_path = os.path.join(self.current_dir,"1_directory_structure")
    
        if os.path.exists(self.saving_path):
            pass
        else:
            os.mkdir("1_directory_structure")

    def dir_blueprint_creater(self): 
        for path,dirs,files in os.walk(self.search_path):
            # if path == self.search_path:       #will check if the current iterative path and the search path is same. (basically the root of your search dir)
            #     files = [fn + '\n' for fn in files]
            #     if(files):
            #         files = [fn + '\n' for fn in files]
            #         with open(os.path.join(self.saving_path,"1_directory_filelist.txt"),'w') as f:
            #             f.writelines(files)
            #     for dir_name in dirs:
            #         if "1_directory_structure" != dir_name:
            #             try:
            #                 os.mkdir(os.path.join(self.saving_path,dir_name))  
            #             except FileExistsError:
            #                 pass
            # else:
            path = path.partition(self.search_path)[-1].lstrip('\\')
            try:
                print(path) 
                os.mkdir(os.path.join(self.saving_path,path))
                
                if(files):
                    files = [fn + '\n' for fn in files]
                    with open(os.path.join(self.saving_path,path,"1_directory_filelist.txt"),'w') as f:
                        f.writelines(files)
                        
            except FileExistsError:
                print(path,files)
                pass    
            
            
          
            


if __name__ == '__main__':
    obj = Main(os.getcwd())
    obj.dir_blueprint_creater()
