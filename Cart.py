import sys
sys.path.append(".")

from Product import product
import functions_for_database as func_db

class cart:
    '''THIS CART CLASS ALLOWS US TO INCREASE PRODUCT'S QUANTITY, DECREASE PRODUCT'S QUANTITY AND EXPORT PRODUCT FOR PAYMENT PURPOSE'''
    def __init__(self):
        self.all_cart_elements=func_db.show_all("item.db","cart")
        self.obj_prod = product() 
    def increase_element(self,element):
        '''INCREASE THE QUANTITY OF PRODUCT'''
        self.obj_prod.add_to_cart(element) # composition

    def decrease_element(self,element):
        '''DECREASE THE QUANTITY OF PRODUCT'''
        for element_cart in self.all_cart_elements:
            #if product is present and it's quantity is greater than zero
            #acha muju tumhay idhar bus ak cheez ka dehan rakhna hay agar element jo pass ho raha hay woh aysi jagah say a raha hay jahan apkay tuple mah row id nahi hay to if statement mah element[1] ho jayga
            #since idhar row_id hay
            #yah error a sakta  hay 
            if (element_cart[2]==element[2]) and element_cart[4]>1:
                element_cart=list(element_cart)
                element_cart[4]-=1
                func_db.update_data("item.db",'cart',element_cart[4],element_cart[2])
            elif (element_cart[2]==element[2]) and element_cart[4]==1:
                func_db.delete_one("item.db","cart",element_cart[2])

    def checkout(self,element):
        for element_cart in self.all_cart_elements:
            if (element_cart[2]==element[2]):
                self.export = element_cart[1:]
                return self.export
if __name__ == "main":
    c=cart()

    c.increase_element((3, 'ELECTRONICS', 'TV', 50000.4, 0))   


