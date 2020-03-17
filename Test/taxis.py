def min_num_taxis(requests):
    taxi = 1
    requests.sort()
    for i in range(len(requests)-1):
        flag = []
        for j in range(len(requests)-1):
            if i == j:
                pass
            else:
                try:
                    if len(set(range(requests[i][0],requests[i][1]+1)) & set(range(requests[j+1][0],requests[j+1][1]+1))) > 0:
                        flag.append(True)
                    else: flag.append(False)
                except:
                    pass
        #print(flag)
        if any(flag): taxi += 1
    return taxi

print(min_num_taxis([(1, 4), (5, 7), (6, 9)]))
print(min_num_taxis([(3, 7), (1, 4), (5, 7), (6, 9),(4, 10)]))
print(min_num_taxis([(1, 4), (5, 7), (6, 9)]))
