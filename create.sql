-- Create circuits table
CREATE TABLE circuits (
    circuitId VARCHAR(40) PRIMARY KEY,
    circuitName VARCHAR(100)  NOT NULL,
    country VARCHAR(50)
);

-- Create drivers table
CREATE TABLE drivers (
    driverId VARCHAR(40) PRIMARY KEY,
    givenName VARCHAR(100) NOT NULL,
    familyName VARCHAR(100) NOT NULL,
    dateOfBirth DATE,
    nationality VARCHAR(100)   
);

-- Create constructors table
CREATE TABLE constructors (
    constructorId VARCHAR(40) PRIMARY KEY,
    constructorName VARCHAR(100) NOT NULL,
    nationality VARCHAR(50) NOT NULL
);

-- Create RaceInfo table
CREATE TABLE raceinfo (
    season INT NOT NULL,
    round INT NOT NULL,
	raceName VARCHAR(100) NOT NULL,
    date DATE,
    raceTime TIME,
    circuitId VARCHAR(40) NOT NULL,
    PRIMARY KEY (season, round),
    FOREIGN KEY (circuitId) REFERENCES circuits(circuitId)
);

-- Create results table
CREATE TABLE results (
    season INT NOT NULL,
    round INT NOT NULL,
    driverId VARCHAR(40) NOT NULL,
    resultGrid INT NOT NULL,
    resultLap INT,
    resultStatus VARCHAR(100),
    PRIMARY KEY (season, round, driverId),
    FOREIGN KEY (season, round) REFERENCES raceinfo(season, round),
    FOREIGN KEY (driverId) REFERENCES drivers(driverId)
);

-- Create Driver stardings table
CREATE TABLE driver_standings (
    season INT NOT NULL,
    round INT NOT NULL,
    driverId VARCHAR(40) NOT NULL,
    position INT NOT NULL,
    points INT NOT NULL,
    positionText VARCHAR(2),
    PRIMARY KEY (season, round, driverId),
    FOREIGN KEY (season, round) REFERENCES raceinfo(season, round),
    FOREIGN KEY (driverId) REFERENCES drivers(driverId)
);

-- Create Driver team table
CREATE TABLE driver_teams (
    season INT NOT NULL,
    driverId VARCHAR(40) NOT NULL,
    constructorId VARCHAR(40) NOT NULL,
    PRIMARY KEY (season, driverId),
    FOREIGN KEY (driverId) REFERENCES drivers(driverId),
    FOREIGN KEY (constructorId) REFERENCES constructors(constructorId)
);

-- Create pitstops table
CREATE TABLE pitstops (
    season INT NOT NULL,
    round INT NOT NULL,
    driverId VARCHAR(40) NOT NULL,
    lap INT NOT NULL,
    stop INT NOT NULL,
    time TIME,
    duration INTERVAL NOT NULL,
    PRIMARY KEY (season, round, driverId, lap),
    FOREIGN KEY (season, round) REFERENCES raceinfo(season, round),
    FOREIGN KEY (driverId) REFERENCES drivers(driverId)
);

-- Create lapTime table
CREATE TABLE laptimes (
    season INT NOT NULL,
    round INT NOT NULL,
    lap int NOT NULL,
    driverId VARCHAR(40) NOT NULL,
    position VARCHAR(100),
    laptime TIME NOT NULL,
    PRIMARY KEY (season, round, driverId, lap),
    FOREIGN KEY (season, round) REFERENCES raceinfo(season, round),
    FOREIGN KEY (driverId) REFERENCES drivers(driverId)
);