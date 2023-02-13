# -*- coding: utf-8 -*-

''' Import MySQL connector '''
import mysql.connector as mysql

''' Import argparse '''
import argparse

parser = argparse.ArgumentParser(description='Summarize weather for a specified zip code.')
parser.add_argument('sp_name', metavar='sp_name', type=str, help='Stored procedure name')
parser.add_argument('in_args', nargs='*', type=str, help="SP arguments")
args = parser.parse_args()

''' Set parameters for DB connection '''
db_user = 'root'
db_pwd = 'codio'
db_host = '127.0.0.1'
db_name = 'w2la'

''' Create connection with MySQL '''
cnx = mysql.connect(user=db_user, passwd=db_pwd,
                    host=db_host, db=db_name)                              

''' Create cursor to receive data '''
cursor = cnx.cursor()

''' Request results from DB with SELECT query '''
cursor.callproc(args.sp_name, args.in_args)

''' Retrieve results by iterating through the stored_results() '''
results = []
for result in cursor.stored_results():
    results.append(result.fetchall())

''' Close cursor '''
cursor.close()

''' Inspect results '''
print(results)
print('Number of results:', len(results))
for i,result in enumerate(results):
  print('Type of (outer) data result ' + str(i) + ': ' + str(type(result)))
  print('Type of (outer) data result ' + str(i) + ': ' + str(type(result[0])))