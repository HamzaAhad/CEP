import functions_for_database as func_db
class payment:
    #muju yah jo element hay yah woh hay kay jab hum screen pay click karaingay to hamary pass ayga
    #is element kay indar (prod_type,prod_name,price,no_of_prod_in_cart) wala tuple hay
    #toh attach kardayna issay button say
    #secondaly yah jo element hay woh bina row_id kay pass hoga agar row_id wala pass karna hay toh har jagah index+1 kar dayna code mah
    def __init__(self,element):
        self.element=element
    
    def confirm_order(self):
        #yahan confirmation message dal dayna or agar yes ho to cart table say item delete ho jayga and items table say stock mah -1 ho jayga and after confirmation shopping history will be added to user_db
        self.confirm = input("Confirm order : ")
        if self.confirm == "yes": 
            #table cart
            #func_db.delete_one("item.db","cart",self.element[1])
            #table items
            self.all_products=func_db.show_all("item.db","items")
            for element_product in self.all_products:
                if element_product[2]==self.element[1]:
                   #element_product tuple will in following format (row_id,prod_type,prod_name,price,stock)
                    print(element_product)
                    element_product=list(element_product)
                    element_product[4]-=1
                    func_db.update_data_items("item.db",'items',element_product[4],element_product[2])
        #adding shopping_details to shop_his table of user.db
        #format (NAME , ADDRESS , PRODUCT , AMOUNT)
        func_db.add_one_data("user.db","shop_his",(self.name,self.address,self.element[1],self.total_amount))

    def cod(self):
        print("your amount is : ",self.total_amount)
        self.confirm_order()

    def card(self):
        self.card = input("CARD NUMBER : ")
        self.confirm_order()

    def shipping_info(self):
        self.name=input("ENTER NAME : ")
        self.address=input("ENTER ADDRESS : ")
        self.city=input("ENTER CITY : ")
        self.country=input("ENTER COUNTRY : ")
        self.method=input("CHOOSE METHOD OF PAYMENT EITHER 1.COD OR 2.CARD : ")
        self.price = self.element[2]
        self.quantity =self.element[3]
        self.total_amount = float(self.price) * float(self.quantity)

        if self.method == "1" :
            self.cod()
        else :
            self.card()

if __name__ == "main" :
    p=payment(('ELECTRONICS', 'TV', 50000.4, 4))
    p.shipping_info()