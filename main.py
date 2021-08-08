from tabulate import tabulate
# NESTED DICTIONARY TO HOLD EACH ORDER
ORDER_DICTIONARY = {'ORDER_ID': [], 'TYPE': [], 'ITEM_1': [], 'QTY_1': [], 'EXGST_1': [], 'ITEM_2': [], 'QTY_2': [], 'EXGST_2': [], 'ITEM_3': [], 'QTY_3': [], 'EXGST_3': [], 'ITEM_4': [], 'QTY_4': [], 'EXGST_4': [], 'ORDER_TOTAL': []}
PRICES = {'cappuccino': 3, 'espresso': 2.25, 'latte': 2.5, 'iced coffee': 2.5}
ORDER_ID_COUNT = 0
CAPPUCCINO_COUNT = 0
ESPRESSO_COUNT = 0
LATTE_COUNT = 0
ICED_COFFEE_COUNT = 0
GST_COLLECTED = 0
DAILY_INCOME = 0

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
    count(IITEM, 'cappuccino', CAPPUCCINO_COUNT)
    count(IITEM, 'espresso', ESPRESSO_COUNT)
    count(IITEM, 'latte', LATTE_COUNT)
    count(IITEM, 'iced coffee', ICED_COFFEE_COUNT)

def count(i,coffee,counter):
    if i.lower() == coffee:
        counter = counter + 1

def order_filler():
    ITEM = f'ITEM_{LOOP_COUNT}'
    ORDER_DICTIONARY[ITEM].append(' ')
    QTY = f"QTY_{LOOP_COUNT}"
    ORDER_DICTIONARY[QTY].append("0")
    EXGST = f"EXGST_{LOOP_COUNT}"
    ORDER_DICTIONARY[EXGST].append("0")

def cups(no, number):
    for cups in range(0, len(ORDER_DICTIONARY[f'ITEM_{number}'])):
        no = no + ORDER_DICTIONARY[cups]

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
        y = ORDER_ID_COUNT - 1
        GST_1 = ORDER_DICTIONARY['EXGST_1'][y] * 0.1
        GST_2 = ORDER_DICTIONARY['EXGST_2'][y] * 0.1
        GST_3 = ORDER_DICTIONARY['EXGST_3'][y] * 0.1
        GST_4 = ORDER_DICTIONARY['EXGST_4'][y] * 0.1
        GST_COLLECTED = GST_COLLECTED + GST_1 + GST_2 + GST_3 + GST_4
        Total_1 = ORDER_DICTIONARY['EXGST_1'][y] + GST_1
        Total_2 = ORDER_DICTIONARY['EXGST_2'][y] + GST_2
        Total_3 = ORDER_DICTIONARY['EXGST_3'][y] + GST_3
        Total_4 = ORDER_DICTIONARY['EXGST_4'][y] + GST_4
        if ORDER_DICTIONARY['TYPE'][y].lower() == 'takeaway':
            Extra = (Total_1 + Total_2 + Total_3 + Total_4)*0.05
            Total = Total_1 + Total_2 + Total_3 + Total_4 + Extra
        else:
            Extra = 0
            Total = Total_1 + Total_2 + Total_3 + Total_4 + Extra
        amount_tendered = 0
        change = 0
        DAILY_INCOME = DAILY_INCOME + Total
        Info_Display = [['', 'Quantity', 'Item', 'Price', 'GST', 'Total', 'Extra Charges', 'Full Total'], ['Item 1', ORDER_DICTIONARY['QTY_1'][y], ORDER_DICTIONARY['ITEM_1'][y],ORDER_DICTIONARY['EXGST_1'][y], GST_1, Total_1], ['Item 2', ORDER_DICTIONARY['QTY_2'][y], ORDER_DICTIONARY['ITEM_2'][y],ORDER_DICTIONARY['EXGST_2'][y], GST_2, Total_2], ['Item 3', ORDER_DICTIONARY['QTY_3'][y], ORDER_DICTIONARY['ITEM_3'][y],ORDER_DICTIONARY['EXGST_3'][y], GST_3, Total_3], ['Item 4', ORDER_DICTIONARY['QTY_4'][y], ORDER_DICTIONARY['ITEM_4'][y],ORDER_DICTIONARY['EXGST_4'][y], GST_4, Total_4], ['Total', '', '', '', '', '', Extra,Total], ['Cash', '', '', '', '', '', '', amount_tendered], ['Change', '', '', '', '', '', '', change]]
        print(tabulate(Info_Display))
        while True:
            try:
                amount_tendered = float(input('How much money paid: '))
                break
            except ValueError:
                print('Wrong input.Try again.')
        change = amount_tendered - Total
        print('SALES RECEIPT:')
        print(tabulate(Info_Display))
    elif mode == "daily summary":   # Daily Summary
        print("\nDaily Summary")
        #  Total Number of Orders
        ORDER_DICTIONARY['ORDERS_COUNT'] = ORDER_ID_COUNT
        #  No.dine ins
        Dine_In = 0
        for t in range(0, len(ORDER_DICTIONARY['TYPE'])):
            if t == 'dine in':
                Dine_In = Dine_In + 1
        ORDER_DICTIONARY['DINE-IN'] = Dine_In
        #  No. takeaways
        Takeaway = 0
        for t in range(0,len(ORDER_DICTIONARY['TYPE'])):
            if t == 'takeaway':
                Takeaway = Takeaway + 1
        ORDER_DICTIONARY['TAKE_AWAY'] = Takeaway
        #  Total number of cappuccinos
        ORDER_DICTIONARY['CAPPUCCINO_COUNT'] = CAPPUCCINO_COUNT
        #  Total number of espressos
        ORDER_DICTIONARY['ESPRESSO_COUNT'] = ESPRESSO_COUNT
        #  Total number of latte
        ORDER_DICTIONARY['LATTE_COUNT'] = LATTE_COUNT
        #  Total number of ice coffee
        ORDER_DICTIONARY['ICED_COFFEE_COUNT'] = ICED_COFFEE_COUNT
        #  Total number of cups of coffee
        cup_count = 0
        cups(cup_count, 1)
        cups(cup_count, 2)
        cups(cup_count, 3)
        cups(cup_count, 4)
        ORDER_DICTIONARY['CUPS_COUNT'] = cup_count

        ORDER_DICTIONARY['GST_COLLECTED'] = GST_COLLECTED  #  Total Day's GST
        ORDER_DICTIONARY['DAILY_INCOME'] = DAILY_INCOME  #   Total Day's income
        SUMMARY = [['ORDERS_COUNT', 'DINE_IN', 'TAKE_AWAY', 'CAPPUCCINO_COUNT', 'ESPRESSO_COUNT', 'LATTE_COUNT', 'ICED_COFFEE_COUNT', 'CUPS_COUNT', 'GST_COLLECTED', 'DAILY_INCOME'],[ORDER_DICTIONARY['ORDERS_COUNT'],ORDER_DICTIONARY['DINE-IN'],ORDER_DICTIONARY['TAKE_AWAY'], ORDER_DICTIONARY['CAPPUCCINO_COUNT'], ORDER_DICTIONARY['ESPRESSO_COUNT'], ORDER_DICTIONARY['LATTE_COUNT'], ORDER_DICTIONARY[ 'ICED_COFFEE_COUNT'], ORDER_DICTIONARY['CUPS_COUNT'], ORDER_DICTIONARY['GST_COLLECTED'], ORDER_DICTIONARY['DAILY_INCOME']]]
        print(tabulate(SUMMARY))
    else:  # Incorrect input
        print("wrong input")
