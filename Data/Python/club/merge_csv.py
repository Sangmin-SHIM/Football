from .csv_custom import FILE_CLUB_PATH
import os

def make_batch_for_merge_csv_file(**kwargs):
    league_name = kwargs['league_name']
    
    batch = open(f'{league_name}/merge_csv.bat', 'w')
    batch.write(f'copy *.csv {league_name}_merged.csv')
    batch.close()

def execute_batch_for_merged_csv_file(**kwargs):
    league_name = kwargs['league_name']
    dirs_folder = f'{league_name}/'
    absolute_path = os.path.abspath(dirs_folder)

    os.chdir(absolute_path)
    os.system('merge_csv.bat')
    


