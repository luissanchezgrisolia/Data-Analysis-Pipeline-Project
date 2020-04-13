# Data-Analysis-Pipeline-Project
2nd project for bootcamp IronHack

**_Developing of a program which shows a brief analysis about the share prices of NASDAQ-100 companies_**

#![](giphy.gif)

### RESUME📈💰

I have develop a basic program which you can run from the bash-terminal and it returns a brief analysis of the share price in a specific date of a company you choose.

You have two options:
  -1st: work through the bash terminal and the program will be showing you some options where you have to take a decision        before printing you the analysis.
  
  -2nd: work through the bash terminal as well but, if you choose that option, the program will generate a PDF with the   report. You have an example in the SRC folder.
 
PS:*You can go directly to HOW IT WORKS example in order to start having fun.

### WORK PROCESS 💻 

In "Input" folder you will find the initial CSV from which I have worked.
I have clean them using Python 3 and modules pandas, numpy and matplotlib; always keeping in mind what my objective was to analyze with my program.

After that, I wrote the code that makes this possible and which you can find in the SRC folder. I used Python use as programming language and visual studio code.

### HOW IT WORKS(EXAMPLE)🎮  

-Go open your terminal and make sure you have Python. 
-Write the name of the file in which is the code and run "-h" to see all the options:
`
python3 main.py -h
usage: main.py [-h] [-l LISTCOMPANY] [-c COMPANY] [-d DATE]

Basic analysis of Nasdaq-100 companies share prices

optional arguments:
  -h, --help      show this help message and exit
  -l LISTCOMPANY  Write 'listcompany' to show a list with the Nasdaq-100
                  companies name you can choose from
  -c COMPANY      Name of the company you would like to analyze
  -d DATE         Date as YYYY-MM-DD you would like to analyze
`
-If you type "-l listcompany" a list with all the availables companies will be shown 
-Once you decided the company and the date, type them as -c and -d and it will all start. For example:

`python3 main.py -c "Facebook Inc." -d "2019-05-05"`

-Everything that comes later, is super intuitive.




Hope you like it.

LSG
