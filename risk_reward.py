from  tkinter import *

from sqlalchemy import column


main_window=Tk()
main_window.title('Risk Reward Calculator')
main_window.geometry('420x250')

Label(main_window,text='').grid(row=0, column=1)

Label(main_window,text='Risk Ratio').grid(row=5, column=1)
Label(main_window,text='Reward Ratio').grid(row=7, column=1)
Label(main_window,text='Buy Price').grid(row=9, column=1)

Label(main_window,text='Target Price').grid(row=30, column=1)
Label(main_window,text='Stop Loss').grid(row=32, column=1)





def calculate():

      target.delete(0,END)
      stp_loss.delete(0,END)
      
      risk_ratio =float(risk.get())
      reward_ratio =float(reward.get())
      stock_buy_price=float(buy_price.get())

      Target_price = ((stock_buy_price/100)*reward_ratio)+stock_buy_price
      stop_loss = stock_buy_price-((stock_buy_price/100)*risk_ratio)

      target.insert(0,str(Target_price))
      stp_loss.insert(0,str(stop_loss))


      


risk = Entry(main_window, width=50, borderwidth=5)
risk.grid(row=5, column=5)


reward = Entry(main_window, width=50, borderwidth=5)
reward.grid(row=7, column=5)

buy_price = Entry(main_window, width=50, borderwidth=5)
buy_price.grid(row=9, column=5)

target= Entry(main_window, width=50, borderwidth=5)
target.grid(row=30, column=5)

stp_loss= Entry(main_window, width=50, borderwidth=5)
stp_loss.grid(row=32, column=5)
  

Button(main_window, text='calculate', command = calculate).grid(row=15, column=5, padx=10, pady=10)



main_window.mainloop()




