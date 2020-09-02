# Project Title: Is the NBA Combine an Effective Predictor of In Game Performance

By: Markham Lee

This was a project for my CSE163 - Intermediate Data Programming Course at the University of Washington. The version posted here has some updated analysis related to the number of players above the average for points per game and win shares and those in the 75th percentile for same. The report PDF is also significantly streamlined as the report contained items that were very specific to the assignment rubric, and aren't particularly relevant outside of the class. Items called out in "version information" are items I specifically added to the project after I turned it in, in order to enhance it as a portfolio project.

This project makes heavy use of Jupyter Notebooks, if you don't have the environment for Jupyter Notebook, Binder is a free open source tool that can read a directory containing Jupyter Notebooks and provide a browser based environment to run them  in.

Please clone or download this project before interacting with it, you won't be able to save changes or notes to this repository

**Included in this repository are the following files:**

* NBA_Project(Revised).ipynb is the Jupyter notebook that contains the original code, some additions I after I had turned the project in also has analyses/write-up embedded into it. This is the primary source of the code for this project.
* nba_stats contains the files with NBA player statistics
* new_data contains the file with the NBA Combine information
* data_analysis.py contains the code that generates all of the visualizations, it's the original code from the assignment, save the additional code I added to the Jupyter notebook
* data_processing.py contains the code for ingesting and cleaning the data
* If you want to run the analysis with the python code directly just run everything from the visualization file, as it will call the ingestion file when necessary. In Visual Studio code I would just right click and select "run the file"  

**Python Packages Information:**

* Pandas for data frame interactions
* OS for accessing a file directory, glob for opening multiple CSV files and appending them into one data frame
* matplotlib and seaborn for the visualizations
* numpy and sklearn are listed in the jupyter notebook but not used since regression and/or ML ended up not being necessary. I left them there as I may use them in future versions 

**Development Tools & Language Information:**

* Managed the python environment and packages with Anaconda
* IDE: Visual Studio Code for Python and Markdown file editing
* Jupyter Notebook
* Flake8 for code hygiene and lintiing for .py and .md files created in Visual Studio Code

## Update Information

### 9-1-2020 NBA_Project(Revised)**

* Added analysis related to number and % of athletes selected with the first 15 picks of the draft that performed above the league average in win shares and points per game
* Added significance tests for PPG, I.e. is there any difference in the proportion of players above and below the average
* Added analysis around the number of players selected with the first 15 picks of the draft that performed in the 75th percentile

### Future changes

* Add a PDF file that's a high level summary of all findings replete with visualizations
* Add a static version of the Jupyter Notebook
* Use the NBA API to gather a larger data set, extended the in game player staistics to 20-30 seasons
* Add combine data for a similar time frame as above
