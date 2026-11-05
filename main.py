import pandas as pd

data = pd.DataFrame({
    "order_id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "city": [
        "Tehran", "Shiraz", "Tehran", "Tabriz", "Shiraz",
        "Tehran", "Tabriz", "Shiraz", "Tehran", "Tabriz"
    ],
    "product": [
        "Laptop", "Phone", "Phone", "Laptop", "Laptop",
        "Phone", "Phone", "Laptop", "Laptop", "Phone"
    ],
    "quantity": [2, 3, 1, 1, 2, 4, 2, 1, 3, 5],
    "unit_price": [800, 300, 300, 800, 800, 300, 300, 800, 800, 300],
    "discount": [0, 10, 0, 5, 15, 10, 0, 0, 5, 10]
})

def calc(row):
    final = row["quantity"] * row["unit_price"] * (1 - (row["discount"] / 100))
    return final

def categor(revenue) :
    if revenue >= 1500 :
        return "High"
    elif 700 <= revenue < 1500 :
        return "Medium"
    else :
        return "Low"

def update():
    global data
    print("\n>> Updating ...\n")
    data["revenue"] = data.apply(calc,axis=1)
    data["category"] = data["revenue"].apply(categor)
    data = data.sort_values(by=["revenue"],ascending=False)

def data_best():
    mask = data["revenue"] >= 1000
    return data.loc[mask,["city","order_id","revenue"]]

def city_best():
    return data.groupby("city")["revenue"].agg(["sum","mean","max"])

def best_of_sale() :
    return data.pivot_table(
    values="revenue",
    index="city",
    columns="product",
    aggfunc="sum"
)

def main() :
    print(data)
    update()
    print("\n",data_best())
    print("\n",city_best(),"\n")
    print(best_of_sale(),"\n")
    print(data)

if __name__ == "__main__" :
    main()
    print("\n>> Thanks for choosing us ;)\n") 