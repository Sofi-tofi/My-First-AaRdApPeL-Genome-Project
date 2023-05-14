# My-First-AaRdApPeL-Genome-Project
SRA entries for Genomic projects in Solanum tuberosum Every time that the webpage updates the following information is loaded: Run_Accession Study_Accession Study_Title Library_Layout Instrument LibraryLayout Public_URL ReleaseDate Tissue Age Organism Genotype


SRA entries for Genomic projects in Solanum tuberosum
Every time that the webpage updates the following information is loaded:
Run_Accession Study_Accession Study_Title Library_Layout Instrument LibraryLayout Public_URL ReleaseDate Tissue Age Organism Genotype

Dependencies:

django
pandas
pysradb
datetime
itertools

An env folder is avaliable:
my_papa_world

The django project was tested in Ubuntu 22

Instructions:

download the folder env
open a shell in env folder
activate the env with:
source my_papa_world/bin/activate

download the folder my_tennis_club
open a shell in my_tennis_club folder
update the database with:
python3 manage.py updatemodels
run the app with:
python3 manage.py runserver

Open a new browser window and type [127.0.0.1:8000] (http://127.0.0.1:8000/)
