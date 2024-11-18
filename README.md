How to Containerize the Python Application. 
1. Make sure Docker Desktop is opened 
2. In your terminal, run ```docker build -t my-app .```
3. Then run ```docker run -p 5000:5000 my-app```
4. Open your address to access it! 

Troubleshooting/Notes: 
- Make sure you have python downloaded to run this 
- When pushing to GitHub, ensure that ```.env``` is present in the .gitignore file

Developer Instructions

Follow the below steps to develop the application on your local machine. The steps below that you have Python 3.12 and VSCode installed.

1. Open the VSCode command palette (View > Command Palette or (```Ctrl+Shift+P```))

2. Select *Python: Create Environment* from the Palette's dropdown menu.

3. Run *Terminal: Create New Terminal (```Ctrl+Shift+ ```)*. This will automatically activate the virtual environment you just created.

4. Type ```pip install requirements.txt``` to install the necessary dependencies into your virtual environment. Flask is one of the dependencies.
