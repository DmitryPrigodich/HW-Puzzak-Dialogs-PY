import time
import logging

from pages.all_page_bak import All_Pages_Backup

logger = logging.getLogger(__name__)

# def test_benchmark(page, benchmark):
#     def run_test():
#         # test_constellation_data(page)
#         # test_event_data(page)
#         test_quest_line_data(page)
#     benchmark(run_test)

# @pytest.mark.asyncio
# async def _test_async(page):
#     start_time = time.time()
#     end_time = time.time()
#     print(f"Event Data search time is: {(start_time-end_time):.2f} seconds")


def _test_backup_all_data(page):
    #do not run until you want to reset all data: it took 90 minutes to save
    start_time = time.time()

    backuper = All_Pages_Backup()
    backuper.backup_everything(page)

    end_time = time.time()
    print(f"Backup All Test execution time is: {(end_time - start_time):.2f} seconds")