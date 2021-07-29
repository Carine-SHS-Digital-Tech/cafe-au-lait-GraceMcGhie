mode = input("What Mode of operation would you like to use (New Order or Daily Summary): ")
if mode == "new order": #New Order (Default)
    print("new order")
elif mode == "daily summary": #Daily Summary
    print("daily summary")
else:
    print("wrong input")
