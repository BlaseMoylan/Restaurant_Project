from logger import logger
class Log_Transaction_validation:
    @staticmethod
    def log_transaction_validation():
        user_order_log=False
        while user_order_log==False:
            order_log=input('Do you wish to continue with the current transaction log? (y/n) ')
            if order_log=='y':
                user_order_log=True
            elif order_log=='n':
                file=open('log.txt','w')
                file.close()
                user_order_log=True
            else:
                print('This is not one of the options!')