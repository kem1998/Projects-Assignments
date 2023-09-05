PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: AgeGroups
DROP TABLE IF EXISTS AgeGroups;

CREATE TABLE AgeGroups (
    age_group_id INTEGER PRIMARY KEY AUTOINCREMENT,
    [groups]     STRING  NOT NULL
);


-- Table: AgeGroupVaccinations
DROP TABLE IF EXISTS AgeGroupVaccinations;

CREATE TABLE AgeGroupVaccinations (
    iso_code                            STRING  REFERENCES Locations (iso_code) 
                                                NOT NULL,
    date                                DATE    NOT NULL,
    age_group_id                        INTEGER REFERENCES AgeGroups (age_group_id) 
                                                NOT NULL,
    people_vaccinated_perhundred        INTEGER,
    people_fully_vaccinated_per_hundred INTEGER
);


-- Table: CountryDailyTotals
DROP TABLE IF EXISTS CountryDailyTotals;

CREATE TABLE CountryDailyTotals (
    iso_code                INTEGER REFERENCES Locations (iso_code) 
                                    NOT NULL,
    date                    DATE    NOT NULL,
    data_source_id          INTEGER REFERENCES DataSource (data_source_id) 
                                    NOT NULL,
    vaccine_id              INTEGER REFERENCES Vaccines (vaccine_id) 
                                    NOT NULL,
    total_vaccinations      INTEGER,
    people_vaccinated       INTEGER,
    people_fully_vaccinated INTEGER
);


-- Table: CountryStateDailyTotals
DROP TABLE IF EXISTS CountryStateDailyTotals;

CREATE TABLE CountryStateDailyTotals (
    iso_code                                    REFERENCES Locations (iso_code) 
                                                NOT NULL,
    location                            STRING  NOT NULL,
    date                                DATE    NOT NULL,
    total_vaccinations                  INTEGER,
    total_distributed                   INTEGER,
    people_vaccinated                   INTEGER,
    people_fully_vaccinated_per_hundred INTEGER,
    total_vaccinations_per_hundred      INTEGER,
    people_fully_vaccinated             INTEGER,
    people_vaccinated_per_hundred       INTEGER,
    distributed_per_hundred             INTEGER,
    daily_vaccinations_raw              INTEGER,
    daily_vaccinations                  INTEGER,
    daily_vaccinations_per_million      INTEGER,
    share_doses_used                    INTEGER
);


-- Table: CountryVaccByManufacturer
DROP TABLE IF EXISTS CountryVaccByManufacturer;

CREATE TABLE CountryVaccByManufacturer (
    iso_code           INTEGER REFERENCES Locations (iso_code) 
                               NOT NULL,
    date               DATE    NOT NULL,
    vaccine_id         INTEGER NOT NULL
                               REFERENCES Vaccines (vaccine_id),
    total_vaccinations INTEGER
);


-- Table: CountryVaccinations
DROP TABLE IF EXISTS CountryVaccinations;

CREATE TABLE CountryVaccinations (
    iso_code                            STRING  REFERENCES Locations (iso_code) 
                                                NOT NULL,
    date                                DATE    NOT NULL,
    total_vaccinations                  INTEGER,
    people_vaccinated                   INTEGER,
    people_fully_vaccinated             INTEGER,
    daily_vaccinations_raw              INTEGER,
    daily_vaccinations                  INTEGER,
    total_vaccinations_per_hundred      INTEGER,
    people_vaccinated_per_hundred       INTEGER,
    people_fully_vaccinated_per_hundred INTEGER,
    daily_vaccinations_per_million      INTEGER
);


-- Table: DataSource
DROP TABLE IF EXISTS DataSource;

CREATE TABLE DataSource (
    data_source_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    iso_code         STRING  REFERENCES Locations (iso_code) 
                             NOT NULL,
    source_name      STRING  NOT NULL,
    source_website   STRING,
    last_observation DATE    NOT NULL
);


-- Table: Locations
DROP TABLE IF EXISTS Locations;

CREATE TABLE Locations (
    iso_code STRING PRIMARY KEY
                    UNIQUE,
    location STRING NOT NULL
);


-- Table: LocationVaccines
DROP TABLE IF EXISTS LocationVaccines;

CREATE TABLE LocationVaccines (
    iso_code         STRING  REFERENCES Locations (iso_code) 
                             NOT NULL,
    vaccine_id       INTEGER REFERENCES Vaccines (vaccine_id) 
                             NOT NULL,
    date_avaliable   DATE,
    date_unavaliable DATE,
    data_source_id   INTEGER REFERENCES DataSource (data_source_id) 
                             NOT NULL
);


-- Table: Vaccines
DROP TABLE IF EXISTS Vaccines;

CREATE TABLE Vaccines (
    vaccine_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name       STRING  NOT NULL
);


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
