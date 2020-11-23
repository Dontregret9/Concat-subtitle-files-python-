import re

def plus_time(time1,time2):#string like '00:10:54'
    if time1=="00:00:00":
        return time2
    elif time2=="00:00:00":
        return time1

    h1,m1,s1 = time1.split(':')
    h2,m2,s2 = time2.split(':')

    rs = int(s1)+int(s2)
    rm = int(m1) + int(m2)
    rh = int(h1)+int(h2)
    if rs > 59:
        rs = rs - 60
        rm += 1
    if rm > 59:
        rm = rm - 60
        rh +=1
    rss = rms = rhs = ''
    if rs < 10:
        rss = '0'+str(rs)
    else:
        rss = str(rs)
    if rm < 10:
        rms = '0'+str(rm)
    else:
        rms = str(rm)
    if rh <10:
        rhs = '0'+str(rh)
    else:
        rhs = str(rh)
    return rhs+':'+rms+':'+rss
    
def concat_srt(filenames,duration): # filenames is a list of .srt file in ordered
    result = []
    i=0; cur_time = "00:00:00"
    for f in filenames:
        file = open(f,'r')
        subs = file.readlines()
        cur_time = plus_time(cur_time,duration[i])
        print(f,duration[i],cur_time)
        i+=1
        for line in subs:
            isTime = re.findall("\d\d:\d\d:\d\d",line)
            if len(isTime) > 0:
                new_time0 = plus_time(isTime[0],cur_time)
                new_time1 = plus_time(isTime[1],cur_time)

                new_line = re.sub(isTime[0],new_time0,line)
                new_line = re.sub(isTime[1],new_time1,new_line)
                result.append(new_line)
            else:
                result.append(line)
                
        file.close()
    return result

# example
result = concat_srt(['1.srt','2.srt','3.srt'],# all filenames to concat (in ordered)
["00:00:00","00:04:25","00:31:59","00:37:48"])# durarion of those files (00:00:00 for the first fiel)
file = open("sub.srt","w")# filename for result file
file.writelines(result)
file.close()