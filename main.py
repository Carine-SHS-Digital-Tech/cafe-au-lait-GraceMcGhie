from tabulate import tabulate
# NESTED DICTIONARY TO HOLD EACH ORDER
ORDER_DICTIONARY = {'ORDER_ID': [], 'TYPE': [], 'ITEM_1': [], 'QTY_1': [], 'EXGST_1': [], 'ITEM_2': [], 'QTY_2': [], 'EXGST_2': [], 'ITEM_3': [], 'QTY_3': [], 'EXGST_3': [], 'ITEM_4': [], 'QTY_4': [], 'EXGST_4': [], 'ORDER_TOTAL': []}
PRICES = {'cappuccino': 3, 'espresso': 2.25, 'latte': 2.5, 'iced coffee': 2.5}
ORDER_ID_COUNT = 0  # The ORDER_ID count

def order_function():
    ITEM = f'ITEM_{LOOP_COUNT}'
    IITEM = input('What coffee from the list above would you like: ')  # Input for ITEM
    while IITEM.lower() not in ['cappuccino', 'espresso', 'latte', 'iced coffee']:  # Data validation for ITEM
        IITEM = input('Wrong input.Try again.\nWhat coffee from the list above would you like: ')
        IITEM = IITEM.lower()
    ORDER_DICTIONARY[ITEM].append(IITEM)
    QTY = f"QTY_{LOOP_COUNT}"

    while True:  # Data validation for QTY
        try:
            IQTY = int(input('What quantity of the coffee would you like: '))  # Input for QTY
            break
        except ValueError:
            print('Wrong input.Try again.')
    while IQTY < 1:
        IQTY = int(input('Wrong input.Try again.\nWhat quantity of the coffee would you like: '))
    ORDER_DICTIONARY[QTY].append(IQTY)
    EXGST = f"EXGST_{LOOP_COUNT}"
    IITEM = IITEM.lower()
    IEXGST = PRICES[IITEM] * IQTY
    ORDER_DICTIONARY[EXGST].append(IEXGST)

def order_filler():
    ITEM = f'ITEM_{LOOP_COUNT}'
    ORDER_DICTIONARY[ITEM].append(' ')
    QTY = f"QTY_{LOOP_COUNT}"
    ORDER_DICTIONARY[QTY].append("0")
    EXGST = f"EXGST_{LOOP_COUNT}"
    ORDER_DICTIONARY[EXGST].append("0")




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

        print('\n4 available items\n Cappuccino : $3.00 \n Espresso : $2.25 \n Latte : $2.50 \n Iced Coffee: $2.50\n\n')  # Showing the 4 line item options

        LOOP_COUNT =  1
        order_function()
        New_Order = input('Would you like to order a different coffee (Yes or No)? ')
        while New_Order.lower() not in ['yes', 'no']:
            New_Order = input('Wrong input.Try again.\nIncorrect Would you like to order a different coffee (Yes or No)? ')
        while New_Order.lower() == 'yes' and LOOP_COUNT <= 4:
            LOOP_COUNT = LOOP_COUNT + 1
            order_function()
            New_Order = input('Would you like to order a different coffee (Yes or No)? ')
            while New_Order.lower() not in ['yes', 'no']:
                New_Order = input('Wrong input.Try again.\nIncorrect Would you like to order a different coffee (Yes or No)? ')
        while LOOP_COUNT < 4:
            LOOP_COUNT = LOOP_COUNT + 1
            order_filler()


        Info_Display = [ORDER_ID_COUNT]
        print(Info_Display)

        amount_tendered = int(input('How much money paid: '))

    elif mode == "daily summary":   # Daily Summary
        print("\nDaily Summary")
        #  Total Number of Orders
        ORDER_DICTIONARY['ORDERS_COUNT'] = ORDER_ID_COUNT
        #  No.dine ins
        Dine_In = 0
        for t in range(0, len(ORDER_DICTIONARY['TYPE'])):
            if t.lower() == 'dine in':
                Takeaway = Takeaway + 1
        ORDER_DICTIONARY['DINE-IN'] = Dine_In
        #  No. takeaways
        Takeaway = 0
        for t in range(0,len(ORDER_DICTIONARY['TYPE'])):
            if t.lower() == 'takeaway':
                Takeaway = Takeaway + 1
        ORDER_DICTIONARY['TAKE_AWAY'] = Takeaway
        #  Total number of cappuccinos


        #  Total number of espressos


        #  Total number of latte


        #  Total number of ice coffee


        #  Total number of cups of coffee
        cup_count = 0
        def cups (number)
            for cups in range(0,len(ORDER_DICTIONARY[f'ITEM_{number}'])):
                cup_count = cup_count + ORDER_DICTIONARY[cups]
        cups(1)
        cups(2)
        cups(3)
        cups(4)
        ORDER_DICTIONARY['CUPS_COUNT'] = cup_count
        #  Total Day's income

        #  Total Day's GST


        SUMMARY = [['ORDERS_COUNT' ,'DINE-IN' , 'TAKE_AWAY','CAPPUCCINO_COUNT' ,'ESPRESSO_COUNT','LATTE_COUNT' ,'ICED COFFEE_COUNT','CUPS_COUNT','DAILY_INCOME'],[ORDER_DICTIONARY['ORDERS_COUNT'],ORDER_DICTIONARY['DINE-IN'],ORDER_DICTIONARY['TAKE_AWAY']]]
        print(tabulate(SUMMARY))
    else:  # Incorrect input
        print("wrong input")
