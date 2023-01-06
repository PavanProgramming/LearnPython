import os

print(dir(os)) # returns all the attributes and methods for os
print(os.getcwd())

os.chdir('D:\workSpace\Python\gitHubRepos\YoutubeLearn\Learning_Python\Beginner')
print(os.getcwd())
print(os.listdir())  # lists the files and folders

# creating
os.mkdir('temp')
print(os.listdir())
# os.mkdir('temp1/temp1_a') # error because temp1 not exists
# print(os.listdir())
os.makedirs('temp1/temp1_a') # creates multi-level directories
print(os.listdir())

# removing
os.rmdir('temp')
print(os.listdir())
os.removedirs('temp1/temp1_a')
print(os.listdir())

# rename
print(os.listdir())
#os.mkdir('temp2')
#os.rename('temp2','temp3')
#print(os.listdir())
#os.rmdir('temp3')

#os.rename('tempa.txt','tempb.txt')

#file properties
print(os.stat('tempb.txt')) # provides multiple data related to that file
#size is most useul one
#st_mtime : last modification time
print(os.stat('tempb.txt').st_size)

from datetime import datetime

mod_time = os.stat('tempb.txt').st_mtime
print(datetime.fromtimestamp(mod_time))

# to get all the folders and files in a directory
for dirpath, dirnames, filenames in os.walk('D:\pavanfiles\LearningResources\e-books'):
    print('Current path:', dirpath)
    print('Directories', dirnames)
    print('Files:', filenames)
    print()

# to get environment variables
print(os.environ) # all environment variables
print()
print(os.environ.get('ALLUSERSPROFILE')) # specific environment variable

# os.path module to work with paths
# join will take care about backslash
print(dir(os.path))

file_path = os.path.join(os.environ.get('ALLUSERSPROFILE'),'test.txt')
print(file_path)
print(os.path.basename('D:\workSpace\Python\gitHubRepos\YoutubeLearn\Learning_Python\Beginner\08_Python-OSModule\main.py'))
print(os.path.dirname('D:\workSpace\Python\gitHubRepos\YoutubeLearn\Learning_Python\Beginner\08_Python-OSModule\main.py'))
print(os.path.split('D:\workSpace\Python\gitHubRepos\YoutubeLearn\Learning_Python\Beginner\08_Python-OSModule\main.py'))
print(os.path.exists('D:\workSpace\Python\gitHubRepos\YoutubeLearn\Learning_Python\Beginner\07_Python-Modules\main.py'))

print('\f')
print('\\f')
print(r'\f')

print(os.path.isdir(r'D:\workSpace\Python\gitHubRepos\YoutubeLearn\Learning_Python\Beginner\07_Python-Modules'))
print(os.path.isdir('D:\\workSpace\\Python\\gitHubRepos\\YoutubeLearn\\Learning_Python\\Beginner\\07_Python-Modules'))
print(os.path.isfile(r'D:\workSpace\Python\gitHubRepos\YoutubeLearn\Learning_Python\Beginner\07_Python-Modules\main.py'))
# to split file extension
print(os.path.splitext('D:\workSpace\Python\gitHubRepos\YoutubeLearn\Learning_Python\Beginner\07_Python-Modules\main.py'))






