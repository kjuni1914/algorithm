def solution(data, ext, val_ext, sort_by):
    enum = 0
    if ext == "code": enum = 0
    elif ext == "date": enum = 1
    elif ext == "maximum": enum = 2
    else: enum = 3
    snum = 0
    if sort_by == "code": snum = 0
    elif sort_by == "date": snum = 1
    elif sort_by == "maximum": snum = 2
    else: snum = 3
    data = [i for i in data if i[enum] < val_ext]
    answer = sorted(data, key = lambda x: x[snum])
    return answer