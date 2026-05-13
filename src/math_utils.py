import logging

class MyBigNumber:
    """
    Class to perform addition of two large numbers represented as strings.
    """
    
    def sum(self, stn1: str, stn2: str) -> str:
        """
        Adds two numbers represented as strings using column addition logic (3rd grade style).
        Logs each step of the process.
        
        Args:
            stn1: The first number string.
            stn2: The second number string.
            
        Returns:
            The sum of the two numbers as a string.
        """
        # Initialize variables
        i = len(stn1) - 1
        j = len(stn2) - 1
        carry = 0
        result = []
        step = 1

        # Iterate from right to left
        while i >= 0 or j >= 0 or carry > 0:
            # Get digits, default to 0 if index is out of bounds
            digit1 = int(stn1[i]) if i >= 0 else 0
            digit2 = int(stn2[j]) if j >= 0 else 0
            
            # Calculate sum of digits
            current_sum = digit1 + digit2
            
            log_msg = f"Bước {step}: Lấy {digit1} cộng với {digit2} được {current_sum}."
            
            # If there was a carry from previous step
            if carry > 0:
                total_sum = current_sum + carry
                log_msg += f" Cộng tiếp với nhớ {carry} được {total_sum}."
                current_sum = total_sum
            
            # Update carry and result digit
            carry = current_sum // 10
            result_digit = current_sum % 10
            
            # Store result digit
            result.append(str(result_digit))
            
            # Finalize log message for this step
            current_result_str = "".join(result[::-1])
            log_msg += f" Lưu {result_digit} vào kết quả (hiện tại: \"{current_result_str}\") và nhớ {carry}."
            logging.info(log_msg)
            
            # Move to the next digits
            i -= 1
            j -= 1
            step += 1

        # Reverse and join the result list to get the final string
        return "".join(result[::-1])

