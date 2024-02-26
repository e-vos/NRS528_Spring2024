import csv

years = []  # Create a list to store YYYY from the date column
annuals_dict = {}  # Dictionary for use later on...
ppm_values = []  # For the second task

# Find unique YYYY values, to iterate through the ppm values

with open(
        r"C:\Users\Elliot\Documents\Github\NRS528\NRS528_Spring2024\CodingChallenges\Coding_Challenge_3\co2-ppm-daily.csv") as co2:
    next(co2)

    for row in csv.reader(co2):
        date = row[0]  # This block splits row[0] by hyphens into a list, then grabs the first
        year = date.split('-')[0]  # item in the list (i.e. the year in YYYY format).
        years.append(year)  # Then add it to the years list

years_set = sorted(list(set(years)))  # Turn it into a set to get unique years, turn it back into a list, then sort it in ascending order.

# Now for iterating through the ppm column by the items in years_set

for year in years_set:

    with open(r"C:\Users\Elliot\Documents\Github\NRS528\NRS528_Spring2024\CodingChallenges\Coding_Challenge_3\co2-ppm-daily.csv") as co2:

        summed_values = float(0)  # Need float here because the ppm values are floats
        count_values = 0  # Count can be an integer

        next(co2)

        for row in csv.reader(co2):

            if str(year) in str(row[0]):  # Check if these are the values we're looking for

                summed_values += float(row[1])  # Sum all of the ppm values found with the current year index
                count_values += 1  # Count how many ppm values have been summed

            if count_values != 0:  # Best practice for the future, yes?

                annual_avg = float(summed_values / count_values)  # Calculate average ppm value for the year
                annuals_dict[year] = annual_avg  # Associate the average with the year, in the dictionary (e.g. 1959 | 300).

print("Contents of annuals dictionary = " + str(annuals_dict))

# Find the minimum, maximum, and average values for the entire dataset

with open(r"C:\Users\Elliot\Documents\Github\NRS528\NRS528_Spring2024\CodingChallenges\Coding_Challenge_3\co2-ppm-daily.csv") as co2:

    summed_values = float(0)  # Same as in Task 1
    count_values = 0

    next(co2)

    for row in csv.reader(co2):
        ppm = row[1]
        ppm_values.append(ppm)
        summed_values += float(ppm)
        count_values += 1

    srt_ppm_values = sorted(ppm_values)  # Need to sort these for the next steps

    min_ppm = srt_ppm_values[0]  # Since ppm values are sorted numerically, 1st item = minimum
    max_ppm = srt_ppm_values[-1]  # and last item = maximum.
    avg_ppm = summed_values / count_values

print("\n") # I'm putting these newlines before every printout block to increase readability
print(f"Minimum ppm value =  {min_ppm} ppm")
print(f"Maximum ppm value = {max_ppm} ppm")
print(f"Average ppm value = {avg_ppm} ppm")

# Seasonal average in Spring, Summer, Fall, and Winter

monthly_dict = {} # Dictionary to store monthly averages

with open(r"C:\Users\Elliot\Documents\Github\NRS528\NRS528_Spring2024\CodingChallenges\Coding_Challenge_3\co2-ppm-daily.csv") as co2:

    next(co2)  # Skip header

    for row in csv.reader(co2):

        date, ppm = row[0], float(row[1])
        month = date.split('-')[1]

        if month not in monthly_dict:

            monthly_dict[month] = []

        monthly_dict[month].append(ppm)

for month, ppm_values in monthly_dict.items():  # Need to calculate monthly averages before seasonal averages

    monthly_avg = sum(ppm_values) / len(ppm_values)
    monthly_dict[month] = monthly_avg

# Define seasons dictionary
seasons = {'spring': ["03", "04", "05"], 'summer': ["06", "07", "08"],
           'fall': ["09", "10", "11"], 'winter': ["12", "01", "02"]}

seasonal_avgs = {}  # Dictionary to store seasoal averages

for season, months in seasons.items():

    season_values = [monthly_dict[month] for month in months if month in monthly_dict]
    seasonal_avg = sum(season_values) / len(season_values)
    seasonal_avgs[season] = seasonal_avg

print("\n") # ""
for season, average in seasonal_avgs.items():

    print(f"{season} average = {average} ppm") # Print the seasonal averages across all years

# Calculate the anomaly for each value in the dataset relative to the mean for the entire time series.

anomalies = {}  # Dictionary to store anomaly values
position = 0  # Initialize the position counter

with open(r"C:\Users\Elliot\Documents\Github\NRS528\NRS528_Spring2024\CodingChallenges\Coding_Challenge_3\co2-ppm-daily.csv") as co2:
    next(co2)

    for row in csv.reader(co2):
        ppm_value = float(row[1])
        anomaly = ppm_value - avg_ppm  # Calculate anomaly value for the current ppm value based on avg_ppm
        anomalies[position] = anomaly  # Store the position as key and anomaly as its value in the dictionary
        position += 1  # Increment the position counter

print("\n") # ""
for value, anomaly in anomalies.items():
    print(f"Entry #{value} deviates {anomaly} ppm from the dataset mean.")

Contents of annuals dictionary = {'1958': 315.3004807692307, '1959': 315.8790196078429, '1960': 316.8222569444445, '1961': 317.61999999999983, '1962': 318.69220640569387, '1963': 318.94874100719426, '1964': 318.62375886524825, '1965': 320.2260638297872, '1966': 321.59765799256496, '1967': 322.0138247011951, '1968': 322.7914516129033, '1969': 324.5488928571427, '1970': 325.8655849056604, '1971': 326.4479180887374, '1972': 327.51316923076894, '1973': 330.02322957198476, '1974': 330.2248265895953, '1975': 331.23306060606063, '1976': 332.00996784565916, '1977': 333.93527210884366, '1978': 335.42905660377335, '1979': 336.7954268292682, '1980': 338.78596969696974, '1981': 340.09549857549854, '1982': 341.40758823529427, '1983': 342.9984615384613, '1984': 344.57359999999983, '1985': 346.1026791277259, '1986': 347.35453124999987, '1987': 349.2359701492537, '1988': 351.5589684813755, '1989': 353.1558974358976, '1990': 354.4028813559323, '1991': 355.61309192200554, '1992': 356.4537572254332, '1993': 357.1797084548104, '1994': 358.87334285714303, '1995': 360.83225352112686, '1996': 362.6507670454544, '1997': 363.7080174927114, '1998': 366.679858757062, '1999': 368.3254178674349, '2000': 369.5712464589234, '2001': 371.1067462686569, '2002': 373.2740173410401, '2003': 375.80642253521137, '2004': 377.47371830985946, '2005': 379.96399999999994, '2006': 381.8855910543131, '2007': 383.85930463576165, '2008': 385.51644518272417, '2009': 387.42231003039507, '2010': 389.83562310030396, '2011': 391.65559171597624, '2012': 393.8747660818713, '2013': 396.46677018633557, '2014': 398.7114705882352, '2015': 400.8659633027522, '2016': 404.28065420560745, '2017': 406.52384374999986}


Minimum ppm value =  312.33 ppm
Maximum ppm value = 412.66 ppm
Average ppm value = 354.85535280324115 ppm


spring average = 356.74317036175654 ppm
summer average = 355.6681871158778 ppm
fall average = 352.6596526278202 ppm
winter average = 354.3792471037786 ppm