import time
from constructors.star_map_constructor import Star_Map_Constructor


def _test_create_star_map():
    start_time = time.time()

    star_mapper = Star_Map_Constructor()
    star_mapper.get_systems_from_constellation_data()
    star_mapper.get_systems_from_star_system_data()

    star_mapper.write_json()
    star_mapper.write_data()

    end_time = time.time()
    print(f"Star Mapper execution time is: {(end_time - start_time):.2f} seconds")

def test_get_star_name_by_coordinates():
    start_time = time.time()
    star_mapper = Star_Map_Constructor()
    assert star_mapper.get_star_system_by_coordinates("[-1240, -410]") == "TANOCHETLAN"

    end_time = time.time()
    print(f"Star Mapper execution time is: {(end_time - start_time):.2f} seconds")