class Queue:
    def __init__(self):
        self.items=[]
    def size(self):
        return len(self.items)
    
    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        if self.size()==0:
            return None
        return self.items.pop(0)
    
    def show_queue(self):
        print(self.items)

class IceCreamShop():
    def __init__(self,flavors):
        self.flavors=flavors
        self.orders=Queue()

    def take_order(self,customer,flavor,scoops):
        if flavor in self.flavors:
            if scoops>0 and scoops<4:
                print("Order created!")
                order={"customer":customer,"flavor":flavor,"scoops":scoops}

                self.orders.enqueue(order)  # results: the dictionary is inside the list.
            elif scoops==0 or scoops<0:
                print("You don't want any?")
            else:   # if scoops>4:
                print("Sorry, I don't have that much")
        else:
            print(f"I don't have {flavor} flavor here")

    def show_all_orders(self):
        print("\nAll Pending Ice Cream Orders:")
        for key in self.orders.items:
            print(f"Customer: {key['customer']} -- Flavor: {key['flavor']} -- Scoops: {key['scoops']}")
    
    # dequeue the head order in the queue and show it
    def next_order(self):
        # dequeue will pop(0) from the list.
        # this should be like this:
        # [{"customer":"string","flavor":"string","scoops":integer}]
        dequeue_order=self.orders.dequeue()
        if dequeue_order is not None:
            print("\nNext Order Up!")
            print(f"Customer: {dequeue_order['customer']} -- Flavor: {dequeue_order['flavor']} -- Scoops: {dequeue_order['scoops']}")
        else:
            print("There is no order yet")

        

shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()