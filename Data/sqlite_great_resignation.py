# sqlite_demo.py

import sqlite3
import pandas as pd

# use pandas to create dataframe based on csv data
df_linechartdata = pd.read_csv(r'line_chart_data.csv')
df_databystatemarch2023 = pd.read_csv(r'data_by_state_march_2023.csv')
df_top5industryannualquitrates = pd.read_csv(r'annual_quit_rates_top5.csv')
df_highestquitratesbystate = pd.read_csv(r'highest_quit_rates_by_state.csv')
df_sectorquits = pd.read_csv(r'sector_quits.csv')

# create a sqlite database and a connection to it
cnxn = sqlite3.connect('great_resignation.db')
crsr = cnxn.cursor()

# create linechart table with a primary key
create_statement_linechart = """CREATE TABLE linechartdata (
Rates text PRIMARY KEY,
'2001' real,
'2002' real,
'2003' real,
'2004' real,
'2005' real,
'2006' real,
'2007' real,
'2008' real,
'2009' real,
'2010' real,
'2011' real,
'2012' real,
'2013' real,
'2014' real,
'2015' real,
'2016' real,
'2017' real,
'2018' real,
'2019' real,
'2020' real,
'2021' real,
'2022' real,
'2023' real
);"""
crsr.execute(create_statement_linechart)

# create databystatemarch table with a primary key
create_statement_databystatemarch2023 = """CREATE TABLE databystatemarch2023 (
State text PRIMARY KEY,
'Hires rate' real,
'Hires level' integer,
'Job openings rate' real,
'Job openings level' integer,
'Quits rate' real,
'Quits level' integer
);"""
crsr.execute(create_statement_databystatemarch2023)

# create top5industryannualquitrates table with a primary key
create_statement_top5industryannualquitrates = """CREATE TABLE top5industryannualquitrates (
Industry text PRIMARY KEY,
'column_2018' real,
'column_2019' real,
'column_2020' real,
'column_2021' real,
'column_2022' real
);"""
crsr.execute(create_statement_top5industryannualquitrates)

# create highestquitratesbystate table with a primary key
create_statement_highestquitratesbystate = """CREATE TABLE highestquitratesbystate (
Rank integer PRIMARY KEY,
state text,
'Resignation Rate (Latest Month)' real,
'Resignation Rate (Last 12 Months)' real
);"""
crsr.execute(create_statement_highestquitratesbystate)

# create sectorquits table with a primary key
create_statement_sectorquits = """CREATE TABLE sectorquits (
Industry text PRIMARY KEY,
'2007' integer,
'2008' integer,
'2009' integer,
'2010' integer,
'2011' integer,
'2012' integer,
'2013' integer,
'2014' integer
);"""
crsr.execute(create_statement_sectorquits)

# insert your dataframes into that database
df_linechartdata.to_sql('linechartdata', cnxn, index=False, if_exists="append")
df_databystatemarch2023.to_sql('databystatemarch2023', cnxn, index=False, if_exists="append")
df_top5industryannualquitrates.to_sql('top5industryannualquitrates', cnxn, index=False, if_exists="append")
df_highestquitratesbystate.to_sql('highestquitratesbystate', cnxn, index=False, if_exists="append")
df_sectorquits.to_sql('sectorquits', cnxn, index=False, if_exists="append")

cnxn.close()

# success! you now have a sqlite database on your computer
