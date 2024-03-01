import sys

def process_data(input_data):
    return input_data.upper()
if __name__ == "__main__":
   # input_data = sys.argv[1]
    processed_data = process_data("hello")
    print(f"Processed data: {processed_data}")