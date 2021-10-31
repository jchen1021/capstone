import dicom2nifti #Needs pip install
import os

patients_folder = os.listdir(path_to_all_patients) #Fill in path

for patient in patients_folder:
    dicom2nifty.convert_directory(os.path.join(path_to_all_patients, patient), os.path.join(path_to_save_folder, patient))
    
    #fill in path