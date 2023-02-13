- Repeat the previous problem in a stored procedure named <code>spGetNextEast</code> with this added constraint:
  - Output only the data for the locations that can be visited immediately from a specified origin if those locations are to the east of the specified origin.
  - Order the output in the same manner as in the previous problems with the fields in the same order.

Check the output from your stored procedure by executing the stored procedure in MySQL Workbench or clicking the button below.

Note: This stored procedure may require two <code>SELECT</code> statements, either one embedded within another or two sequential query statements.

{Run Your Stored Procedure for OK}(bash data/exec_mysql_sp.sh spGetNextEast OK)

{Run Your Stored Procedure for DE}(bash data/exec_mysql_sp.sh spGetNextEast DE)

{Check It!|assessment}(code-output-compare-2712800813)
