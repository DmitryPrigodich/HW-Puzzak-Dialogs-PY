import time
from constructors.star_map_constructor import Star_Map_Constructor
from constructors.dia_seq_constructor import Dialog_Sequence_Constructor
from constructors.string_constructor import String_Data_Constructor

def _test_string_data():
    start_time = time.time()

    string_translator = String_Data_Constructor()
    assert string_translator.get_string_by_key("name_activity_001") == "TUTORIAL"

    end_time = time.time()
    print(f"String Data Converstion Test execution time is: {(end_time - start_time):.2f} seconds")

def _test_create_star_map():
    start_time = time.time()

    star_mapper = Star_Map_Constructor()
    star_mapper.set_star_map()
    star_mapper.write_json()
    star_mapper.write_data()

    end_time = time.time()
    print(f"Star Mapper execution time is: {(end_time - start_time):.2f} seconds")

def _test_get_star_name_by_coordinates():
    start_time = time.time()
    star_mapper = Star_Map_Constructor()
    assert star_mapper.get_star_system_by_coordinates("[-1240, -410]") == "TANOCHETLAN"

    end_time = time.time()
    print(f"Star Mapper execution time is: {(end_time - start_time):.2f} seconds")

def _test_dialog_seq():
    start_time = time.time()

    dia_seq_data = Dialog_Sequence_Constructor()
    dia_seq_data.set_dialogs()
    dia_seq_data.write_data()

    end_time = time.time()
    print(f"Dialog Seq Data Rec Test execution time is: {(end_time - start_time):.2f} seconds")

def test_dialog_seq_w_strings():
    start_time = time.time()

    dia_seq_data = Dialog_Sequence_Constructor()
    dia_seq_data.read_json()
    dia_seq_data.set_string_data()
    dia_seq_data.write_data_w_strings()

    end_time = time.time()
    print(f"Dialog Seq String Addition Test execution time is: {(end_time - start_time):.2f} seconds")

def _test_get_dialog_seq_by_head():
    start_time = time.time()

    dia_seq_data = Dialog_Sequence_Constructor()
    assert "Crew Member" in dia_seq_data.get_dialog_seq_string_by_header("qm_t0_scientist_Baaekh_A_1_end")

    end_time = time.time()
    print(f"Star Mapper execution time is: {(end_time - start_time):.2f} seconds")