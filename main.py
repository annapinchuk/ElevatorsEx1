import json
import sys
import csv
from callforelevator import callforelevator
from building import building
from elevator import elevator


def j_to_building(building_path):
    with open(building_path) as f:
        data = json.load(f)
        elevators = [elevator(
            e["_id"],
            e["_speed"],
            e["_minFloor"],
            e["_maxFloor"],
            e["_closeTime"],
            e["_openTime"],
            e["_startTime"],
            e["_stopTime"])
            for e in data["_elevators"]]
        building_ = building(data["_minFloor"],
                             data["_maxFloor"],
                             elevators)
        f.close()
    return building_


def allocate_call_for_elev(call, max_length, building):
    length_of_the_call = abs(int(call.dest) - int(call.src))
    building.sort_speed_elev(call)
    section_size = max_length / len(building.elevators)
    index_of_elev = int(length_of_the_call / section_size)
    # out of bounds patch
    if index_of_elev >= len(building.elevators) - 1:
        index_of_elev = index_of_elev - 1
    call.elev = building.elevators[index_of_elev].ID
    return call


def csv_to_calls(path):
    calls_of_elev = []
    with open(path) as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row_csv in csv_reader:
            call = callforelevator(row_csv[1], row_csv[2], row_csv[3], row_csv[4], -1)
            calls_of_elev.append(call)
        file.close()
    return calls_of_elev


def csv_output_writer(out_path, calls_for_elev):
    with open(out_path, 'w', newline='') as file:
        writer = csv.writer(file)
        for call in calls_for_elev:
            row = call.for_out()
            writer.writerow(row)
        file.close()


if __name__ == '__main__':
    cmd_args = sys.argv[1:]
    building_path = cmd_args[0]
    calls_path = cmd_args[1]
    out_path = cmd_args[2]

    newbuilding_ = j_to_building(building_path)
    allcalls_ = csv_to_calls(calls_path)
    max_interval = max([abs(x.dest - x.src) for x in allcalls_])
    for call_ in allcalls_:
        call_ = allocate_call_for_elev(call_, max_interval,newbuilding_)
    csv_output_writer(out_path, allcalls_)