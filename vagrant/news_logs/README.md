## PRE-REQUISITES
- [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
- [Vagrant](https://www.vagrantup.com/downloads.html)

## VM CONFIGURATION
1. Fork and clone VM configuration files from [https://github.com/udacity/fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm)
2. Change directory to the vagrant directory (inside of the recently forked repository)
3. Download the database config file [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
4. Unzip the file and move `newsdata.sql` into it's own subfolder called `news_logs` within the vagrant folder
5. Start the virtual machine using `vagrant up`
6. Once finished, log into your VM using `vagrant ssh`
7. Navigate into the folder created in step 4 and execute `psql -d news -f newsdata.sql` to populate the database
8. Connect to the database with `psql -d news` and you should be able to see the populated authors, articles, and log tables

## HOW TO RUN
1. Log into the VM and navigate to /vagrant/news_logs
2. Execute the following command
    ```
        python report.py
    ```
3. Output can be seen in the terminal window and in output.txt 
  <br/>

## CODE DESIGN
The code is separated into three functions to print the answer
to each of the three questions. The SQL statements are
broken down as described below:

1. What are the most popular three articles of all time?
    - The log and articles tables are joined so that the article title
    can be associated with each view
    - The two tables are joined based on the article slug matching the
    log path ending
    - The articles are grouped by the article id
    - The article title and count for each article (views) are selected
    from this joined table

2. Who are the most popular article authors of all time?
    - Similar to the previous SQL command, however the authors table
    is also joined with log and articles table
    - The articles and log tables are joined similarly to above, and
    the authors table is joined by the author id matching the article author
    - Unlike above, the articles are grouped by author
    - The author name and count for each author (author views) are selected
    from this joined table

3. On which days did more than 1% of requests lead to errors?
    - A subquery selects the count of all log entries (total) and a count of log
    entries where status is '404 NOT FOUND' (fail) per day
    - The outside query gets the date and calculates the failure percentage
    by dividing fail by total