class Order_Validation:
    @staticmethod
    def real_order():
        user_input=False
        while user_input==False:
            user_order=input('what are you ordering? \npress 0 for Pizza\npress 1 for Pasta\npress 2 for Salad')
            if user_order.isnumeric():
                user_order=int(user_order)
                menu=['Pizza','Pasta','Salad']
                if user_order<len(menu):
                    user_input=True
                    return user_order
                else:
                    print('this is not one of the options! Please order something else.')
            else:
                print('this is not one of the options! Please order something else.')