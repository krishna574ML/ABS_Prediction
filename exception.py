import sys
from logger import logging

def error_message_details(error_message , error_details:sys):
    _,_, exc_tb = error_details.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    linenumber = exc_tb.tb_lineno
    error = str(error_message)
    error_message = f"error occured in the file {filename} on the line {linenumber} with error{error}"
    return error_message

    
    
    
class SensorException(Exception):
    
    def __init__(self , error_message , error_details:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message , error_details=error_details)
        
        
    def __str__(self):
        return self.error_message


        
    