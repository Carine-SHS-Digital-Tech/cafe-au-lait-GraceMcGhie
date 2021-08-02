# NESTED DICTIONARY TO HOLD EACH ORDER
ORDER_DICTIONARY = {'ORDER_ID': [], 'TYPE': [],
          'ITEM_1': [], 'QTY_1': [], 'EXGST_1': [],
          'ITEM_2': [], 'QTY_2': [], 'EXGST_2': [],
          'ITEM_3': [], 'QTY_3': [], 'EXGST_3': [],
          'ITEM_4': [], 'QTY_4': [], 'EXGST_4': [],
          'ORDER_CUPS': [], 'ORDER_GST': [], 'ORDER_TAX': [], 'ORDER_TOTAL': []}
while True:  #Infinite looped program
    mode = input("What Mode of operation would you like to use (New Order or Daily Summary): ")

    if mode == "new order": #New Order (Default)
        print("New Order")

    elif mode == "daily summary":   #Daily Summary
        print("Daily Summary")

    else: #Incorrect input
        print("wrong input")

