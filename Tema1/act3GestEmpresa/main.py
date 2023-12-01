import pandas as pd;
import matplotlib.pyplot as plt

data = pd.read_csv("sales.csv")

def createBestPaidProductLines(data, product_line, gross_income, quantity):
    bestPaidProduct = data[[product_line, gross_income, quantity]].groupby(product_line).sum().round().sort_values(gross_income, ascending=False)
    bestPaidProduct.to_csv("best_paid_product.csv")

def bestPaidProductLine():
    tmp = pd.read_csv("best_paid_product.csv")
    bestLine = tmp.iloc[0]
    print(bestLine)
    print(tmp["Quantity"].iloc[0])

def bestPaidProductLine2():
    tmp = pd.read_csv("best_paid_product.csv")
    bestLine = tmp.iloc[1]
    print(bestLine)

def productEvolByMonths(data, product_line, gross_income, date):
        data[date] = pd.to_datetime(data[date])
        data["Month"] = data[date].dt.month
        evol = data[[product_line, gross_income, "Month"]].groupby(["Month", product_line]).sum().round().sort_values(["Month", gross_income], ascending = [True, False])
        evol.to_csv("product_evolution_month.csv")

def createEstudiProductes(data, product_line, quantity, date):
    estudi = data[[product_line, quantity, date]].groupby([date, product_line]).sum().round().sort_values([date, quantity], ascending = [True, False])
    estudi.to_csv("estudi_productes.csv")

def createEstudiGraph(date, quantity):
    tmp = pd.read_csv("estudi_productes.csv")
    tmp.plot(x=date, y=quantity, kind='line', figsize=(15, 6))
    plt.title("Evolució de les vendes dels productes al llarg del temps")
    plt.xlabel("Date")
    plt.ylabel("Quantity")
    plt.legend(loc='best')
    plt.grid(True)
    plt.show()

createEstudiGraph("Date", "Quantity")