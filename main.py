# NESTED DICTIONARY TO HOLD EACH ORDER
ORDER_DICTIONARY = {'ORDER_ID': [], 'TYPE': [],
          'ITEM_1': [], 'QTY_1': [], 'EXGST_1': [],
          'ITEM_2': [], 'QTY_2': [], 'EXGST_2': [],
          'ITEM_3': [], 'QTY_3': [], 'EXGST_3': [],
          'ITEM_4': [], 'QTY_4': [], 'EXGST_4': [],
          'ORDER_CUPS': [], 'ORDER_GST': [], 'ORDER_TAX': [], 'ORDER_TOTAL': []}
PRICES = {'Price_Cappuccino': 3, 'Price_Espresso': 2.25, 'Price_Latte': 2.5, 'Price_Iced_Coffee': 2.5}

while True:  #Infinite looped program
    mode = input("What Mode of operation would you like to use (New Order or Daily Summary): ")
    if mode == "new order": #New Order (Default)
        print("New Order")
        ORDER_DICTIONARY['TYPE'].append(input('Would you like takeaway or dine in (takeaway incurs a 5% surcharge): '))
        print('4 available items:\n Cappuccino : $3.00 \n Espresso : $2.25 \n Latte : $2.50 \n Iced_Coffee: $2.50')
        count = 0
        for x in range(0, 4):
            count = count + 1
            ITEM = (f'ITEM_{count}')
            ORDER_DICTIONARY[ITEM].append(input('What will be you first line item from the list above: '))
            QTY = (f"QTY_{count}")
            ORDER_DICTIONARY[QTY].append(int(input('What quantity of the coffee would you like: ')))
            EXGST = (f"EXGST_{count}")
            PRICES[
            ORDER_DICTIONARY[EXGST].append()
        print(ORDER_DICTIONARY)
    elif mode == "daily summary":   #Daily Summary
        print("Daily Summary")

    else: #Incorrect input
        print("wrong input")
