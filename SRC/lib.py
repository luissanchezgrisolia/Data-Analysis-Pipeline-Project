import pandas as pd
import numpy as np
import os
import base64
#from sendgrid import SendGridAPIClient
#from sendgrid.helpers.mail import (
#    Mail, Attachment, FileContent, FileName,
#    FileType, Disposition, ContentId)
from dotenv import load_dotenv
load_dotenv()
import re
#from fpdf import FPDF
import requests
import matplotlib as mpl
import matplotlib.pyplot as plt


#Origin dataframe from which I am going to define some functions
df=pd.read_csv('../../CSV/nasdaq_final.csv',low_memory=False)  


#Returns a list with the name of the companies
def company_list(listcompany):                                  
    out=set(df.Name)
    print(out)


#For print by console
def company_info(company,date):                                             
    out= df[(df['Name'].str.lower()==company.lower())&(df['date']==date)]
    if date in set(df.date):            
        print(out)
    else:
        print("That date is not defined in DF, probably because it was weekend. Try with another different day. Anaway: ")
   

#For add in pdf
def company_info_pdf(company,date):                                             
    df2= df[(df['Name'].str.lower()==company.lower())&(df['date']==date)] 
    fig, ax = plt.subplots()
    fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')
    ax.table(cellText=df2.values, colLabels=df2.columns, loc='center')
    fig.tight_layout()
    plt.savefig("body.png", bbox_inches='tight')           
  


#Plot for print by console
def stats(company):                                                         
    dtp = df[df["Name"].str.lower()==company.lower()]
    dtp=dtp.groupby(dtp["date"]).agg({"open":"mean"}).plot.bar()
    plt.xlabel("From 2015 to now")
    plt.ylabel("Open price of the shares")
    plt.title("Evolution of the company share price")
    plt.show()

#Plot for add in pdf
def stats_pdf(company):                                                      
    dtp = df[df["Name"].str.lower()==company.lower()]
    dtp=dtp.groupby(dtp["date"]).agg({"open":"mean"}).plot.bar()
    plt.xlabel("From 2015 to now")
    plt.ylabel("Open price of the shares")
    plt.title("Evolution of the company share price")
    plt.savefig("evolucion.png", bbox_inches='tight')