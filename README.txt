Description:
This package contains several files & executions that need to occur separately.

Data Collection:
It starts with the web-scrapping code utilizing JavaScript library Puppeteer (pageScraper.js) to parse through the NCEI website (https://www.ncei.noaa.gov) and obtain all the relevant weather data per state for the year 2010 - 2024.

Data Cleaning:
Once the scraping is finished, the data cleaning process can start with the script.py file, which will cherry-pick the columns relevant for our analysis.

Data Storage:
All data storage was completed using DataGrip. A stored procedure was created to take each csv state weather data file and calculate maximum temperatures by month and year of each state.

Modeling:
All modeling work was done using Jupyter Notebook using Python to produce predicted temperatures and energy demand into a final csv for Tableau.

Tableau Visualization:
The attached Tableau workbook is a packaged workbook. If desired, it can be reconnected to the csv data source.

Installation:
Data Collection:
In the Collection directory, run "npm install" to install the necessary packages.

Data Cleaning:
Make sure you have python3.10+
There are no further installation required, just that the folder structure is upheld and the files downloaded from the scraper are in their respective places.

Data Storage:
Within the Storage directory, first, import each state table as the following, 'StateAbbreviation_1' as a table. Create the stored procedure titled STATETABLE from the file datasstorage.txt. Run a call as formatted in data storage.txt.

Modeling:
Make sure you have python3.10+
All required libraries are listed in the first cell. Ensure folder structure is upheld and adjust file paths to csvs as needed.

Tableau Visualization:
Open the workbook in Tableau Desktop. Reconnect to data source if desired.


Execution:
Data Collection:
In the Collection directory, run "npm run start" to open the chromium browser that will handle the scraping.

Data Cleaning:
In the Cleaning directory, run python script.py to start iterating through all the files in each of the state and organize them into a csv file per state.

Data Storage:
In the Storage directory, create a table titled ALL using a union of the created from the stored procedure state tables. Download this table as a csv for preliminary python regressions. 

Modeling:
Run the notebook to get model results and final csvs as needed. Use finaldata.csv for Tableau.

Tableau Visualization: 
Adjust any visual elements if desired through Tableau Desktop.

