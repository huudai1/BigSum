import logging
import sys
from src.math_utils import MyBigNumber

# Configure logging to output to console
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)

def main():
    big_number = MyBigNumber()
    
    # Example from the requirement
    stn1 = "1234"
    stn2 = "897"
    
    print(f"Adding '{stn1}' and '{stn2}'...")
    result = big_number.sum(stn1, stn2)
    print(f"Final Result: {result}")
    
    # Another example
    stn3 = "999"
    stn4 = "1"
    print(f"\nAdding '{stn3}' and '{stn4}'...")
    result2 = big_number.sum(stn3, stn4)
    print(f"Final Result: {result2}")

if __name__ == "__main__":
    main()

