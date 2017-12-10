

import gridfs
import os
from pymongo import MongoClient


def storedata(data_folder_path):
    
    dirs = os.listdir(data_folder_path)


    client = MongoClient('localhost', 27017)
    database = client['django_precog']
    fs = gridfs.GridFS(database)

    for dir_name in dirs:
        
       
        if not dir_name.startswith("s"):
            continue;
            
       


        
        subject_dir_path = data_folder_path + "/" + dir_name
        

        subject_images_names = os.listdir(subject_dir_path)

        
        for image_name in subject_images_names:
            

            if image_name.startswith("."):
                continue;
            
            
            image_path = subject_dir_path + "/" + image_name

            label = int(dir_name.replace("s", ""))
    	    
    	    datafile = open(image_path,"r");
    	    thedata = datafile.read()
 

     	    
    	    #connection = pymongo.Connection("localhost",27017);
    	    #database = connection['django_precog']
 


     

    	    stored = fs.put(thedata, filename=str(label)+"_"+image_name)


    	    outputdata =fs.get(stored).read() 
     
 
 

    	    outfilename = data_folder_path+"/mongo_data/"+str(label)+"_"+image_name
    	    output= open(outfilename,"w")
     
    	    output.write(outputdata)

    	    output.close()
 
 

    	    #fs.delete(stored)

    #connection.close()




	     	   

storedata(os.getcwd()+"/training-data")


