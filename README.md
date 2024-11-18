How to Containerize the Python Application. 
1. Make sure Docker Desktop is opened 
2. In your terminal, run ```docker build -t my-app .```
3. Then run ```docker run -p 5000:5000 my-app```
4. Open your address to access it! 

Troubleshooting/Notes: 
- Make sure you have python downloaded to run this 
- When pushing to GitHub, ensure that ```.env``` is present in the .gitignore file
