# Excel2Text
This repo is designed specifically for simplifying the process of writing the relations from the Discovery Matrix.
But can be modified to satisfy various needs, the python file basically reads an excel file, with indexed columns and spits out the data in textual form in another file.

## Dependencies
* Python 3.9
* Pandas module

## Instructions
1. This script must be placed in the same folder as the excel sheet to be read
2. Create a new file named "results.txt" in the same folder as this script
3. The first row in the spreadsheet must be indexed, starting from 0, refer to the spreadsheet attached for reference
4. Change the value of the variables in the python script before executing to the number of rows/columns in the required table

## Limitations
+ Works only for square matrices
+ The value of correlation between two elements must be either a 1 or a 0
***
### Author
Vibhav - <vibhavgopal2004@gmail.com>
