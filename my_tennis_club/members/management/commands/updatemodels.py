from django.core.management.base import BaseCommand
import pandas as pd
from members.models import Member
from pysradb.sraweb import SRAweb
from pysradb.search import SraSearch
import datetime
from datetime import date
from itertools import chain


class Command(BaseCommand):
    help = 'import booms'
    
    def add_arguments(self, parser):
        pass
    #Clean database
    Member.objects.all().delete()    
    
    def handle(self, *args, **options):  
        #new entries in SRA that query the search "Solanum tuberosum",and GENOMIC source.
        #the entries will be added to a seed database conteined in test_clean.csv
        #new entries are defided by date, from the last uptdate until the current day
        df = pd.read_csv('test_clean.csv')
        #dates for update
        today = date.today()
        d1 = today.strftime("%d-%m-%Y")
        d2 = datetime.date(2023, 5, 10)
        d2 = d2.strftime("%d-%m-%Y")
        #Search engine in SRA with pysradb package
        instance = SraSearch(0, 1000, organism="Solanum tuberosum", source="GENOMIC", publication_date = f'{d2}:{d1}') 
        instance.search()
        df1 = instance.get_df()
        # if there are update add the entris to the database if not pass
        if len(df1.index) != 0 :
            flatten_list = list(chain.from_iterable(df1.values.tolist()))
            db = SRAweb()
            df0 = db.sra_metadata(flatten_list, detailed=True)
            df = pd.concat([df, df0])
        else:
            df            
        #Sort results per date, new entries in the top part
        df.sort_values("public_date")
        
        #Adding values to the model=SQLdatabase
        for A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11 in zip (df.run_accession, df.study_accession, df.study_title, df.library_layout, df.instrument_model, df.public_url, df.public_date, df.tissue, df.age, df.scientific_name, df.genotype):
            models = Member(run=A1, bioproject=A2, biosample=A3, assay_type=A4, center_name=A5, experiment=A6, instrument=A7, library_layout=A8, library_selection=A9, library_source=A10, org = A11)
            models.save()
