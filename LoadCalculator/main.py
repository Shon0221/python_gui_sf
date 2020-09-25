# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tkinter import *

class LoanCalculator:

    def __init__(self):
        window = Tk()
        window.title('Calculator')
        window.configure(bg="light green")

        Label(window, font='Helvetica 12 bold', bg='light green', text='Annual Interest Rate').grid(row=1, column=1, sticky=W)
        Label(window, font='Helvetica 12 bold', bg='light green', text='Number of Years').grid(row=2, column=1, sticky=W)
        Label(window, font='Helvetica 12 bold', bg='light green', text='Loan Amount').grid(row=3, column=1, sticky=W)
        Label(window, font='Helvetica 12 bold', bg='light green', text='Monthly Payment').grid(row=4, column=1, sticky=W)
        Label(window, font='Helvetica 12 bold', bg='light green', text='Total Payment').grid(row=5, column=1, sticky=W)

        self.annualInterestRateVar = StringVar()
        Entry(window, textvariable=self.annualInterestRateVar, justify=RIGHT).grid(row=1, column=2)
        self.numOfYearVar = StringVar()
        Entry(window, textvariable=self.numOfYearVar, justify=RIGHT).grid(row=2, column=2)
        self.loanAmountVar = StringVar()
        Entry(window, textvariable=self.loanAmountVar, justify=RIGHT).grid(row=3, column=2)
        self.monthlyPaymentVar = StringVar()
        lblMonthlyPayment = Label(window, font='Helvetica 12 bold', bg='light green', textvariable=self.monthlyPaymentVar).grid(row=4, column=2, sticky=E)
        self.totalPaymentVar = StringVar()
        lblTotalPayment = Label(window, font='Helvetica 12 bold', bg='light green', textvariable=self.totalPaymentVar).grid(row=5, column=2, sticky=E)

        btComputePayment = Button(window, text='Compute Payment', bg='red', fg='white', font='Helvetica 14 bold', command=self.computePayment).grid(row=6, column=2, sticky=E)
        btClear = Button(window, text='Compute Payment', bg='blue', fg='white', font='Helvetica 14 bold', command=self.delAll).grid(row=6, column=8, padx=20, pady=20, sticky=E)

        window.mainloop()

    def computePayment(self):
        monthlyPayment = self.getMonthlyPayment(
            float(self.loanAmountVar.get()),
            float(self.annualInterestRateVar.get()) / 1200,
            int(self.numOfYearVar.get())
        )
        self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f'))

        totalPayment = float(self.monthlyPaymentVar.get()) * 12 * int(self.numOfYearVar.get())

        self.totalPaymentVar.set(format(totalPayment, '10.2f'))

    def getMonthlyPayment(self, loadAnou, monthlyInterestRate, numOfYears):
        return loadAnou * monthlyInterestRate / (1 - 1 / (1 + monthlyInterestRate) ** (numOfYears * 12))

    def delAll(self):
        self.monthlyPaymentVar.set('')
        self.loanAmountVar.set('')
        self.annualInterestRateVar.set('')
        self.numOfYearVar.set('')
        self.totalPaymentVar.set('')


def main():
    # Use a breakpoint in the code line below to debug your script.
    LoanCalculator()  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
