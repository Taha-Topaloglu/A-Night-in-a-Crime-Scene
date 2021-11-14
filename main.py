def convert(my_str):
    my_list = list(my_str.split(' '))
    return my_list
values = {}
times = {}
weights = {}
ids = []

f = open('crime_scene.txt')
my_lines = f.readlines()
stripped_lines = [line.strip() for line in my_lines]
f.close()

N = int(stripped_lines[1])
w = int(convert(stripped_lines[0])[0])
t = int(convert(stripped_lines[0])[1])

if N != 1:
    for n in range(2,N+2):
        content = convert(stripped_lines[n])
        values[content[0]] = content[3]
        times[content[0]]  = content[2]
        weights[content[0]] = content[1]
        ids.append(content[0])
else:
    n = 2
    content = convert(stripped_lines[n])
    values[content[0]] = content[3]
    times[content[0]] = content[2]
    weights[content[0]] = content[1]
    ids.append(content[0])


def list_sum(my_lst,wanted = None):
    if wanted == None:
        wanted = 0
    if len(my_lst) == 0:
        return wanted
    wanted = wanted + int(my_lst[0])
    return list_sum(my_lst[1:],wanted)


def my_weights(my_lst,wanted = None):
    if wanted == None:
        wanted = []
    if len(my_lst) == 0:
        return wanted
    wanted.append(weights[my_lst[0]])
    return my_weights(my_lst[1:],wanted)


def my_times(my_lst,wanted = None):
    if wanted == None:
        wanted = []
    if len(my_lst) == 0:
        return wanted
    wanted.append(times[my_lst[0]])
    return my_times(my_lst[1:],wanted)


def my_values(my_lst,wanted = None):
    if wanted == None:
        wanted = []
    if len(my_lst) == 0:
        return wanted
    wanted.append(values[my_lst[0]])
    return my_values(my_lst[1:],wanted)


def control1(my_lst):   #  output 1
    if list_sum(my_weights(my_lst)) <= w:
        return True
    else:
        return False

def control2(my_lst):   #  output 2
    if list_sum(my_times(my_lst)) <= t:
        return True
    else:
        return False


def control3(my_lst):   #  output 3
    if list_sum(my_weights(my_lst)) <= w and list_sum(my_times(my_lst)) <= t:
        return True
    else:
        return False


def creating_lst(my_lst,for_lst,wanted = None):
    if wanted == None:
        wanted = []
    if len(for_lst) == 0:
        return wanted
    wanted.append([my_lst[-1]]+for_lst[0])
    return creating_lst(my_lst,for_lst[1:],wanted)


def combinations(my_lst):
    if my_lst:
       sonuc = combinations(my_lst[:-1])
       wanted = sonuc + creating_lst(my_lst,sonuc)
       return wanted
    else:
       return [[]]

def comb_control1(my_lst,i = None,wanted = None):   #  output 1
    if i == len(combinations(my_lst)):
        return wanted
    if i == None:
        i = 0
    if wanted == None:
        wanted = []
    if control1(combinations(my_lst)[i]):
        wanted.append(combinations(my_lst)[i])
    else:
        pass
    i += 1
    return comb_control1(my_lst,i,wanted)

def comb_control2(my_lst,i = None,wanted = None):   #  output 2
    if i == len(combinations(my_lst)):
        return wanted
    if i == None:
        i = 0
    if wanted == None:
        wanted = []
    if control2(combinations(my_lst)[i]):
        wanted.append(combinations(my_lst)[i])
    else:
        pass
    i += 1
    return comb_control2(my_lst,i,wanted)


def comb_control3(my_lst,i = None,wanted = None):   #  output 3
    if i == len(combinations(my_lst)):
        return wanted
    if i == None:
        i = 0
    if wanted == None:
        wanted = []
    if control3(combinations(my_lst)[i]):
        wanted.append(combinations(my_lst)[i])
    else:
        pass
    i += 1
    return comb_control3(my_lst,i,wanted)


def biggest_subset(my_lst,max = None,wanted_lst = None):
    if len(my_lst) == 0:
        return wanted_lst
    if max == None:
        max = 0
    if wanted_lst == None:
        wanted_lst = []
    if list_sum(my_values(my_lst[0])) > max:
        max = list_sum(my_values(my_lst[0]))
        wanted_lst = my_lst[0]
    else:
        pass
    return biggest_subset(my_lst[1:],max,wanted_lst)

ideal_list1 = biggest_subset(comb_control1(ids))
ideal_list2 = biggest_subset(comb_control2(ids))
ideal_list3 = biggest_subset(comb_control3(ids))


sorted_output1 = []  # w
sorted_output2 = []  # t
sorted_output3 = []  # t and w

while ideal_list1:
    my_min = ideal_list1[0]
    for evidence in ideal_list1:
        if int(evidence) < int(my_min):
            my_min = evidence
    sorted_output1.append(my_min)
    ideal_list1.remove(my_min)


while ideal_list2:
    my_min = ideal_list2[0]
    for evidence in ideal_list2:
        if int(evidence) < int(my_min):
            my_min = evidence
    sorted_output2.append(my_min)
    ideal_list2.remove(my_min)


while ideal_list3:
    my_min = ideal_list3[0]
    for evidence in ideal_list3:
        if int(evidence) < int(my_min):
            my_min = evidence
    sorted_output3.append(my_min)
    ideal_list3.remove(my_min)

def _output1(my_lst):
    f1 = open('solution_part1.txt','w+')
    f1.write(str(list_sum(my_values(my_lst)))+'\n')
    for evidence in my_lst:
        f1.write(str(evidence)+' ')
    f1.close()


def _output2(my_lst):
    f2 = open('solution_part2.txt','w+')
    f2.write(str(list_sum(my_values(my_lst)))+'\n')
    for evidence in my_lst:
        f2.write(str(evidence)+' ')
    f2.close()


def _output3(my_lst):
    f3 = open('solution_part3.txt','w+')
    f3.write(str(list_sum(my_values(my_lst)))+'\n')
    for evidence in my_lst:
        f3.write(str(evidence)+' ')
    f3.close()


_output1(sorted_output1)
_output2(sorted_output2)
_output3(sorted_output3)











