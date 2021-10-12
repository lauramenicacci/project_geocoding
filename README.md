# project_geocoding
European Import-Export Geoanalysis

Description:
Due to our interest in the flows of goods from and to the European Union, we decided to focus our project on the trade activity of the EU member countries, the USA and BRICS countries. Our idea is to show the economic value of goods imported and exported by sea every month by every EU member state in and from the 10 partners. The output will be a dynamic representation of the commercial relations. Our analysis is limited to the years 2020 and 2021 and we will analyse imports and exports separately.
The final output should visualize the monetary size of imports and exports in every month of the two selected years as well as the routes between the countries. 

Resources: 
https://ec.europa.eu/eurostat/web/transport/data/database

Visualization of results: 
The dots will represent the value of total imports (exports) of each EU country for each month of the selected years. 
The lines instead will represent the value of goods imported (exported) by each EU country from (to) each trading partner. 
The thickness of the lines will change according to the value of goods traded in each month of the selected years. 

User interaction: 
The user will be able to select the states between which she wants to see the exports and imports relationships. 

Tools:
We predict to use the following packages: geopandas, geopy and networkx. However, it might also be that while doing the project we will decide to include the use of other packages that better fit our purposes. 

Goals of the project:
show the economic size of export and import via maritime transportation 
analyse economic trends between EU and BRICS countries
make data and maps available for the user to select countries of interest 

IN DOUBT
Steps: 

Retrieve the dataset. The source we used to download data is https://ec.europa.eu/eurostat/web/transport/data/database. 
Clean and merge the datasets, rendering it available to use. 
Analysis 

