items={
    1:{"name":"Pizza","price":200},
    2:{"name":"Chicken Pizza","price":220},
    3:{"name":"Bugger","price":200},
    4:{"name":"Biryani","price":200},
    5:{"name":"Sandwich","price":200},
    6:{"name":"chicken lolipop","price":200},
}
def display_items():
    print("Available:")
    for key,item in items.items():
        print(f"{key} .{item['name']}-{item['price']}")
