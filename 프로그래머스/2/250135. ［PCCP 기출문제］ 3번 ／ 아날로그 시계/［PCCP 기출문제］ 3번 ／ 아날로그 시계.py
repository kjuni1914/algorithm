def solution(h1, m1, s1, h2, m2, s2):

    nows = s1 % 60
    nowm = (m1*60 + s1) % 3600
    nowh = (h1%12*3600 + (m1 * 60 + s1)) % 43200
    
    alarm = []
    time = tosec(h1, m1, s1, h2, m2, s2)
    cnt = 1
    
    if nows / 60 == nowm / 60 or nowm / 60 == nowh / 12 or nows / 60 == nowh / 12:
        alarm.append(cnt)
    
    while cnt <= time:
        tmps=nows+1
        tmpm=nowm+1
        tmph=nowh+1
        
        if nows/60<nowm/3600 and tmps/60>=tmpm/3600:
            alarm.append(cnt)
        if nows/60<nowh/43200 and tmps/60>=tmph/43200:
            if tmph != 43200:
                alarm.append(cnt)

        if tmps == 60:
            tmps = 0
        if tmpm == 3600:
            tmpm = 0
        if tmph == 43200:
            tmph = 0
        
        nows = tmps
        nowm = tmpm
        nowh = tmph
        
        cnt+=1
        
    answer = len(alarm)
    return answer

def tosec(h1, m1, s1, h2, m2, s2):
    if m2 < m1:
        h2-=1
        m2+=60
    if s2 < s1:
        m2-=1
        s2+=60
    
    return (h2-h1)*3600 + (m2-m1)*60 + (s2-s1)