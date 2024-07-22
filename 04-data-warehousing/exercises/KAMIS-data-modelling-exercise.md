### Module 4 Assignment- Design a Star Schema

For this module, we covered the fundamentals of data modelling, `normalization and denormalization` and their respective use cases. We also looked at the `Kimball Approach (Star)`  and compared that with the `Imnon Approach (Snowflake)`

In this directory `phoenix-etl-workshop-q2 > 04-data-warehousing > data`  there is a dataset named `sample_agric_commodities.csv`. The file contains data scraped from this site https://amis.co.ke/site/market.

*You are to design two data models, a Star Schema and a snowflake schema. You are to the write a data pipeline that ingests the csv file, cleans the data, transform the data according to your star schema and load it to your Supabase instance*

**Deliverables**

- [ ] two png diagram, one for the star, another for the snowflake schema *(use diagramming tools like drawio, or lucidchart)*

- [ ] code for your working data pipeline

- [ ] link to your supabase instance 

##### Submissions

In this directory, `phoenix-etl-workshop-q2 > 04-data-warehousing > submissions`, create a folder with the name format, <04-YOUR_FIRST_NAME-SUBMISSION>. 

For instance if my name is 'James Kamau', your folder for this week's module should be named `04-james-submission`. Your folder should have three subfolders. `> erd-diagrams, kamis-data-pipeline, supabase-link.`  

In the erd diagrams folder, submit your two diagrams for the star and snowflake schema. Your pipeline code should go in the kamis-data-pipeline. In the supabase link, submit either a markdown file or a text file containing a link to your remote supabase instance.

##### Additional Resource

[Dimensional Modeling - YouTube](https://www.youtube.com/watch?v=lWPiSZf7-uQ&t=2s)[Dimensional Modeling - YouTube](https://www.youtube.com/watch?v=lWPiSZf7-uQ&t=2s)

Go through the above video, it will be of great help when designing your star and snowflake schema.

##### NOTE : Code Quality

For your data pipeline, marks will be scored according to the quality of your code.

1. Write modular code

2. Write consistent documentation (use docstrings)

3. implement error handling using try-except blocks in your functions. 

4. Implement logging in your functions
