#This part of my final project displays how many money your monthly savings will generate 
#in 3, 6, 9 and 12 months if you save up "x" count of money per month and how many percentage
# you would like to frozen, your money has 6.5% interest to annual grow buy if you frozen this increase to 13% annual
from pydoc import text
import tkinter as tk
from tkinter import Frame, Label, Button
from unittest import result 


def main():
    root=tk.Tk()
    root.option_add("*Font", "Helvetica 14")
    frm_main=Frame(root)
    frm_main.master.title("Monthly Savings Calculator")
    frm_main.pack(padx=10,pady=10,fill=tk.BOTH,expand=True)
    setup_main(frm_main)
    frm_main.mainloop()


def setup_main(frm):
    lbl_saving=Label(frm,text="Monthly saving amount: ")
    lbl_saving.grid(row=0,column=0, padx=5,pady=5)
    ent_saving=tk.Entry(frm, width=15)
    ent_saving.grid(row=0, column=1)

    lbl_frozen=Label(frm,text="Frozen percentage: ")
    lbl_frozen.grid(row=1,column=0, padx=5,pady=5)
    ent_frozen=tk.Entry(frm, width=15)
    ent_frozen.grid(row=1, column=1,)

    lbl_result=Label(frm,text="" ,justify="left")
    lbl_result.grid(row=3, column=0, columnspan=2, pady=10)

    def calculate_action():
        try:
            monthly_saving=float(ent_saving.get())
            frozen = float(ent_frozen.get())
        except ValueError:
            lbl_result.config(text="Please enter a valid numbers")
            return 
        except ValueError:
            lbl_result.config(text="Please enter a valid number for frozen percentage.")
            return 
        
        result_text=display_results(monthly_saving,frozen)
        lbl_result.config(text=result_text)
        
    Button(frm, text="Calculate", command=calculate_action).grid(row=2, column=0, columnspan=2, pady=2)


def calculate_monthly_savings(monthly_saving,annual_rate_normal,annual_rate_frozen,months,frozen_percentage):
    """Calculates savings with interest. monthly contributions, 
        without subtracting tax"""
    
    monthly_rate_normal=annual_rate_normal/12
    monthly_rate_frozen=annual_rate_frozen/12
    
    total_contributed=monthly_saving*months
    interest_normal=0
    interest_frozen=0
    
    for month in range(months):
        months_remaining=months-month

        frozen_amount=monthly_saving*(frozen_percentage/100)
        normal_amount=monthly_saving - frozen_amount

        interest_normal+=normal_amount*((1+monthly_rate_normal)**months_remaining-1)
        interest_frozen+=frozen_amount*((1+monthly_rate_frozen)**months_remaining-1)
    
    total_interest=interest_normal+interest_frozen
    total_final=total_contributed+total_interest

    return {
        "subtotal": round(total_contributed, 2),
        "interest_normal": round(interest_normal, 2),
        "interest_frozen": round(interest_frozen, 2),
        "total_interest": round(total_interest, 2),
        "total_final": round(total_final, 2)
    }


def display_results(monthly_saving,frozen_percentage):
    normal_rate=0.065 #6.5% annual
    frozen_rate=0.13 #13% annual
    periods=[3,6,9,12]
    text=""
    for months in periods:

        total=calculate_monthly_savings(monthly_saving, normal_rate, frozen_rate, months, frozen_percentage)
        text += f"{months} months: ${total['total_final']:.2f}\n"
   

    print(text)
    return text

if __name__ == "__main__":
        main()

