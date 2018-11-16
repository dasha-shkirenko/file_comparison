### Description
Tool was made for testing financial reports downloaded from different code version to ensure data consistency. Also it can be used for comparing two `.xls` files

### How it works
Script takes two `.xls` files and start matching each appropriate cell from files row by row. In case of detecting different value in appropriate cells, script prints to console next data:
> `Number of row`, `Name of column`:

> `First file name`: `cell value`

> `Second file name`: `cell value`

This information helps you to understand where exactly files have difference.

In case of different number of rows in two files script finds first cells with different values, prints it to console, add message `From row #{row_number} reports start differentiating.` and exit from loop. It helps you to understand from what row files start differentiating and avoid useless script work.

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
    >`python3 comparison.py file_1.xls file_2.xls`
