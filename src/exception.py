import os 
import sys 



def exception(error,error_details:sys):
    
    _,_,exc_info=error_details.exc_info()

    file_name=exc_info.tb_frame.f_code.co_filename

    return f"error found in line {exc_info.tb_lineno} in script {file_name} and error is {error}"




class Custom_Exception(Exception):

    def __init__(self,error,error_details:sys):
        self.error=error
        self.error_details=error_details
        super().__init__(error)
        self.exception_cls= exception(self.error,self.error_details)


    def __str__(self):
        return self.exception_cls

    
