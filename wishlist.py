
from Product import product

import functions_for_database as func_db
class wishlist:
    ''' WE CAN ADD , DELETE FROM WISHLIST AND CAN ALSO EXPORT WISH TO CART'''
    def __init__(self):
        self.all_wish_elements=func_db.show_all("item.db","wishlist")
        self.obj_prod = product() #composition
    def add_to_wishlist(self,element):
        self.obj_prod.add_to_wishlist(element)
    def export_to_cart(self,element):
        self.obj_prod.add_to_cart(element)
    def delete_from_wishlist(self,element):
        for element_wish in self.all_wish_elements:
            if (element_wish[2]==element[2]):
                func_db.delete_one("item.db","wishlist",element_wish[2])
if __name__ == "main":

    w = wishlist()
    w.delete_from_wishlist((2, 'CLOTHES', 'PANT', 230.23, 2))