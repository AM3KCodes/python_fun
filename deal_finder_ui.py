import requests

def main_menu():
    option = input("""Welcome to the eBay deal finder interface. Please enter a number for the following options:
1. Search for items
2. Exit
""")
    if option:
        switch_handler(option)
    else:
        print("Invalid input. Please enter again.")
        main_menu()
    
def switch_handler(option):
    match option:
        case "1":
            prod_or_sandbox()
        case "2":
            print("Exiting application.")
            exit()
        case _:
            print("Invalid input. Returning to main menu.")
            main_menu()
                

def prod_or_sandbox():
    url_choice = input("Production (P) or Sandbox (S)?\n").lower()
    if url_choice == "p":
        url = "https://api.sandbox.ebay.com/buy/browse/v1/item_summary/search"
        search = input("Enter search: ")
        keyword_and_filters(url, search)

    elif url_choice == "s":
        url = "https://api.ebay.com/buy/browse/v1/item_summary/search"
        search = input("Enter search: ")
        keyword_and_filters(url, search)
    else:
        print("Invalid input. Please enter again.")
        switch_handler("1")

def keyword_and_filters(url, search):
    filters = []
    filter_string = input("""What filters do you want to include?
                          P) Price
                          C) Condition
                          For each filter, type the corresponding letter (case-insensitive).
                          """).upper()
    list(filter_string)
    for filter in filter_string:
        filters.append(filter)
    
    for filter in filters:
        if filter == "P":
            lower_bound = input("Enter the lower bound for the price range:")
            upper_bound = input("Enter the upper bound for the price range:")
            if (int(lower_bound) < 0) or (int(upper_bound) < 0):
                print("Invalid input. Enter again.")
                continue
            else:
                bounds = f"price:[{lower_bound}..{upper_bound}]"

        
        if filter == "C":
            condition = input("""What item condition do you want to search for?
                              1000 (New)
                              1500 (New (other))
                              2000 (Manufacturer refurbished)
                              2500 (Seller refurbished)
                              3000 (Used)
                              4000 (Used - Very Good)
                              5000 (Used - Good)
                              6000 (Used - Acceptable)
                              7000 (For parts or not working)
                  """)
            if condition != 1000 or condition != 1500 or condition != 2000 or condition != 2500 or condition != 3000 or condition != 4000 or condition != 5000 or condition != 6000 or condition != 7000:
                print("Invalid condition. Please enter again.")
            else:
                condition_string = "{{conditionIds:{}}}".format(condition)
        if len(filters) >= 2:
            if 'P' in filters and 'C' in filters:
                filter_argument = bounds + "," + condition_string
        else:
            filter_argument = bounds or condition_string
        
    limit = input("Include how many results?")
    query(url, search, limit, filter_argument)
    
    
    
def query(url, search, limit, filter_argument):
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    params = {
        "q": search, # search keyword
        "limit": int(limit), # amount of results
        "filter": f"{filter_argument}"  # optional filters
    }

    r = requests.get(url, headers=headers, params=params)
    data = r.json()

    for item in data.get("itemSummaries", []):
        print(item["title"], "-", item["price"]["value"], item["price"]["currency"])
    
    print("Status:", r.status_code)
    print("Response:", r.text)



main_menu()