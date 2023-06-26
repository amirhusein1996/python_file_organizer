import glob
import os

class Organize:
    def __init__(self):
        self.pictures=['apng','avif','gif','tif','tiff','jpg','jpeg','jfif','pjpeg','pjp','jpe','png'
                ,'svg','webp','bmp','dib','hiec','hif' ]

        self.videos=['yuv','wmv','webm','vob','viv','svi','roq','rmvb','rm','ogv','ogg','nsv','mxf'
                ,'mts','m2ts','ts','mpg','mpeg','m2v','mpg','mp2','mpeg','mpe','mpv','mp4','m4p'
                ,'m4v','mov','qt','mng','mkv','m4v','gifv','flv','f4v','f4p','f4a','f4b','drc','avi'
                ,'asf','amv','3gp','3g2']

        self.musics=['mp3' ,'wav' ,'wma' ,'mpa' ,'ram' ,'ra' ,'aac' ,'aif' ,'m4a' ,'tsa']

        self.documents=['doc','pdf', 'ppt', 'pps', 'docx', 'pptx']

        self.programs=['exe', 'msi' ,'apk' ,'ipa', 'dmg', 'pkg']

        self.compressed=['zip' ,'rar', 'r0*', 'r1*' ,'arj', 'gz' ,'sit', 'sitx', 'sea', 'ace', 'bz2', '7z']


        self.all_files=glob.glob('*') #get name of all files
        self.all_files.remove(os.path.basename(__file__))
    def __create_folders(self):
        
        # for file_type in file_name: 
        file_extentions={ext.lower().split('.')[-1] for ext in self.all_files if os.path.isfile(ext)}
        # create new folders by file type:
        for ext in file_extentions:
            if ext in self.pictures and not os.path.exists('Pictures'):
                    os.makedirs('Pictures')
                    
            elif ext in self.videos and not os.path.exists('Videos'):
                    os.makedirs('Videos')
                    
            elif ext in self.documents and not os.path.exists('Documents'):
                    os.makedirs('Documents')
                    
            elif ext in self.compressed and not os.path.exists('Compressed'):
                    os.makedirs('Compressed')
                    
            elif ext in self.musics and not os.path.exists('Musics'):
                    os.makedirs('Musics')
                    
            elif ext in self.programs and not os.path.exists('Programs'):
                    os.makedirs('Programs')
            elif not os.path.exists('General'):
                    os.makedirs('General')

    def __move(self):
        all_files=self.all_files
        
        for file in all_files:
            try:
                ext=file.lower().split('.')[-1]
                if os.path.isfile(file):    
                    if  ext in self.pictures:
                        os.rename(file,f'Pictures/{file}')
                        
                    elif ext in self.videos:
                        os.rename(file,f'Videos/{file}')
                        
                    elif ext in self.documents:
                        os.rename(file,f'Documents/{file}')
                    
                    elif ext in self.compressed:
                        os.rename(file,f'Compressed/{file}')
                    
                    elif ext in self.musics:
                        os.rename(file,f'Musics/{file}')
                    
                    elif ext in self.programs:
                        os.rename(file,f'Programs/{file}')
                    else:
                        os.rename(file,f'General/{file}')                
            except:
                continue

    def __delete_empty_folders(self):
        all_files=self.all_files
        for file in all_files:
            try:
                if os.path.isdir(file):
                    os.rmdir(file)
            except:
                continue
    
    def move(self):
        self.__create_folders()
        self.__move()
    
    def delete_empty_folders(self):
        self.__delete_empty_folders()

    def count_folders(self):
        return len([folder for folder in self.all_files if os.path.isdir(folder)])
    
    def count_files(self):
        return len([file for file in self.all_files if os.path.isfile(file)])
    
