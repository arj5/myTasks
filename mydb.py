import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	password = 'October_0510'

	)

# prepare cursor object

cursorObject = dataBase.cursor()\

# create database

cursorObject.execute("CREATE DATABASE tasks")

print("database created.")