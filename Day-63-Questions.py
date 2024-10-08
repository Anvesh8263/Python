#Nested List

if __name__ == '__main__':
    name_List = []
    score_List = []
    records = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
        name_List.append(name)
        score_List.append(score)
        
    score_List = list(set(score_List))
    score_List.sort()
    second_low = score_List[1]
    out = [i[0] for i in records if i[1]==second_low]
    out.sort()
    for i in out:
        print(i)
