from logger import logger
class Log_Transaction_validation:
    @staticmethod
    def log_transaction_validation():
        """
        This method prompts the user to validate a transaction log and takes action accordingly.

        The user is asked if they wish to continue with the current transaction log ('y') or clear it ('n').
        If 'y' is selected, the method exits, indicating validation.
        If 'n' is selected, the method clears the transaction log by creating an empty 'log.txt' file and then exits.
        If an invalid input is provided, the user is informed that it's not one of the options and prompted again.

        Returns:
            None
        """
        user_order_log = False
        while not user_order_log:
            order_log = input('Do you wish to continue with the current transaction log? (y/n) ')
            if order_log == 'y':
                user_order_log = True
            elif order_log == 'n':
                # Clear the transaction log by creating an empty file
                with open('log.txt', 'w') as file:
                    pass
                user_order_log = True
            else:
                print('This is not one of the options!')