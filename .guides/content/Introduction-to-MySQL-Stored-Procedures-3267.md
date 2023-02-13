## Key characteristics of stored procedures

- Stored procedures are queries that are stored in the database for repeated execution.
  - They are, essentially, programming code that can be executed at any time
  - So, creating stored procedures makes sense when a particular query will be used frequently
- Stored procedures are more powerful and flexible than hard-coded queries, however, because they permit the query to be tailored to a particular need
  - Flexibility is accomplished by sending arguments to a stored procedure as inputs that, for example, can be used in a <code>WHERE</code> clause
- Databases can "interoperate" with other software applications so that data can be extracted and used programmatically with code in other programming contexts, for example, with Python code
  - We will use the <code>mysql.connector</code> in Python to input <code>MySQL</code> data into our Python code


  ## Refreshers from Class

  - Please recall from class that you will need to refresh the database navigation pane in order to see your stored procedures after you have written them.
  - Buttons have been provided in this guide that, when clicked, your stored procedures will be executed and compared with the correct output.  As you write your stored procedures, however, you will probably want to execute them without checking them, just to verify you are getting the output you desire.  Please recall from class that you can do this in two ways within MySQL Workbench:
    - Hover over the stored procedure and click on the "lightning bolt". 
    ![Execute Stored Procedure with Lightning Bolt](.guides/img/jb/sp_lightning.jpg)
    - Open an SQL editor window and execute the SQL "CALL __stored_procedure_name__;"
    ![Execute Stored Procedure with SQL Script](.guides/img/jb/sp_sql_editor.jpg)
  
These two methods work in the MySQL Workbench instances that run directly on your computer as well as the MySQL Workbench instances that run within this Codio guide.     