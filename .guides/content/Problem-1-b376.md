- Create a stored procedure in the <code>w2la</code> database named <code>spGetLinks</code>
- The stored procedure should do the following:
  - Output the contents of the of the <code>links</code> table with the columns/fields in this order:
    - <code>orig</code>
    - <code>dest</code>
    - <code>miles</code>
  - Sequence the rows, first, in <code>ASC</code>ending order of <code>orig</code> and then <code>ASC</code>ending order of <code>dest</code>

Check the output from your stored procedure by executing the stored procedure in MySQL Workbench or clicking the button below.

{Run Your Stored Procedure}(bash data/exec_mysql_sp.sh spGetLinks)

{Check It!|assessment}(code-output-compare-3883254745)
