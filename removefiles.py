import os
import shutil
import time

def main():
	deletedfolderscount = 0
	deletedfilescount = 0
	path = "/delete_path"
	days = 30
	seconds = time.time() - (days*24*60*60)

	if os.path.exists(path):



        for root_folder, folders, files in os.walk(path):


			if seconds >= getdate(root_folder):
				remove_folder(root_folder)
				deletedfolderscount += 1 
				break

			else:

				for folder in folders:
					folder_path = os.path.join(root_folder, folder)
					if seconds >= getage(folder_path):
						remove_folder(folder_path)
						deletedfolderscount += 1 


				for file in files:
					file_path = os.path.join(root_folder, file)
					if seconds >= getage(file_path):
						remove_file(file_path)
						deletedfilescount += 1 

		else:
			if seconds >= getage(path):
				remove_file(path)
				deletedfilescount += 1 

	else:
		print(f'"{path}" is not found')
		deletedfilescount += 1 
	print(f"Number of foleders deleted: {deletedfolderscount}")
	print(f"Number of files deleted: {deletedfilescount}")


def remove_folder(path):
	if not shutil.rmtree(path):
		print(f"{path} is deleted successfully")
	else:
		print(f"Sorry. Unable to to delete the "+path)



def remove_file(path):
	if not os.remove(path):
		print(f"{path} is removed successfully")
	else:
		print("Unable to delete the "+path)


def getage(path):
	ctime = os.stat(path).st_ctime
	return ctime

if __name__ == '__main__':
	main()