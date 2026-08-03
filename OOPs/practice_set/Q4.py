class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, other):
        return self.price > other.price


def main() :
    odr1 = Order("Pizza", 450)
    odr2 = Order("Kaju Katli", 920)

    res = odr1 > odr2
    if res:
        print("Order 1 is costly")
    else:
        print("Order 2 is costly")

main()