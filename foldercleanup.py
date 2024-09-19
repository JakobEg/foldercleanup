import os
import shutil

def rename_and_delete_folders(parent_folder):
    # Iterate through all items in the parent folder
    for folder_name in os.listdir(parent_folder):
        folder_path = os.path.join(parent_folder, folder_name)
        
        # Ensure it's a folder
        if os.path.isdir(folder_path):
            # Iterate through files in the folder
            for file_name in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file_name)
                
                # Ensure it's a file
                if os.path.isfile(file_path):
                    # Create new file path with the folder name
                    new_file_path = os.path.join(parent_folder, folder_name + os.path.splitext(file_name)[1])
                    os.rename(file_path, new_file_path)
                    print(f"Renamed '{file_name}' to '{folder_name + os.path.splitext(file_name)[1]}'")
            
            # Delete the folder after renaming files
            shutil.rmtree(folder_path)
            print(f"Deleted folder: {folder_name}")

# Set the path to the parent folder
parent_folder_path = "/Users/Jakob/VS_code_projects/kattis_test/Kattis"

# Run the function
rename_and_delete_folders(parent_folder_path)
