
INSTRUCTIONS TO RUN BOOKLEASE IN WINDOWS and MacOS:

•	Install python 3.5.2. Make sure python is in the path.

•	Install python package manager using the below command in windows: 
            >> C:\Users\arnika> python -m pip install -U pip
            
   For MacOS - Install python package manager using the below command in windows.
   Step -1  curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
   Step -2  python get-pip.py


          
•	Install Python Virtual Environment in Windows
            >> C:\Users\arnika>pip install virtualenv
    For MacOS tyep this command - $ pip install --user virtualenv
            
            
•	After extracting the files from the zip file, ‘booklease_i3’ folder will be created as shown below

•	Go to the directory ‘booklease_i3’ in the command prompt as shown below
            >> C:/Temp/booklease_i3
     
•	Now run the below command:
            >> C:\Temp\booklease_i3>virtualenv env_mysite
            
•	In the command prompt go to “booklease_i3\env_mysite\Scripts” directory by using the below command
            >> cd booklease_i3\env_mysite\Scripts
            
•	Now run the below command in the command prompt for windows.
            >> activate
            
   For MacOS run this command to activate virtualenv - $ source bin/activate
            
•	Now change the directory to “booklease_i3\env_mysite\mysite” in command prompt.

•	Run the below command  : 
            >> python manage.py runserver
            This will be run the local server on port 8000
            
 •	Now open the browser on the local machine and type the below URL :  http://127.0.0.1:8000/booklease
 
 •	Once the sign in page shows up you can enter the log in credentials to sign in which we have already created i.e.       Username: arnika   Password: puru12345 or you can sign up by clicking the signup button to create your own account.








    
