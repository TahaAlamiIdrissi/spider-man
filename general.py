import os

#each website you crawl is a separate project(folder)
#new folder = new project

def create_project_dir(directory):
    #if the folder (project)does not  already exist
    
    if not os.path.exists(directory):
        print("Creating project "+directory)
        os.makedirs(directory)
        
create_project_dir("talassi")