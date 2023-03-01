#Increase the Logger’s transaction_count by one
 #Add the price of the Order object to the Logger’s daily_sales
#Increase the Logger’s transaction_count by one
#Add the price of the Order object to the Logger’s daily_sales
#Write a well-formatted message to the log.txt file 
# containing the current transaction count, 
# the name of the dish ordered, the store it was ordered from,
# the price of the item, and the combined daily income.
#Close the log.txt file.
#As a developer, I want to use the Singleton pattern 
# (as shown in the Design Patterns Demo repo) to create 
# a single instance of a Logger object inside the logger.py file 
# and import this instance into the Franchise class 
# to be shared by all instantiations.
class Logger:
    def __init__(self) -> None:
        self.count=0
        self.daily_sales=0
    def log_transaction(self,order,store_number):
        self.count+=1
        self.daily_sales+=order.price
        file=open('log.txt','a')
        file.write(f'TRX#{self.count}: {order.dish_name} at location {store_number}: ${order.price}. Total: ${self.daily_sales}\n')
        file.close()
logger=Logger()
