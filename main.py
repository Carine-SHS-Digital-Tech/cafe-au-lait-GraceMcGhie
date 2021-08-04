# NESTED DICTIONARY TO HOLD EACH ORDER
ORDER_DICTIONARY = {'ORDER_ID': [], 'TYPE': [], 'ITEM_1': [], 'QTY_1': [], 'EXGST_1': [], 'ITEM_2': [], 'QTY_2': [], 'EXGST_2': [], 'ITEM_3': [], 'QTY_3': [], 'EXGST_3': [], 'ITEM_4': [], 'QTY_4': [], 'EXGST_4': [], 'ORDER_CUPS': [], 'ORDER_GST': [], 'ORDER_TAX': [], 'ORDER_TOTAL': []}
PRICES = {'cappuccino': 3, 'espresso': 2.25, 'latte': 2.5, 'iced coffee': 2.5}
ORDER_ID_COUNT = 0  # The ORDER_ID count
while True:  # Infinite looped program
    mode = input("What Mode of operation would you like to use (New Order or Daily Summary): ")
    if mode.lower() == "new order":  # New Order (Default)
        print("\nNew Order")
        ORDER_ID_COUNT = ORDER_ID_COUNT + 1  # To increase ORDER_ID count for each loop
        ORDER_DICTIONARY["ORDER_ID"].append(ORDER_ID_COUNT)  # Adding ORDER_ID to the dictionary

        TYPE = input('Would you like takeaway or dine in (takeaway incurs a 5% surcharge): ')  # TYPE input
        if TYPE.lower() in ['takeaway', 'dine in']:  # Data validation for the TYPE input
            ORDER_DICTIONARY['TYPE'].append(TYPE)
        else:
            while TYPE.lower() not in ['takeaway', 'dine in']:
                TYPE = input('Wrong input.Try again.\nWould you like takeaway or dine in (takeaway incurs a 5% surcharge): ')
            ORDER_DICTIONARY['TYPE'].append(TYPE)

        print('\n4 available items\n Cappuccino : $3.00 \n Espresso : $2.25 \n Latte : $2.50 \n Iced_Coffee: $2.50\n\n')  # Showing the 4 line item options
        LOOP_COUNT = 0
        for x in range(0, 4):
            LOOP_COUNT = LOOP_COUNT + 1
            ITEM = f'ITEM_{LOOP_COUNT}'
            IITEM = input('What coffee from the list above would you like: ')
            if IITEM.lower() in ['cappuccino', 'espresso', 'latte', 'iced coffee']:
                ORDER_DICTIONARY[ITEM].append(IITEM)
            else:
                while IITEM.lower() not in ['cappuccino', 'espresso', 'latte', 'iced coffee']:
                    IITEM = input('Wrong input.Try again.\nWhat coffee from the list above would you like: ')
                    IITEM = IITEM.lower()
                ORDER_DICTIONARY[ITEM].append(IITEM)
            QTY = f"QTY_{LOOP_COUNT}"
            IQTY = int(input('What quantity of the coffee would you like: '))
            if IQTY > 0:
                ORDER_DICTIONARY[QTY].append(IQTY)
            else:
                while IQTY < 1:
                    IQTY = int(input('Wrong input.Try again.\nWhat quantity of the coffee would you like: '))
                ORDER_DICTIONARY[QTY].append(IQTY)
            EXGST = f"EXGST_{LOOP_COUNT}"
            IITEM = IITEM.lower()
            IEXGST = PRICES[IITEM]*IQTY
            ORDER_DICTIONARY[EXGST].append(IEXGST)
        print(ORDER_DICTIONARY)
    elif mode == "daily summary":   # Daily Summary
        print("Daily Summary")
    else:  # Incorrect input
        print("wrong input")
