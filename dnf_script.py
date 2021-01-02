import os 

# /////////////getting current dir//////////////////
class Main:
    def __init__(self,main_path):
        self.search_path = main_path
        self.current_dir = os.getcwd()
        self.saving_path = os.path.join(self.current_dir,"1_directory_structure")
        print(self.saving_path)
        if os.path.exists(self.saving_path):
            pass
        else:
            os.mkdir("1_directory_structure")   
    def info_saver(self,cpath,dirs,files):
        if cpath == self.current_dir:
            files = [fn + '\n' for fn in files]
            with open(os.path.join(self.saving_path,"current_directory_filelist.txt"),'w') as f:
                f.writelines(files)
            for dir_name in dirs:
                if "1_directory_structure" != dir_name:
                    os.mkdir(os.path.join(self.saving_path,dir_name))  
                    print(dirs)     
                    
    def dir_blueprint_creater(self):
        for path,dir,files in os.walk(os.getcwd()):
            self.info_saver(path,dir,files)
            


if __name__ == '__main__':
    obj = Main(os.getcwd())
    obj.dir_blueprint_creater()
        
# for i,j,k in os.walk(os.getcwd()):
#     print(i,j,k)              
        


