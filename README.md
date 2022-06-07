# csv_dictionary

![Logo FLinguenheld](https://raw.githubusercontent.com/FLinguenheld/csv_dictionary/main/forelif.png "Pouet")


****
### Description

Allow to scrap 'The Online Plain Text English Dictionary' :  
> https://www.mso.anu.edu.au/~ralph/OPTED/  

This script will create one csv file per letter in **files/** with the delimiter '_'.  
One line per word with the same type (all meanings will be regrouped in the same line and separated by the delimiter).

****
### Installation
Clone this repo :

    git clone https://github.com/FLinguenheld/csv_dictionary

Create a virtual environment :

    python -m venv env

Activate it :

    source env/bin/activate

Install requests :

    pip install -r requirement.txt

****
### Launching

    python scrap_dictionary.py
