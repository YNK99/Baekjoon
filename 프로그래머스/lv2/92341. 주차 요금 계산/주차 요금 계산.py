import math
def solution(fees, records):
    sum_time = {c.split()[1]:0 for c in records}
    sort_time = {}
    in_cars = {c.split()[1]:[] for c in records}
    out_cars = {c.split()[1]:[] for c in records}
    for record in records:
        if record.split()[2] == "IN":
            in_cars[record.split()[1]].append(record.split()[0])
        else:
            out_cars[record.split()[1]].append(record.split()[0])
    for i, j, k, t in zip(in_cars.keys(), in_cars.values(), out_cars.keys(), out_cars.values()):
        if len(j) != len(t):
            out_cars[k].append("23:59")

    for i, j, k, t in zip(in_cars.keys(), in_cars.values(), out_cars.keys(), out_cars.values()):
        for a, b in zip(j, t):
            times = (int(b.split(":")[0])*60 + int(b.split(":")[1])) - (int(a.split(":")[0])*60 + int(a.split(":")[1]))
            sum_time[i] += abs(times)
    for i, j in sum_time.items():
        if j <= fees[0]:
            sort_time[i] = fees[1]
        else:
            sort_time[i] = fees[1] + math.ceil((j-fees[0])/fees[2]) * fees[3]
    sort_time = sorted(sort_time.items())
    answer = ([c[1] for c in sort_time])
    return answer