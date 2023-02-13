- Create a stored procedure in the <code>w2la</code> database named <code>spGetNextCount</code> that does the following:
  - For all locations, output the location abbreviations that can be traveled to directly from each of those locations and the count of the number of feasible next destinations for each location, in that order.
  
  - Order the output in <code>ASC</code>ending order of location abbreviation.

Check the output from your stored procedure by executing the stored procedure in MySQL Workbench or clicking the button below.

{Run Your Stored Procedure}(bash data/exec_mysql_sp.sh spGetNextCount)

{Check It!|assessment}(code-output-compare-2428926219)
