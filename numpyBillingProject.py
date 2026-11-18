import numpy as np
import datetime
name=[]
prices=[]
quantitys=[]
while True:
 item_name=input("Product name('done'):")
 if item_name.lower()=='done':
  break
 price_input=input(f"{item_name} price:")
 price_list= price_input.split(',')
 
 for p in price_list:
  price=float(p.strip())
  quantity=int(input(f"Rs{price} wale {item_name} how many?:" ))

  name.append(item_name)
  prices.append(price)
  quantitys.append(quantity)
 print(f"{item_name}added to cart!\n")

price_array=np.array(prices)
qty_array=np.array(quantitys)
item_total=price_array*qty_array
grand_total=np.sum(item_total)

tax_amount = grand_total*0.18
final_amount = grand_total + tax_amount
most_selling = np.argmax(qty_array)
print("Best Seller:",name[most_selling])


for i in range(len(name)):
 print(f"{name[i]}|Qty:{qty_array[i]}|price:Rs{price_array[i]}|Item_total:Rs{item_total[i]}")

print("-"*30)
print(f"sub total: Rs{grand_total}")
print(f"GST (18%): Rs{tax_amount}")
print(f"Grand_Total(payable):Rs{final_amount}")




with open("bill_records.txt", "a") as file:
    file.write(f"\n--- Bill Record: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---\n")
    file.write(f"Sub Total: Rs {grand_total}\n")       
    file.write(f"GST (18%): Rs {tax_amount}\n")             
    file.write(f"Grand Total: Rs {final_amount}\n")   
    file.write("----------------------------------------\n")

print("\n✅ Bill details 'bill_records.txt' mein successfully save ho gayi hain!")