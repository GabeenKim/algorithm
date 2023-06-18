def solution(players, callings):
    dict_list = dict(zip(players,range(len(players))))

    for i in callings:
        idx = dict_list[i]
        frt_idx = idx - 1
        
        players[idx], players[frt_idx] = players[frt_idx],players[idx]
        
        dict_list[players[idx]] = idx
        dict_list[players[frt_idx]] = frt_idx
    
    return players
