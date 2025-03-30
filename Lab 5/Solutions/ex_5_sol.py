def f5_1(file_path: str = 'customers-100.csv') -> None:
    """
    Count and display the number of customers per country.
    
    This implementation uses defaultdict to count occurrences,
    providing a concise approach to counting country frequencies.
    
    Args:
        file_path: Path to the CSV file containing customer data (default: 'customers-100.csv')
    
    Output:
        Prints the count of customers from each country in alphabetical order
    """
    import csv
    from collections import defaultdict
    
    # Initialize defaultdict to store country counts
    countries = defaultdict(int)
    
    # Open and process the CSV file
    with open(file_path) as file:
        # Skip the header row
        _ = next(file)
        
        # Create CSV reader
        csv_file = csv.reader(file)
        
        # For each record, increment the count for the country (at index 6)
        for records in csv_file:
            countries[records[6]] += 1
    
    # Print results in alphabetical order by country name
    for country in sorted(countries):
        print(countries[country], 'from', country)


def f5_2(file_path: str = 'customers-100.csv') -> None:
    """
    Count and display the number of customers per country.
    
    This implementation uses the csv.DictReader class which makes
    the code more readable by accessing columns by name rather than index.
    
    Args:
        file_path: Path to the CSV file containing customer data (default: 'customers-100.csv')
    
    Output:
        Prints the count of customers from each country in alphabetical order
    """
    import csv
    
    # Dictionary to store country counts
    country_counts = {}
    
    # Open and process the CSV file
    with open(file_path) as file:
        # Use DictReader to get named columns
        reader = csv.DictReader(file)
        
        # Process each row
        for row in reader:
            country = row['Country']
            
            # If country already exists in dictionary, increment its count
            if country in country_counts:
                country_counts[country] += 1
            # Otherwise, initialize its count to 1
            else:
                country_counts[country] = 1
    
    # Print results in alphabetical order by country name
    for country in sorted(country_counts.keys()):
        print(country_counts[country], 'from', country)


def f5_3(file_path: str = 'customers-100.csv') -> None:
    """
    Count and display the number of customers per country.
    
    This implementation demonstrates a more functional programming approach,
    using generators and the Counter class from collections.
    
    Args:
        file_path: Path to the CSV file containing customer data (default: 'customers-100.csv')
    
    Output:
        Prints the count of customers from each country in alphabetical order
    """
    import csv
    from collections import Counter
    from typing import Iterator
    
    # Extract countries from CSV
    def extract_countries() -> Iterator[str]:
        with open(file_path) as file:
            # Skip header
            next(file)
            
            # Create CSV reader
            reader = csv.reader(file)
            
            # Yield each country
            for row in reader:
                yield row[6]
    
    # Count occurrences of each country using Counter
    country_counter = Counter(extract_countries())
    
    # Print results in alphabetical order by country name
    for country, count in sorted(country_counter.items()):
        print(count, 'from', country)