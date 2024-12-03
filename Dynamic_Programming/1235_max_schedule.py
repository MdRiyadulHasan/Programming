from bisect import bisect_right
def jobScheduling(startTime, endTime, profit):
    jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
    dp = [0]*(len(jobs)+1)
    end_times = [0]+[job[1] for job in jobs] 
    print ("jobs", jobs)
    print("dp", dp)
    print("end_times", end_times)
    for i in range(1, len(jobs)+1):
        start, end, profit = jobs[i-1]
        index = bisect_right(end_times, start)-1
        dp[i] = max(dp[i-1], dp[index]+profit)
    return dp[-1]
    
startTime = [1, 2, 3, 3, 4, 6, 7, 8, 9, 10]
endTime =   [3, 5, 4, 6, 7, 9, 8, 11, 12, 13]
profit =    [50, 20, 30, 70, 60, 80, 40, 90, 100, 120]
print(jobScheduling(startTime, endTime, profit))
# jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
# Sorted jobs: [(1, 3, 50), (3, 4, 30), (2, 5, 20), (3, 6, 70), (4, 7, 60), (6, 9, 80), (7, 8, 40), (8, 11, 90), (9, 12, 100), (10, 13, 120)]
