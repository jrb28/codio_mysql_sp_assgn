- Create a stored procedure in the <code>w2la</code> database named <code>spGetShortestNextEast</code> that does what the previous stored procedure does, but with this modification this constraint:
  - Of the locations that can be traveled to directly from a specified origin, output the location that is closest to the specified origin and also to the east of the specified origin
  - Output the location abbreviation, the full spelling of the location, and the number of miles to it, in that order
  - Represent the origin by an appropriate MySQL input argument

Check the output from your stored procedure by executing the stored procedure in MySQL Workbench or clicking the button below.

NOTE: This stored procedure required multiple nested SQL statements.  It can, however be created by using the SQL in previous problems.

{Run Your Stored Procedure for Location OK}(bash data/exec_mysql_sp.sh spGetShortestNextEast OK)

{Run Your Stored Procedure for Location D}(bash data/exec_mysql_sp.sh spGetShortestNextEast D)

{Run Your Stored Procedure for Location SL}(bash data/exec_mysql_sp.sh spGetShortestNextEast SL)

{Check It!|assessment}(code-output-compare-2667341417)
