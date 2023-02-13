- Create a stored procedure in the <code>w2la</code> database named <code>spGetNext</code> that does the following:
  - Output the abbreviations for the locations that can be traveled to directly from a specified origin (using its abbreviation) and the mileage to those destinations, with the two columns in that order.
  - Order the output in <code>ASC</code>ending order of the <code>miles</code>
  - Represent the origin abbreviation by an appropriate MySQL input argument

Check the output from your stored procedure by executing the stored procedure in MySQL Workbench or clicking the button below, which uses SL as the <code>orig</code>.

{Run Your Stored Procedure for Location SL}(bash data/exec_mysql_sp.sh spGetNext SL)   

{Run Your Stored Procedure for Location LA}(bash data/exec_mysql_sp.sh spGetNext LA)   

{Check It!|assessment}(code-output-compare-723096472)
