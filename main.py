from argparse import ArgumentParser
import datetime
from lib import (company_info, stats, company_list)
import matplotlib.pyplot as plt
#from mail import (mail)
from pdf import (genPDF)

def parse():
    parser = ArgumentParser(description="Basic analysis of Nasdaq-100 companies share prices")
    parser.add_argument("-l",dest='listcompany', help="Write 'listcompany' to show a list with the Nasdaq-100 companies name you can choose from")
    parser.add_argument("-c",dest='company', help="Name of the company you would like to analyze")
    parser.add_argument("-d", dest='date', help="Date as YYYY-MM-DD you would like to analyze")
    return parser.parse_args()

def main():
    args = parse()
    company=args.company
    date=args.date
    listcompany = args.listcompany
    
    if args.listcompany:
        company_list(listcompany)
    else:
        if not(args.date):
            print("You must define a date")
        elif not(args.company):
            print("You must define a company")
        else:
            qst=str(input(f"Would you like to run the program by console(C) or create a PDF(P)? (C/P): "))
            while qst not in (["C","P"]):
                print("You must answer with C if console or P if PDF")
                qst=str(input(f"Would you like to run the program by console(C) or create a PDF(P)? (C/P): "))
            if qst=="P":
                print(f"Cool, generating PDF. See next time!")
                genPDF(company,date)
            elif qst=="C":
                print(f"Cool! Here you have the share prices info about {company} from {date}")
                company_info(company,date)
                answer=str(input(f"Would you like to have a plot about last 5 years prices evolution for {company} (Y/N): "))
                while answer not in (["Y","N"]):
                    print("You must answer with Y if yes or N if no")
                    answer=str(input(f"Would you like to have a plot about last 5 years prices evolution for {company} (Y/N): "))
                if answer=="Y":
                    print(f"So this the last 5 years prices evolution for {company}")
                    stats(company)
                elif answer=="N":
                    print("Ok. See you next time!")  

            
                    
       
    

    
    

    
if __name__ == '__main__':
    main()
    
    #parser = ArgumentParser(description="Basic analysis of Nasdaq-100 companies share prices")
    #parser.add_argument("-c",dest='company', help="Name of the company you would like to analyze")
    #parser.add_argument("-d", dest='date', type=datetime.datetime.fromisoformat, help="Date as YYYY-MM-DD you would like to analyze")
    #parser.add_argument("-e","--email", help="Email address where you would like to receive the report")
    #parser.add_argument("-s","--stats", help="Historical company stats")
    #args = parser.parse_args()
    #company_info(args.company,args.date)
    #if not(args.company and args.date):
    #    print("You must define a company and a date")
    #else:
    #    if not args.email:
    #        print(f"This is the share prices info about {args.company} from {args.date}")
    #        company_info(args.company, args.date)
    #        print("And this the last 5 years prices evolution for {args.company}")
    #        stats(args.company)
        #else: #Crearpdf