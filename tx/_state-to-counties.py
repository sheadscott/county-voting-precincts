import fileinput

inputfile = 'tx/tx-precincts.geojson'

countyNames = ["Anderson","Andrews","Angelina","Aransas","Archer","Armstrong","Atascosa","Austin","Bailey","Bandera","Bastrop","Baylor","Bee","Bell","Bexar","Blanco","Borden","Bosque","Bowie","Brazoria","Brazos","Brewster","Briscoe","Brooks","Brown","Burleson","Burnet","Caldwell","Calhoun","Callahan","Cameron","Camp","Carson","Cass","Castro","Chambers","Cherokee","Childress","Clay","Cochran","Coke","Coleman","Collin","Collingsworth","Colorado","Comal","Comanche","Concho","Cooke","Coryell","Cottle","Crane","Crockett","Crosby","Culberson","Dallam","Dallas","Dawson","Deaf Smith","Delta","Denton","DeWitt","Dickens","Dimmit","Donley","Duval","Eastland","Ector","Edwards","Ellis","El Paso","Erath","Falls","Fannin","Fayette","Fisher","Floyd","Foard","Fort Bend","Franklin","Freestone","Frio","Gaines","Galveston","Garza","Gillespie","Glasscock","Goliad","Gonzales","Gray","Grayson","Gregg","Grimes","Guadalupe","Hale","Hall","Hamilton","Hansford","Hardeman","Hardin","Harris","Harrison","Hartley","Haskell","Hays","Hemphill","Henderson","Hidalgo","Hill","Hockley","Hood","Hopkins","Houston","Howard","Hudspeth","Hunt","Hutchinson","Irion","Jack","Jackson","Jasper","Jeff Davis","Jefferson","Jim Hogg","Jim Wells","Johnson","Jones","Karnes","Kaufman","Kendall","Kenedy","Kent","Kerr","Kimble","King","Kinney","Kleberg","Knox","Lamar","Lamb","Lampasas","La Salle","Lavaca","Lee","Leon","Liberty","Limestone","Lipscomb","Live Oak","Llano","Loving","Lubbock","Lynn","McCulloch","McLennan","McMullen","Madison","Marion","Martin","Mason","Matagorda","Maverick","Medina","Menard","Midland","Milam","Mills","Mitchell","Montague","Montgomery","Moore","Morris","Motley","Nacogdoches","Navarro","Newton","Nolan","Nueces","Ochiltree","Oldham","Orange","Palo Pinto","Panola","Parker","Parmer","Pecos","Polk","Potter","Presidio","Rains","Randall","Reagan","Real","Red River","Reeves","Refugio","Roberts","Robertson","Rockwall","Runnels","Rusk","Sabine","San Augustine","San Jacinto","San Patricio","San Saba","Schleicher","Scurry","Shackelford","Shelby","Sherman","Smith","Somervell","Starr","Stephens","Sterling","Stonewall","Sutton","Swisher","Tarrant","Taylor","Terrell","Terry","Throckmorton","Titus","Tom Green","Travis","Trinity","Tyler","Upshur","Upton","Uvalde","Val Verde","Van Zandt","Victoria","Walker","Waller","Ward","Washington","Webb","Wharton","Wheeler","Wichita","Wilbarger","Willacy","Williamson","Wilson","Winkler","Wise","Wood","Yoakum","Young","Zapata","Zavala"]

for county in range(1,255):
    countyName = countyNames[county-1].lower().replace(" ", "-") # Get county name from array and make it URL-friendly
    outputfile = 'tx/counties/' + countyName + '.geojson' # Make outputfile pathname
    cntyNumber = "\"cntykey\": " + str(county) + "," # Sting to search for when extracting lines

    with open(inputfile) as oldfile, open(outputfile, 'w') as newfile:
        i = 0
        for line in oldfile:
            if cntyNumber in line or (i < 4): # Take the first 4 lines of the file and all that contain the county
                line = line.rstrip()
                newfile.write(line)
            i += 1
        newfile.write(']}') # Close the JSON

    for line in fileinput.input(outputfile, inplace=1): # Remove the trailing comma from the last line so JSON will validate
        line = line.replace(",]}", "]}")
        print line

# Validate JSON. I used the jsonlint npm package to verify all files in the directory at once jsonlint tx/counties/*.geojson
