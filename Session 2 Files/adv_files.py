import json

# The file example from before was fairly simple. This is a more advanced example to show what you can do.
cars_file = 'data\\cars.json'

with open(cars_file, 'r') as f:
    cars = json.load(f)

# Lets combine the ability to iterate and our dict commands to transform the data into nested dicts
new_cars = {}

# Iterate over the list
for car in cars:
    # Setup some dictionaries
    main_details = {}
    driving_details = {}
    fine_details = {}
    
    # Lets get the ID first
    id = car.get('_id').get('$oid')
    
    # Let's get the main details next (name, year, origin)
    main_details.setdefault('Name', car.get('Name'))
    main_details.setdefault('Year', car.get('Year'))
    main_details.setdefault('Origin', car.get('Origin'))

    # Let's get the driving details next (mpg, horsepower, acceleration)
    driving_details.setdefault('Miles_per_Gallon', car.get('Miles_per_Gallon'))  
    driving_details.setdefault('Horsepower', car.get('Horsepower'))
    driving_details.setdefault('Acceleration', car.get('Acceleration'))
    
    # Let's get the finer details last (cylinders, displacement, weight)
    fine_details.setdefault('Cylinders', car.get('Cylinders'))
    fine_details.setdefault('Displacement', car.get('Displacement'))
    fine_details.setdefault('Weight_in_lbs', car.get('Weight_in_lbs'))

    # Create a dictionary with everything in it
    compacted = {
        'main_details': main_details,
        'driving_details': driving_details,
        'fine_details': fine_details
    }

    # Append it to the finalized dictionary
    new_cars.setdefault(id, compacted)
    
# Let's write it to a file now
new_cars_file = 'data\\new_cars.json'
with open(new_cars_file, 'w') as f:
    json.dump(new_cars, f, indent=4)

# Just as this file converted a list into nested dicts, you can do the reverse or more advanced stuff (like loading this data into memory as class object)
# It will work with any size of file