import fileinput

inputfile = 'wisconsin.geojson'

county_names = ['Adams','Ashland','Barron','Bayfield','Brown','Buffalo','Burnett','Calumet','Chippewa','Clark','Columbia','Crawford','Dane','Dodge','Door','Douglas','Dunn','Eau Claire','Florence','Fond du Lac','Forest','Grant','Green','Green Lake','Iowa','Iron','Jackson','Jefferson','Juneau','Kenosha','Kewaunee','La Crosse','Lafayette','Langlade','Lincoln','Manitowoc','Marathon','Marinette','Marquette','Menominee','Milwaukee','Monroe','Oconto','Oneida','Outagamie','Ozaukee','Pepin','Pierce','Polk','Portage','Price','Racine','Richland','Rock','Rusk','Saint Croix','Sauk','Sawyer','Shawano','Sheboygan','Taylor','Trempealeau','Vernon','Vilas','Walworth','Washburn','Washington','Waukesha','Waupaca','Waushara','Winnebago','Wood']

for county in county_names:
    county_name = county.lower().replace(" ", "_") # Get county name from array and make it URL-friendly
    outputfile = 'counties/' + county_name + '.geojson' # Make outputfile pathname
    cnty_search = "\"CNTY_NAME\": \"" + str(county_name.upper()) + "\"" # String to search for when extracting lines

    with open(inputfile) as oldfile, open(outputfile, 'w') as newfile:
        i = 0
        for line in oldfile:
            if cnty_search in line or (i < 4): # Take the first 4 lines of the file and all that contain the county
                line = line.rstrip()
                newfile.write(line)
            i += 1
        newfile.write(']}') # Close the JSON

    for line in fileinput.input(outputfile, inplace=1): # Remove the trailing comma from the last line so JSON will validate
        line = line.replace(",]}", "]}")
        print(line)

# Validate JSON. I used the jsonlint npm package to verify all files in the directory at once jsonlint tx/counties/*.geojson
