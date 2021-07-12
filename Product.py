#IMPORTING FUNCTIONALITY FOR DATABASE
import functions_for_database as func_db
import voice_recognization as voice_rec
#THIS FILE WILL CONTAIN CLASS PRODUCT

class product:
    '''THIS CLASS HAS THE FUNCTIONALITY TO RETRIVE PRODUCT DATA FROM THE DATABASE AND EXPORT IT TO CART OR WISH LIST'''

    def __init__(self):
        #making them instance variable rather than class variable because whenever the app runs and get_product method will be called ,it will create room for the existance of same product multiple times in the list 
        self.product_cloth_details=[]
        self.product_electronics_details=[]
        self.product_food_details=[]
    def get_product(self):
        '''GET DATA FROM DATABASE'''
        #calling show_all function from functions_for_database it will return all elements
        self.all_products=func_db.show_all("item.db","items")
        # storing products in list of their product type
        for product_info in self.all_products:
            if product_info[1] == "CLOTHES":
                self.product_cloth_details.append(product_info)
            elif product_info[1] == "ELECTRONICS":
                self.product_electronics_details.append(product_info)
            else:
                self.product_food_details.append(product_info)

    def product_cloth(self):
        return self.product_cloth_details

    def product_electronics(self):
        return self.product_electronics_details

    def product_food(self):
        return self.product_food_details

        
    def pick_product(self,user_choice):
        ''' SELECT PRODUCT BY NAME '''
        self.product_avalibility = False
        #user have the option to type the product or use voice recognization
        #for voice_recognization 
        print("speak")
        if user_choice == "voice_recognization":
            self.selected_product = voice_rec.speak()
        
        #for typing
        else:
            self.selected_product = input("Enter Product's Name")
        # check_avalibility of product:
        #list format = [(PRODUCT TYPE , PRODUCT NAME , PRODUCT PRICE , STOCK),(......)] 
        for element in self.product_cloth_details:
            if (self.selected_product == element[2].upper()) or (self.selected_product == element[2].lower()):
                self.product_avalibility = True
                self.element = element
                break
        for element in self.product_electronics_details:
            if (self.selected_product == element[2].upper()) or (self.selected_product == element[2].lower()):
                self.product_avalibility = True
                self.element = element
                break
        for element in self.product_food_details:
            if (self.selected_product == element[2].upper()) or (self.selected_product == element[2].lower()):
                self.product_avalibility = True
                self.element = element
                break
        #Return Product_details as tuple
        if self.product_avalibility == True:
            return self.element
        else:
            return False
        
    def add_to_cart(self,element):
        '''Move data to cart table of item database'''
        #element is in tuple format 
        #calling add_one_data function from functions_for_database it will data one element to database table.
        #passing database_name,table_name,element as parameter
        self.all_cart_elements=func_db.show_all("item.db","cart")
        print(self.all_cart_elements)
        self.product_present = False
        if len(self.all_cart_elements)>0:
            for element_cart in self.all_cart_elements:
                if element_cart[2]==element[2]:
                    self.product_present = True
                    #row_id = element_cart[0] #element_cart tuple will in following format (prod_type,prod_name,price,no_of_prod_in_cart)
                    #func_db.delete_one("item.db","cart",row_id)
                    element_cart=list(element_cart)
                    element_cart[4]+=1
                    
                    func_db.update_data("item.db",'cart',element_cart[4],element_cart[2]) 
                    
            if self.product_present == False:
                element=list(element)
                element[4]= 1
                element=tuple(element)
                func_db.add_one_data("item.db","cart",element[1:]) 
        else:
            element=list(element)
            element[4]= 1
            element=tuple(element)
            func_db.add_one_data("item.db","cart",element[1:])


    def add_to_wishlist(self,element):
        '''Move data to cart table of item database'''
        #element is in tuple format 
        #calling add_one_data function from functions_for_database it will data one element to database table.
        #passing database_name,table_name,element as parameter
        self.all_wish_elements=func_db.show_all("item.db","wishlist")
        print(self.all_wish_elements)
        self.product_present = False
        if len(self.all_wish_elements)>0:
            for element_wish in self.all_wish_elements:
                if element_wish[2]==element[2]:
                    self.product_present = True
                    print("Already in wishlist") #muju is print statment display karadayna gui pay 
                    break
                    
            if self.product_present == False:
                element=list(element)
                element[4]= 0 
                element = tuple(element)
                func_db.add_one_data("item.db","wishlist",element[1:]) #used slicing so as to get rid of row_id as an element of tuple.
        else:
            element=list(element)
            element[4]= 0 
            element = tuple(element)
            func_db.add_one_data("item.db","wishlist",element[1:]) #used slicing so as to get rid of row_id as an element of tuple.
        #yah jo choice hay add_to_cart ki muju issay button pay laga dayna 
        self.choice = input("Do you want to add this product to export to cart ? if yes then press 'y'")
        if self.choice == 'y' or self.choice == "Y":
            self.add_to_cart(element)

if __name__ == "main":
        p1=product()
        p1.get_product()
        print(p1.product_cloth)
        print(p1.product_food)
        print(p1.product_electronics)
        print("say")
        value=p1.pick_product("")
        print(value)
        #p1.add_to_cart(value)
        p1.add_to_wishlist(value)
