import sys
import logging
from logger import logging

def error_mssg_detail(error , error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_mssg = "error occurred in python script name [{0}] line number [{1}] error message  [{2}]".format(file_name,exc_tb.tb_lineno,str(error))
    return error_mssg
    
                
class CustomExecption(Exception):
    def __init__(self,error_mssg,error_detail:sys):
        super().__init__(error_mssg) 
        self.error_mssg = error_mssg_detail(error_mssg,error_detail = error_detail )
        
    def __str__(self):
        return self.error_mssg 

