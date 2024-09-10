New! Keyboard shortcuts … Drive keyboard shortcuts have been updated to give you first-letters navigation
print("Hi!! Welcome to ABC Bank!")
print("I am  your digital assistant!!. Select your query directly  from the list of topics below")
def cont():
  while True:
    user_input= input("Do you want to continue?(yes or no)")
    if (user_input=="yes"):
            main_menu()
            continue     
    elif (user_input=="no"):
            thank()
            break

    elif user_input!="yes" or user_input!="no":
            print("Invalid input.Try again")
            cont()
    
def thank():
    print("")
    print("Thank you for contacting us .")
    print("Feel free to reach out anytime you have queries.")
    print("Have a wonderful day!!")
    print("For more information visit our website abc.com or contact us at toll free number 1800*******")
def main_menu():
 print("The Main Menu is as follows:")
 list_issues=[" 1. ATM card"," 2.NRI"," 3.Open Saving Account", "4.Loan"]
 print(*list_issues,sep="\n")
 choice=int(input("\nEnter your choice "))
 if choice==1:
    def ATM():
       print(" The Information about ATM Card is as follows :")
       atm_issues=["1.Documents required","2.Processing fees","3.Block Card","4.Benefits"]
       print(*atm_issues,sep="\n")
       choice1=int(input("Enter your choice"))
       if choice1==1:
           print("Documents required for ATM Card are as follows:")
           print("1.One ID proof and one Address Proof (PAN , Aadhaar, Driving License etc.) ...")
           print("2.SBI ATM card application form.")
           print("3.Minimum balance in SBI Account for applying for ATM Card.")
           print("4.Account details: Account holder Name, Account Number, DOB, etc.")
           print("5.Registered Mobile Number.")
       elif choice1==2:
             print("Processing fees for ATM Card is")
             print("Gold Debit Card:	₹100/- + plus GST")
             print("Platinum Debit Card:	₹300/- + plus GST")
             print("Clasic/Silver/Global Contactless Debit:NIL")
       elif choice1==3:
             print("In case you need to block your Card, Please contact this toll free number 1800*******.")
       elif choice1==4:
             print("You can use your Debit Card to withdraw Cash and you can also use at PoS/Online for purchases/payments.")
       elif choice1!=1 or choice1!=2 or choice1!=3 or choice1!=4:
            main_menu() 
    ATM()  
    
 elif choice==3:
  def saveacc():
     print(" The Information about Savings account  is as follows :")
     Savings_Account=["1.Eligibility","2.Limit","3.Balance","4. Interest"]
     print(*Savings_Account,sep="\n")
     choice3=int(input("enter your choice "))
     if choice3==1:
         print("1.To be eligible, the person must be at least 18 years old.")
         print("2.If an account is to be opened for a child, their parents or legal guardians can open the account on their behalf.")
         print("3.A legitimate identity and address proof that the government has approved is required of the applicant.")
         print("4.Following bank approval, the applicant must make an initial deposit, which will be determined by the minimum balance requirement of the savings account they have chosen.")
     elif choice3==2:
         print("In addition to the money limit levied on UPI transactions, NPCI has also set a limit on the number of transactions per day. ")
         print("The new regulations state that per day a person is allowed up to 20 transactions post which they are required to wait for 24 hours to renew")
     elif choice3==3:
         print("Minimum balance for urban and metro area: Rs 10,000")
         print("Minimum balance for semi urban/rural area :Rs 5,000")
     elif choice3==4:
         print("Saving Deposits Balance up to Rs.10 crore, Interest Rate 2.70% p.a.")
         print("Saving Deposits Balance above Rs.10 crore and above, Interest Rate 3.00% p.a.")
     elif choice3!=1 or choice3!=2 or choice3!=3 or choice3!=4:
         main_menu()
  saveacc()       
 elif choice==2:
  def nri():
     print(" The Information about NRI Account is as follows :")
     NRI=["1.Eligibility","2.Inward Remittances","3.NRE account & NRO account","4.Basic Limit"]
     print(*NRI,sep="\n")
     choice2=int(input("Enter your choice "))
     if choice2==1:
         print("1.To be eligible, the person must be at least 18 years old")
         print("2.An Indian citizen residing outside India for the purpose of: Employment, studies, business or vocation.")
         print("3.Individual posted in UN organisation or official deputed abroad by Government of India or public sector undertakings.")
         print("4.Indian nationals who may be Mariners or working on oil rigs or foreign registered airlines.")
     elif choice2==2:
         print("One of the primary benefits of the NRI account is that NRIs can repatriate their income to their dependents in India.")
     elif choice2==3:
         print("An NRE account is a bank account opened in India in the name of an NRI, to park his foreign earnings")
         print("NRO account is a bank account opened in India in the name of an NRI, to manage the income earned by him in India.")
     elif choice2==4:
         print("As a Non-resident, you still get the benefit of the basic exemption limit of Rs. 2,50,000 from your total income. ")
     elif choice2!=1 or choice2!=2 or choice2!=3 or choice2!=4:
        main_menu()
  nri()      
 elif choice==4:
  def loan():
     print(" The Information about Loan is as follows :")
     LOAN=["1.Home loan","2. Gold Loan","3.Education Loan","4.Personal Loan"]
     print(*LOAN,sep="\n")
     choice4= int(input("Enter your Choice "))
     if choice4==1:
         def home():
          print("For Home Loan choose from the options given below")
          Home_loan=["1.Eligibility","2.Borrowing Limits","3.Margin","4.Documents Required"]
          print(*Home_loan,sep="\n")
          choiceH=int(input("Enter your Choice "))
          if choiceH==1:
              print("The following individuals above the age of 21 years are eligible to apply for Axis Bank Home Loans:Salaried individuals, Professionals, Self-employed")
          elif choiceH==2:
              print("Home Loan Borrowing Limits Minimum - Rs. 3 lakhs")
          elif choiceH==3:
              print("Margin for home loan is :")
              print("For home loan upto Rs. 30 Lakhs - 10%")
              print("For home loan above Rs. 30 Lakhs upto Rs. 75 Lakhs - 20%")
              print("For loan above Rs. 75 Lakhs - 25%")
          elif choiceH==4:
              print("Documents required for home loan are:")
              print("1.Completely filled and duly signed application form along with all applicants latest passport size photo")
              print("2.Aadhar card is mandatory for Credit Linked Subsidy Scheme (PMAY) applicants")
              print("3.PAN card is mandatory for all financial applicants")
              print("4.Processing Fee and CERSAI cheques")
              print("5.Self-attestation of borrowers on all documents submitted")
          elif choiceH!=1 or choiceH!=2 or choiceH!=3 or choiceH!=4:
              loan()
              
         home()     
     elif choice4==2:
           print("The conditions to apply for gold loan are as follows:")
           print("1.Any Indian citizen be it salaried, self employed, trader, farmer, businessman can apply for gold loan.")
           print("2.You must be between 21-70 years of age anf have gold jewellery of 18-22 carat")
           print("3.Minimum Loan Amount : Rs 20,000 /-")
           print("4.Maximum Loan Amount : Rs 50.00 lacs")
           print("5.Mean Rate of Interest: 9.15%")
     elif choice4==3:
          def edu():
           print("For Education  Loan choose from the options given below")
           Edu_loan=["1.Repayment","2.Processing charges","3.Security","4.Margin"]
           print(*Edu_loan,sep="\n")
           choiceE=int(input("Enter your choice"))
           if choiceE ==1:

              print("Repayment period of upto 15 years after Course Period + 12 months of repayment holiday")
           elif choiceE==2:
             print("Loans upto Rs. 20 lacs : NIL")
             print("Loans above Rs. 20 lacs: Rs. 10,000 (plus taxes)")
           elif choiceE==3:
              print("Upto Rs. 7.5 Lacs:Only Parent/ Guardian as co-borrower. No Collateral Security or third party guarantee")
              print("Above Rs. 7.5 Lacs:Parent/ Guardian as co-borrower and tangible collateral security")
           elif choiceE==4:
              print("Up to Rs 4 Lacs - Nil")
              print("Above Rs 4 Lacs - 5% for studies in India, 15% for studies in abroad")
           elif choiceE!=1 or choiceE!=2 or choiceE!=3 or choiceE!=4:
               loan()
          edu()
     elif choice4==4:
         print("The conditions to apply for personal loan are as follows:")
         print("1.Apply, by sharing your basic personal and financial details for an eligibility check")
         print("2.Get your Personal Offer, by providing/authenticating bank statement and getting your email id verified")
         print("3.Online disbursal, by e-signing the loan agreement and setting up auto-repayment mode")
         print("4.You can also apply for a personal loan of up to Rs. 40 lakhs with few additional steps and documentation at low interest rates and with flexible repayment options.")
     elif choice4!=1 or choice4!=2 or choice4!=3 or choice4!=4:
            main_menu() 
  loan()          
 elif choice!=1 or choice!=2 or choice!=3 or choice!=4 :
    main_menu()
main_menu()   
cont()   
