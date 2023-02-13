----------

# Assignment Database

This guide presents an assignment in which you will write stored procedures in a MySQL database named <code>w2la</code>.  This database contains the data for  the Williamsburg to LA problem we have discussed in class.  Its Entity Relationship (ER) Diagram is shown below.  Each of the two foreign keys are highlighted in the two images.

![ER Diagram](.guides/img/jb/w2la_er.jpg)

Here are a description of the tables and the fields:

<code>loc</code> Table 
| Field | Description |
|---------|----------|
| <code>abbrev</code> | abbreviation of the location for a table row  |
| <code>location</code> | location written as city, state  |
| <code>lat</code> | latitude  |
| <code>lon</code> | longitude  |
| <code>miles_n</code> | miles north of LA (as crow flies) |
| <code>miles_e</code> | miles east of LA (as crow flies) |

<code>links</code> Table 
| Field | Description |
|---------|----------|
| <code>orig</code> | a reference starting location for data in the table row  |
| <code>dest</code> | a feasible next stop from the reference <code>orig</code>  |
| <code>miles</code> | distance in miles between <code>orig</code> and <code>dest</code>  |




Please load the <code>w2la</code> database by clicking the button below, which may also be used to instantiate a fresh database without any stored procedures.  In other words, clicking on the button will delete any stored procedures you have written.

{Load/Reset Database}(sh .guides/restart.sh) 

# Getting Started with MySQL in Codio

The information below is shown as a refresher on signing into MySQL in Codio.  Use it as necessary as a reference.

You must first sign into the MySQL instance that is running in conjunction with this guide.  To do so, navigate to the window in the left pane with the heading that begins with  <code>gurusaturn-...</code> and sign into MySQL, as show in the first image below, and click on the instance to open it.  Next, enter the password (<code>codio</code>) where indicated in the second image below.  This window provides the same MySQL Workbench user interface with which you are already familiar and it permits you to navigate through the databases as well as view the administrative options.

![MySQL Login](.guides/img/jb/mysql_login1.jpg)
![MySQL Login](.guides/img/jb/mysql_login2.jpg)


This guide uses a MySQL database called <code>sales</code>.  In order to load it, please click on the button below, and then <code>Refresh All</code> in the database navigation area, if necessary, to see the <code>sales</code> database.  If the database crashes or you would like to start defining your stored procedures from scratch, you can click on the button below again.  Be aware, however, that the stored procedures you define with be _persistent_ unless you click on this button.  Clicking on this button returns the <code>sales</code> database to it original state.
