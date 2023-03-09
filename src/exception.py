import sys
import logging

def error_message_details(error , error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()             # gives the info about the error what type of error has been occur or which line of exception has been occur and all those of the exception has been store under this variable
    file_name = exc_tb.tb_frame.f_code.co_filename   # return the filename
    error_message = "Error occur in python script [{0}] line number [{1}] error message [{2}]".format(
        file_name , exc_tb.tb_lineno , str(error)
    )
    return error_message

class CustomeException(Exception):
    def __init(self , error_message , error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message , error_detail= error_detail)

    def __str__(self):
        return self.error_message
    

if __name__ == "__main__":
    
    try:
        a = 1/0
    except Exception as e:
        logging.info("Divide my zero Error")
        raise CustomeException(e,sys)
