#Script that extract, transforms and load data from a Kaggle's csv

#Libraries
import sys
import pandas as pd
import warnings

warnings.simplefilter("ignore")

def run():
    #Extract data from a csv
    try:
        dir_csv = sys.argv[1]
    except:
        dir_csv = "./train.csv"

    df = pd.read_csv(dir_csv)

    #Drop Name and PassengerId
    try:
        df = df.drop(["Name","PassengerId"], axis=1)
    except:
        pass

    #Separation of Cabin
    try:
        df[["Deck", "Cabin_num", "Side"]] = df["Cabin"].str.split("/", expand=True)
        df = df.drop(["Cabin"],axis=1)
    except:
        pass

    # Clean empty data
    df[['VIP', 'CryoSleep', 'FoodCourt', 'ShoppingMall', 'Spa', 'VRDeck']] = df[['VIP', 'CryoSleep', 'FoodCourt', 'ShoppingMall', 'Spa', 'VRDeck']].fillna(value=0)

    #Convertion of cabin_num
    index_cabin_null = df[df["Cabin_num"].isnull()].index
    df["Cabin_num"] = df["Cabin_num"].fillna(value=0)
    df["Cabin_num"] = df["Cabin_num"].astype(int)
    for i in index_cabin_null:
        df["Cabin_num"][i] = None

    #It's necessary convert the boolean data types too
    df[["VIP","CryoSleep"]] = df[["VIP","CryoSleep"]].astype(int)

    #Load dataset
    try:
        dir_new_csv = sys.argv[2]
        df.to_csv(dir_new_csv, encoding='utf-8',index=False)
    except:
        df.to_csv('./transformed_train.csv', encoding='utf-8',index=False)
    
    print("Process terminated!")


#Entry point
if __name__ == "__main__":
    run()

else:
    print("This is a principal script")