import os
import sys
import datetime


def check_dir_path_exists(dirname):
    flag=os.path.exists(dirname)
    if flag==False:
         return("The path dosent exist\n")
         

def check_abs_path_exists(path):
     flag=os.path.isabs(path)
     if flag==False:
        return("The Path is Not Complet \n")
    
def convert_to_abs_path(path):

    path=os.path.abspath(path)
    return(f"The Complet path of the directory is \n{path}\n")

def check_path_is_directroy(path):
    flag = os.path.isdir(path)
    if  flag==False:
        return("Path is correct but it is not a directory \n")
        
def creat_new_file():
    filename=datetime.datetime.now().strftime("%D-%H-%M")+".txt"
    return filename


