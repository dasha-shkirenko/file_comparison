### Description
Tool was made for testing financial reports downloaded from different code version to ensure data consistency. Also it can be used for comparing two `.xls` or `.xlsx` files

### How it works
Script takes two `.xls` or `.xlsx` files and start matching each appropriate cell from files row by row. In case of detecting different value in appropriate cells, script prints to console next data:
> `Number of row`, `Number of column`, `Name of column`:

> `First file name`: `cell value`

> `Second file name`: `cell value`

This information helps you to understand where exactly files have difference.

In case of different number of rows in two files script finds first cells with different values, prints it to console, add message `From row #{row_number} reports start differentiating.` and exit from loop. It helps you to understand from what row files start differentiating and avoid useless script work.

In case of different number of rows script shows message `Number of columns is different. 
 File "First file name" has {x} columns 
 File "Second file name" has {y} columns` and stops.

### Running

##### 1. Create `virtualenv`:
- Create `virtualenv` named `myvenv`:
    >`python3 -m venv myvenv`

##### 2. Clone project:
- Execute being in your workspace directory:
    >`https://github.com/dasha-shkirenko/file_comparison.git`

##### 3. Launch `virtualenv` and install package dependencies:
- Launch `virtualenv`:
    >`source myvenv/bin/activate`
- Install package dependencies:
    >`pip install -r requirements.txt`
    
##### 4. Run service:
- Run beeing in project path. 
    >`python3 comparison.py file_1.xls file_2.xls 0`
- Script takes three arguments, firts two is file path to `.xls` or `.xlsx` files you need to compare, and third argument is number of column, which you want to ignore in process of comparing. If it's not needed, pass third argument as `0`, `False` or another text.
