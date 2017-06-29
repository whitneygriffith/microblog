"""
Example connection to the mySQL database
"""

import mysql.connector
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import MYSQLDB_USER, MYSQLDB_PASS, MYSQLDB_HOST


def test_connect():
	# Open connection to database
	connection = mysql.connector.connect(user=MYSQLDB_USER, password=MYSQLDB_PASS, host=MYSQLDB_HOST)

	try:
		cursor = connection.cursor()
		query = "insert into safepassage.posts values (\"m\",\"ne\",\"b\",123.2,4.20);"
		cursor.execute(query)
		connection.commit()
	finally:
		print "DONE"

	connection.close()

if __name__ == "__main__":
	test_connect()