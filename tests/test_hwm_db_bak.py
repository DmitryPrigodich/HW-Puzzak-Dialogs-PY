import time

from pages.all_page_bak import All_Pages_Backup

#do not run until you want to reset all data: it took 90 minutes to save
def _test_backup_all_data(page):
    start_time = time.time()
    test_all_data = All_Pages_Backup()
    test_all_data.backup_everything(page)
    end_time = time.time()
    print(f"Save All Test execution time is: {(end_time - start_time):.2f} seconds")