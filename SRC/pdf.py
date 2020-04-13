import pandas as pd
import numpy as np
import os
import base64
from dotenv import load_dotenv
load_dotenv()
import re
from fpdf import FPDF
import requests
from lib import (stats_pdf, company_info, company_info_pdf)
import matplotlib.pyplot as plt


def genPDF(company,date):
    try:
        pdf = FPDF('P','mm','A4') #210 x 297 mm vertical
        
        #Page
        pdf.add_page()

        #Nasdaq image superior
        pdf.image("nasdaq-logo.png",10,10, 65,20,link="https://logodownload.org/wp-content/uploads/2019/07/nasdaq-logo-4.png")

        # parameters
        w,h=190,277
        font_type = ('Arial', 'B', 15)
        pdf.set_font(*font_type)
        pdf.set_text_color(0)
        pdf.set_draw_color(0)

        # Title
        pdf.set_xy(8,50)
        pdf.cell(25,80)
        pdf.cell(150,10,f"Basic information about {company}´s share price",0,1,"C")  

        # Data
        pdf.set_fill_color(121, 181, 161)
        font_type = ('Arial', '', 12)
        pdf.set_font(*font_type)

        #Body
        company_info_pdf(company,date)
        
        #Adding body
        pdf.image("body.png",15,5, 180,180)


        #company plot
        stats_pdf(company)

        #Adding plot
        pdf.image("evolucion.png",30,140, 140,95)


        #Output
        pdf.output("Nasdaq-PDF.pdf","F")
    except IndexError:
        print("Ooops!! Something went wrong, it seems that date is not defined in DF, probably because it was weekend. Try with another different day.")

   