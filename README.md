# HOMEWORLD MOBILE SCENARIO RESTORATION PROJECT

In this small project I was fulfilling 3 goals:

* Learning Python
* Learning Pytest and Playwright
* Assembling Homeworld Mobile scenario together

## PROJECT HISTORY
At first, I was planning to directly get all the data from the site `https://hwm.puzzak.page/`, that's why I've chosen Python\ Pytest\ Playwright combination. But seeing how slow is the process, and potential unreliability of a private host, I've created a script to download all the data (it took several hours) and to work 
with local files.

In the end, though trials, data research and errors, I've recombined the data into readable document in MD format so that it's easier to work with directly and it's readable directly from GitHub page.

Currently, project is done, as the main goal fullfilled, and HWM Events can be read as a scenario; for Campaign Chapter manual rearrangement of dialog parts is still required as those texts were received in `automatical` way. I will get it later.


## PROJECT STRUCTURE

* **tests**
    * `test_hwm_db_pages.py` - collection of tests to check data retrieved from the web-pages (`/pages`)
    * `test_hwm_db_bak.py` - a test to get all the data from the web-pages at once (requires few hours) (`/json_bak`)
    * `test_hwm_db_jsons.py` - collection of tests to check data made by data constructors (`/constructors`)
    * `test_hwm_db_refill_data.py` - collection of tests to rearrange initial data (`/json_bak`) into json to work with (`/json`) and data to research (`/data`)
    * `test_hwm_db_scenarios.py` - 2 tests to create final data (`/data_final`) with HWM persistent campaign Chapters and eventual Events
* **pages**
    * `all_page_bak.py` - contains a code to download all open data from `https://hwm.puzzak.page/`
    * `base_page.py` - base class for a folder
    * _other_ - all other classes containing code to collect things from their subpages
* **constructors**
    * `star_map_constructor.py` - should be launched first via refill data test, as it generates json used in `constructor_base`
    * `constructor_base.py` - base class for the folder
    * _other_ - constuctors responsible for their part of the data
* **json**
    * `mission_dialogs_rearranged.json` - manually created file to rearrange dialogs from missions in chronological order
    * _other_ - automatically created files (see `test_hwm_db_refill_data.py`) to ease data manipulation (`_set_data` / `write_json` functions)
* **data**
    * automatically created files (see `test_hwm_db_refill_data.py`) to ease reading (`write_data` function)
* **data_final**
    * final goal of the project - formatted Event and Campaign readable scenarios
* base folder:
    * `conftest.py` - use it to run any code before/after tests
    * `constants.py` - a place to store constants used across the project
    * `utils.py` - a place of small utility functions used across the project

Constructors and pages classes are maximally unified to 
    * `save_data()`/`set_data()` - get data for further use
    * `read_json()`- read data from saved jsons
    * `write_json()` - write data to .json
    * `write_data()` - write data to .md-file to read it in a more pleasant way (cleaned up from unrequired information)
    * `write_data_tmp()` - write data to .md-file with all the tags (to check if some info missing)
    * get_%object%() - get some data
    * and others


## PROJECT COMMANDS

* Install IDE (VSCode, for example)
* Install Python, Git (if you haven't)
* Create virtual environment in terminal
    ```python -m venv venv```
* Activate virtual environment in terminal
    ```venv\Scripts\activate```
* Install Playwright (if you'd want to play with web-pages):
    ```
    pip install playwright
    playwright install
    ```
* Install Pytest:
    ```pip install pytest```
* Run tests (any of these):
    * python tests/test_hwm_db_bak.py
    * python tests/test_hwm_db_jsons.py
    * python tests/test_hwm_db_pages.py
    * python tests/test_hwm_db_refill_data.py
    * python tests/test_hwm_db_scenarios.py

Every function inside starting with `test_` would be executed, so exclude the test, just add a symbol, underscore (_) for example.

## NOTES
Well, I've found few things, like
* old Glossary with mentioning PvP Sarassian Sea/Wars thing with 3 corporation from Iyatequa, Yaot, Tanoch
* Strike mission "Down the Well", not implemented, but dialogs ready, so, I've added it instead of unfinished amasum2024 event that initially was reusing already existing missions
* Strike mission "Raid004", not implemented, but mentioning mysterious Gary the Xelassii, Yaotian, that had to help you somehow in Sijin Lighthouse
* Vaygr unimplemented cinematic about their betrayal and running away with Cazoma
* Gideon being named Raab S'jet initially
* and maybe others, but don't recall anymore