- Create a stored procedure in the <code>w2la</code> database named <code>spGetShortestNext</code> that does the following:
  - Of the locations that can be traveled to directly from a specified origin, output the location that is closest to the specified origin 
  - Output the location abbreviation and the number of miles to it, in that order
  - Represent the origin by an appropriate MySQL input argument

Check the output from your stored procedure by executing the stored procedure in MySQL Workbench or clicking the button below.

Note: This stored procedure may require two <code>SELECT</code> statements, either one embedded within another or two sequential query statements.

{Run Your Stored Procedure for location D}(bash data/exec_mysql_sp.sh spGetShortestNext D)

{Run Your Stored Procedure for location SL}(bash data/exec_mysql_sp.sh spGetShortestNext SL)

{Check It!|assessment}(code-output-compare-689256993)
