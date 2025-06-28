import pandas as pd
import os
file_path = 'sales_data.csv'

if not os.path.exists(file_path):
    df_init = pd.DataFrame([
        {"ID": 1, "Customer": "Alice", "Product": "Keyboard", "Quantity": 2, "Price": 50},
        {"ID": 2, "Customer": "Bob", "Product": "Mouse", "Quantity": 1, "Price": 20},
        {"ID": 3, "Customer": "Charlie", "Product": "Monitor", "Quantity": 1, "Price": 150},
    ])
    df_init.to_csv(file_path, index=False)

def load_data():
     return pd.read_csv(file_path)


def save_data(df):
    df.to_csv(file_path, index=False)



def create():
    new = {"ID": 4, "Customer": "Diana", "Product": "Laptop", "Quantity": 1, "Price": 900}
    df = load_data()
    df = pd.concat([df, pd.DataFrame([new])], ignore_index=True)
    save_data(df)
    print("✅ Record added!")



def read():
    df = load_data()
    print("📄 Current Data:")
    print(df)


def update():
    df = load_data()
    df.loc[df['ID'] == 2, 'Product'] = "Wireless Mouse"
    df.loc[df['ID'] == 2, 'Price'] = 25
    save_data(df)
    print("🔁 Record updated!")

def delete():
    df = load_data()
    df = df[df['ID'] != 3]
    save_data(df)
    print("🗑️ Record deleted!")

if __name__ == "__main__":
    create()
    read()
    update()
    delete()
    read()
