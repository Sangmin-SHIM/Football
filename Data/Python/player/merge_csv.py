import os

def make_batch_for_merge_csv_file(**kwargs):
    club_name = kwargs['club_name']
    
    batch = open(f'{club_name}/merge_csv.bat', 'w')
    batch.write(f'copy *.csv {club_name}_merged.csv')
    batch.close()

def execute_batch_for_merged_csv_file(**kwargs):
    club_name = kwargs['club_name']
    dirs_folder = f'{club_name}/'
    absolute_path = os.path.abspath(dirs_folder)

    os.chdir(absolute_path)
    os.system('merge_csv.bat')
    


