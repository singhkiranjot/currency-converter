from tkinter import *
from tkinter import ttk
root = Tk() 

root.title("Currency Converter")
root.config(background="blue")
root.geometry("500x530")



def CurrencyExchangeApi( init_from, init_to , init_amount) : 
	import requests

	
	base_url = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"

	main_url = base_url + "&from_currency=" + init_from +"&to_currency=" + init_to + "&apikey=" + "3N2FR1BAZHKT3FUI" 

	req_ob = requests.get(main_url) 

	result = req_ob.json() 
      
	return (
        float(result["Realtime Currency Exchange Rate"]['5. Exchange Rate']) * init_amount , init_to
    )




label = Label(root,text="Currency Converter" , font=("Arial",15,"bold"))
label.place(x=50,y=50,height=50 ,width=400)



currencies = ["AUD", "CAD", "CZK", "DKK", "EUR", "INR", "PKR", "USD"]

label2 = Label(root,text="From Currency" , font=("Arial",12,"bold"))
label2.place(x=35,y=130,height=50 ,width=150)
combo = ttk.Combobox(root , text="From currency" , font=("Arial" , 12 , "bold"),values=currencies )
combo.place(x=215,y=130 , height=50 , width=250)



label3 = Label(root,text="To Currency" , font=("Arial",12,"bold"))
label3.place(x=35,y=210,height=50 ,width=150)
combo2 = ttk.Combobox(root , text="to currency" , font=("Arial" , 12 , "bold"),values=currencies)
combo2.place(x=215,y=210 , height=50 , width=250)



label4 = Label(root,text="Amount" , font=("Arial",12,"bold"))
label4.place(x=35,y=290,height=50 ,width=150)
amount= Entry(root,font=("Arial" , 12 , "bold") )
amount.place(x=215,y=290 , height=50 , width=250)



label5 = Label(root,text="Converted Amount" , font=("Arial",11,"bold"))
label5.place(x=35,y=450,height=50 ,width=150)
label6 = Label(root,text="" , font=("Arial",11,"bold"))
label6.place(x=215,y=450 , height=50 , width=250)


def retrieve():
    from_currency = combo.get()
    to_currency = combo2.get()
    inputAmount = int(amount.get())
    totalAmount =CurrencyExchangeApi(from_currency , to_currency , inputAmount)
    label6.config(text=totalAmount)
    



button = ttk.Button(root, text="Convert" , command=retrieve)
button.place(x=150 , y=370 ,height=50 , width=200)

root.mainloop()


