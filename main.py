# NESTED DICTIONARY TO HOLD EACH ORDER
ORDER_DICTIONARY = {'ORDER_ID': [], 'TYPE': [],
          'ITEM_1': [], 'QTY_1': [], 'EXGST_1': [],
          'ITEM_2': [], 'QTY_2': [], 'EXGST_2': [],
          'ITEM_3': [], 'QTY_3': [], 'EXGST_3': [],
          'ITEM_4': [], 'QTY_4': [], 'EXGST_4': [],
          'ORDER_CUPS': [], 'ORDER_GST': [], 'ORDER_TAX': [], 'ORDER_TOTAL': []}
PRICES = {'cappuccino': 3, 'espresso': 2.25, 'latte': 2.5, 'iced coffee': 2.5}
while True:  #Infinite looped program
    mode = input("What Mode of operation would you like to use (New Order or Daily Summary): ")
    if mode == "new order": #New Order (Default)
        print("\nNew Order\n")
        ORDER_DICTIONARY['TYPE'].append(input('Would you like takeaway or dine in (takeaway incurs a 5% surcharge): '))
        print('\n4 available items\n Cappuccino : $3.00 \n Espresso : $2.25 \n Latte : $2.50 \n Iced_Coffee: $2.50\n\n')
        count = 0
        for x in range(0, 4):
            count = count + 1
            ITEM = (f'ITEM_{count}')
            IITEM = input('What coffee from the list above would you like: ')
            if IITEM.lower() in ['cappuccino', 'espresso', 'latte', 'iced coffee']:
                ORDER_DICTIONARY[ITEM].append(IITEM)
            else:
                while IITEM.lower() not in ['cappuccino', 'espresso', 'latte', 'iced coffee']:
                    IITEM = input('Wrong input.Try again.\nWhat coffee from the list above would you like: ')
                    IITEM = IITEM.lower()
                ORDER_DICTIONARY[ITEM].append(IITEM)
            QTY = (f"QTY_{count}")
            IQTY = int(input('What quantity of the coffee would you like: '))
            ORDER_DICTIONARY[QTY].append(IQTY)
            EXGST = (f"EXGST_{count}")
            IITEM = IITEM.lower()
            IEXGST = PRICES[IITEM]*IQTY
            ORDER_DICTIONARY[EXGST].append(IEXGST)
        print(ORDER_DICTIONARY)
    elif mode == "daily summary":   #Daily Summary
        print("Daily Summary")
    else: #Incorrect input
        print("wrong input")
