import sys
def print_car_models(car_data):
    """Displays a list of car models along with their specifications."""
    headers = ['Model', 'Make', 'Year', 'Price', 'Fuel Type', 'Horsepower']

    # Create a list to hold rows of data, starting with the headers
    rows = [headers]

    # Print header information
    print('List of Available Car Models\n')

    # Iterate through car data
    for car in car_data:
        # Create a row of data for each car
        row = [
            '_'.join(str(item) for item in car['model']) if car['model'] else 'NA',
            car['make'] if car['make'] else 'NA',
            car['year'] if car['year'] else 'NA',
            '$' + format(car['price'], ',.2f') if car['price'] else 'NA',  # Format price as currency
            car['fuel_type'] if car['fuel_type'] else 'NA',
            car['horsepower'] if car['horsepower'] else 'NA'
        ]
        rows.append(row)

    # Calculate the maximum length for each column
    max_lens = []
    for i in range(len(headers)):
        max_len = max(len(headers[i]), max(len(str(row[i])) for row in rows[1:])) # TD
        max_lens.append(max_len)

    # Create a row of dashes with lengths determined by the maximum width of each column
    rows.insert(1, ['-' * l for l in max_lens])

    # Print the table
    for row in rows:
        for col, max_len in zip(row, max_lens):
            print(str(col).ljust(max_len + 2), end='')  # Add extra space for padding
        print()

    sys.exit(1)

car_data = [
    {'model': ['Civic', 'version 1'], 'make': 'Honda', 'year': 2023, 'price': 25000.99, 'fuel_type': 'Gasoline', 'horsepower': 158},
    {'model': ['Camry', 'version 2'], 'make': 'Toyota', 'year': 2022, 'price': None, 'fuel_type': 'Hybrid', 'horsepower': 208},
    {'model': '', 'make': 'Honda', 'year': 2023, 'price': 28000.75, 'fuel_type': 'Gasoline', 'horsepower': 192},
]

print_car_models(car_data)
