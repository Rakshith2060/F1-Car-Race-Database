CSE 560 PROJECT PHASE-2  REPORT
Project Name : F1 RACES DATABASE
Name of the team : SQLCODE112

Team members:
Sridhara Halkurike Narasimha Swamy	shalkuri@buffalo.edu
Kushwanth Parameshwaraiah		kushwant@buffalo.edu
Rakshith Kumar Narasimha Murthy		rakshit2@buffalo.edu

Description

In this project we aim to collect, process and store data regarding Formula-1 race using RDBMS efficiently. It helps us to query data regarding laptimes, drivers, constructors, pitstop statistics to analyze the performance of drivers, constructors on different circuits for each driver.

Data sources:

We have used 3 sources for collecting the data these are:

1. Data.world dataset source : https://data.world/sportsvizsunday/2020-mar-formula-1/workspace/file?filename=All+F1+Races.xls
	- From Data.world data source we download All_F1_Races.xlsx file, which contain data regarding raceinfo, results, drivers, driver teams, constructors etc details.

2. Ergast.com pitstop API source : https://ergast.com/mrd/methods/pitstops/
	- We use API provided in this website to download all data regarding pitstops.

3. Ergast.com laptime API source : https://ergast.com/mrd/methods/laps/
	- We use API provided in this website to download all data regarding lap data which includes all the laps completed in each race in each season .

Installation and Setup 

1. Database Software Installation:
   - Install a compatible relational database management system (RDBMS) such as PostgreSQL(version 16 is used by us).

2. Database Creation:
   - We create a database named formulaOne using postgreSQL

Processing downloaded data to required CSVs :
	- We use python to read the downloaded files and process them uing python given modules. 
	- We then create all the CSVs in table_name.csv 

Deliverables structure:

milestone2.pdf
.zip file ------|
		| -- create_table_csv.py //To create table_name.csv from processing raw data in raw_data folder
		| -- create.sql
		| -- load.sql
		| -- final_csvs --------|				// use these csvs path in load.sql
		|			| -- circuits.csv
		|			| -- drivers.csv
		|			| -- driver_standings.csv
		|			| -- driver_teams.csv
		|			| -- constructors.csv
		|			| -- laptimes.csv
		|			| -- pitstops.csv
		|			| -- raceinfo.csv
		|			| -- results.csv
		| -- raw_data
		|			| -- All_F1_Races.xlsx
		|			| -- pitstops_scraped.csv
		|			| -- laptimedata 		//this is a folder that contains each year lap details data
		| -- f1_dbms
		|			| -- server -- database.js, server.js
		|			| -- f1dbapp			// This contains all the react app files- GUI
		| -- formula-one.sql					// This the the formula-one database dump
		| -- SQLCODE112_demo_video.mp4	


Creating Relations(Tables):
	- Please use the create.sql file given which contains the create table command for all the tables designed along with primary key and foreign key constraints designed.
	- Go to "Query Tool" for the created formula-one DB and use "Alt + O" to open file create.sql and run the queries.

Loading the data to tables:
	- Use formuls-one.sql file to restore database : this is a dump file of our DB - this is in tar exported
	- Go to restore option getting on right-click on formula-one database
	- select the formula-one.sql file given and click restore.
	- OR use the below method
	- Please use load.sql file to load all the data from the gicen CSV. 
	- Each CSV name is same as table name.
	- Go to "Query Tool" for the created formula-one DB and use "Alt + O" to open file load.sql and run the queries. 

	- **Note** : Please update the CSV absolute path in the load.sql file to your CSV path

Installation and setup of web application
	- Install NodeJs Version 18.12.0 from this link. https://nodejs.org/en/blog/release/v18.12.0
	- After node installation, move into the folder 'fi_dbms', open Command Prompt or any equivalent terminal and run the command: npm install
	- Move to the folder 'f1dbapp' inside the 'f1_dbms' folder. Open Command prompt and run: npm install

Running the backend server
	- Move to the folder 'f1_dbms'. Open the file 'database.js'. Replace the following values with the values from the PostgreSQL server
	- 		const client = new Client({
			host: "localhost",                             // Specifies the hostname or IP address of the PostgreSQL server
			user: "postgres",                             // Specifies the username used to authenticate with the PostgreSQL server.		
			port: 5432,                                        // Specifies the port number where the PostgreSQL server is running
			password: "onepiece",                  // Specifies the password used to authenticate user with the PostgreSQL server
  			database: "formulaOne",             // Specifies the name of the formula one PostgreSQL database
			});
	
	- Open Command Prompt and run the command: node server.js
	- This will run the backend server at 'http://localhost:3001'

Running the frontend server
	- Move to the folder 'f1dbapp'. Open Command Prompt and run the command: npm start
	- This will run the frontend server at 'http://localhost:3000'

Opening the web application
	- Open a browser such as Chrome and hit the URL: http://localhost:3001
