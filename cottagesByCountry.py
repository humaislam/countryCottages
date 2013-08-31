import itertools
import csv

numAdults = []
for i in range(0,31):
	numAdults.append(str(i))

numChildren= []

for i in range(0,11):
	numChildren.append(str(i))

numInfants = []
for i in range(0,6):
	numInfants.append(str(i))

numPets = []
for i in range(0,4):
	numPets.append(str(i))

duration = ['2', '3', '4', '5', '7', '14', '21', 'D']

countryRegions = []

headings = ['Country', 'Region', 'num of Adults', 'num of Children', 'num of Infants', 'num of Pets', 'num of Days']

def makeCountryFile(country, countryRegions):
	thisFile = country[0] + ".csv"
	myFile = open(thisFile, 'wb')
	wr = csv.writer(myFile, quoting=csv.QUOTE_ALL)
	wr.writerow(headings)

 	for r in itertools.product(country, countryRegions, numAdults, numChildren, numInfants, numPets, duration): 
	    	wr.writerow( r)
	return


england = ['England']
engRegion = ['All regions', 'Bedfordshire', 'Buckhinghamshire', 'Derbyshire', 'Gloucestershire', 'Hertfordshire', 'Leicestershire', 'Lincolnshire', 'Northamptonshire', 'Nottinghamshire', 'Oxfordshire', 'Rutland', 'Shropshire', 'Staffordshire', 'Warwickshire', 'Worcestershire', 'Cambridge', 'Essex', 'Norfolk', 'Suffolk', 'County Durham', 'Northumberland', 'Cheshire', 'Cumbria', 'Lancashire', 'Cornwall', 'Devon', 'Dorset', 'Somerset', 'Berkshire', 'Greater London', 'Hampshire', 'Isle of Wight', 'Kent', 'Surrey', 'Sussex', 'Wiltshire', 'Yorkshire', 'Brecon Beacons', 'Cotswolds', 'Dartmoor', 'Exmoor', 'Forest of Dean', 'Lake District', 'New Forest', 'Norfolk Broads', 'Northumberland National Park', 'Peak District', 'Shakespeare Country', 'South Downs', 'Wye Valley', 'Yorkshire Dales', 'Yorkshire Moors','None']

makeCountryFile(england, engRegion)

scotland = ['Scotland']
scotRegion = ['All regions', 'Angus', 'Argyle and Bute', 'Fife', 'Isle of Mull', 'Perthshire', 'Stirlingshire', 'Aberdeenshire', 'Highlands', 'Isle of Skye', 'Orkney Islands', 'Outer Hebrides', 'Ayrshire', 'Dumfries and Galloway', 'Edinburgh and the Lothians', 'Glasgow and Clyde Valley', 'Isle of Arran', 'Isle of Cumbrae', 'The Scottish Borders', 'Cairngorms', 'Loch Lomond and the Trossachs', 'None']

makeCountryFile(scotland, scotRegion)

wales = ['Wales']
walesRegion = ['All regions', 'Cardigan/Ceredigon', 'Powys', 'Anglesey', 'County Conwy', 'Gwynedd', 'North Wales Borders', 'Carmarthenshire', 'Glamorgan', 'Monmouthshire', 'Pembrokeshire Coast', 'Snowdonia', 'Wye Valley', 'None']

makeCountryFile(wales, walesRegion)

channel= ['Channel Islands']
channelRegion = ['All regions', 'Jersey', 'None']

makeCountryFile(channel, channelRegion)

france = ['France']
franceRegion = ['All regions', 'Auvergne', 'Burgundy', 'Ile-de-France and Paris', 'Limousin', 'Loire Valley', 'Alps', 'Franche-Comte', 'Alsace', 'Champagne', 'Lorraine', 'Brittany', 'Normandy', 'Pas-de-Calais', 'Picardy', 'Cote-d\'Azur', 'Languedoc-Rousillon', 'Provence', 'Aquitaine', 'Dordogne and Lot', 'Midi-Pyrenees', 'Poitou-Charentes', 'Vendee', 'None']

makeCountryFile(france, franceRegion)

ireland = ['Ireland']
irelandRegion = ['All regions', 'County Cavan', 'County Dublin', 'County Kildaire', 'County Laois', 'County Longford', 'County Louth', 'County Meath', 'County North Tipperary', 'County Offaly', 'County Westmeath', 'County Wicklow', 'County Carlow', 'County Kilkenny', 'County South Tipperary', 'County Waterford', 'County Cork', 'County Kerry', 'County Clare', 'County Donegal', 'County Galway', 'County Leitrim', 'County Limerick', 'County Mayo', 'County Roscommon', 'County Silgo', 'None']

makeCountryFile(ireland, irelandRegion)

italy = ['Italy']
italyRegion = ['All regions', 'Lazio', 'Tuscany', 'Umbria', 'Liguria', 'Lombardy', 'Veneto', 'Sardinia', 'Sicily', 'Campania', 'Puglia/Apulia', 'None']

makeCountryFile(italy, italyRegion)

