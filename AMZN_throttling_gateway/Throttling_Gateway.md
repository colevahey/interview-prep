## Throttling Gateway
Non-critical requests for a transaction system are routed
through a throttling gateway to ensure that the network is
not choked by non-essential requests.

The gateway has the following limits:  
 - The number of transactions in any given second cannot
   exceed 3.  
 - The number of transactions in any given 10 second period
   cannot exceed 20. A ten-second period includes all
   requests arriving from any time max(1, T-9) to
   T (inclusive of both) for any valid time T.  
 - The number of transactions in any given minute cannot
   exceed 60. Similar to above, 1 minute is from max(1,
   T-59) to T.  

Any request that exceeds any of the above limits will be
dropped by the gateway. Given the times at which different
requests arrive sorted ascending, find how many requests
will be dropped.  

Note: Even if a request is dropped, it is still considered
for future calculations. Although, if a request is to be
dropped due to multiple violations, it is still counted only
once.  

### Solution Input
```Python3
n = 27
requestTime = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5,
5, 6, 6, 6, 7, 7, 7, 7, 11, 11, 11, 11]
```

### Solution Output
```Python3
# Request 1 - Not dropped
# Request 1 - Not dropped
# Request 1 - Not dropped
# Request 1 - Dropped (over 3 per second)
# ...
# Request 7 - Not dropped
# Request 7 - Dropped (over 20 in 10 seconds)
# Request 7 - Dropped (over 20 in 10 seconds)
# Request 7 - Dropped (over 20 in 10 seconds)
# Request 11 - Not dropped
# Request 11 - Dropped (over 20 in 10 seconds)
# Request 11 - Dropped (over 20 in 10 seconds)
# Request 11 - Dropped (over 20 in 10 seconds ALSO over 3 in one
second)

TOTAL: 7 drops
```
