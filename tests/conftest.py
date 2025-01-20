# import pytest

#EXAMPLES

# @pytest.fixture(scope="function", autouse=True)
# def before_each_test():
#     donothing = ""
#     # start_time = time.time()

# @pytest.fixture(scope="function", autouse=True)
# def after_each_test():
#     donothing = ""
#     # end_time = time.time()
#     # print(f"Test execution time is: {(end_time - start_time):.2f} seconds")

# @pytest.fixture(scope="session")
# def db_connection():
#     conn = connect_to_database()
#     yield conn
#     conn.close()