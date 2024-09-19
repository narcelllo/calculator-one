from flask import request as FlaskRequest
from typing import Dict, List
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class Calculator3:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_hendler = driver_handler
        
    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json
        input_data = self.__validate_body(body)
        print(f"input {input_data}")
        print (type(input_data))

        variance = self.__calculate_variance(input_data)
        print(f"variance {variance}")
        print(type(variance))
        multiplication = self.__calculate_mutiplication(input_data)
        print(f"multiplication {multiplication}")
        print(type(multiplication))
        self.__verify_result(variance, multiplication)

        formated_response = self.__format_response(variance)
        return formated_response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise Exception('body does not contain numbers! - incorrect format! \n Examble format: {"numbers": 3.4, 4, 64.13}')
        
        input_data = body["numbers"]
        return input_data
    
    def __calculate_variance(self, numbers: List[float]) -> float:
         variance = self.__driver_hendler.variance(numbers)
         return variance
    
    def __calculate_mutiplication(self, numbers: List[float]) -> float:
        multiplication = 1
        for num in numbers:
            multiplication *= num
        return multiplication

    def __verify_result(self, variance: float, multiplication: float) -> None:
        if variance < multiplication:
            raise Exception('failed: variance < multiplication')
        
    def __format_response(self, variance: float) -> Dict:
        return {
            "data": {
                "Calculator": 3,
                "result": variance,
                "success": True
        }
    }