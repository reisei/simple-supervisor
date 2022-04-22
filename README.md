# Test task

## Description

This tool is a "daemon supervisor", it should check that the process is running at all times and starts it in case is down.

## Parameters

* Seconds to wait between attempts to restart service
* Number of attempts before giving up
* Name of process to supervise
* Check interval in seconds (obsolete, as Subprocess module waits for process to finish)

## Output

bash -c "sleep 1 && exit 0"
```
$ python3 ./supervisor.py --process "bash -c 'sleep 1 && exit 0'" --count 3 --seconds 3
2022-04-22 11:06:39,964 - INFO - Starting process bash -c 'sleep 1 && exit 0'
2022-04-22 11:06:40,967 - INFO - Process bash -c 'sleep 1 && exit 0' ends normally
2022-04-22 11:06:40,967 - INFO - Restarting in 3 seconds...
2022-04-22 11:06:43,971 - INFO - Starting process bash -c 'sleep 1 && exit 0'
2022-04-22 11:06:44,977 - INFO - Process bash -c 'sleep 1 && exit 0' ends normally
2022-04-22 11:06:44,978 - INFO - Restarting in 3 seconds...
2022-04-22 11:06:47,979 - INFO - Starting process bash -c 'sleep 1 && exit 0'
2022-04-22 11:06:48,988 - INFO - Process bash -c 'sleep 1 && exit 0' ends normally
2022-04-22 11:06:48,988 - INFO - Restarting in 3 seconds...
2022-04-22 11:06:51,991 - INFO - Starting process bash -c 'sleep 1 && exit 0'
2022-04-22 11:06:52,999 - INFO - Process bash -c 'sleep 1 && exit 0' ends normally
```

bash -c "sleep 5 && exit 0"
```
$ python3 ./supervisor.py --process "bash -c 'sleep 5 && exit 0'" --count 3 --seconds 3
2022-04-22 11:07:45,822 - INFO - Starting process bash -c 'sleep 5 && exit 0'
2022-04-22 11:07:50,826 - INFO - Process bash -c 'sleep 5 && exit 0' ends normally
2022-04-22 11:07:50,826 - INFO - Restarting in 3 seconds...
2022-04-22 11:07:53,827 - INFO - Starting process bash -c 'sleep 5 && exit 0'
2022-04-22 11:07:58,832 - INFO - Process bash -c 'sleep 5 && exit 0' ends normally
2022-04-22 11:07:58,832 - INFO - Restarting in 3 seconds...
2022-04-22 11:08:01,835 - INFO - Starting process bash -c 'sleep 5 && exit 0'
2022-04-22 11:08:06,840 - INFO - Process bash -c 'sleep 5 && exit 0' ends normally
2022-04-22 11:08:06,840 - INFO - Restarting in 3 seconds...
2022-04-22 11:08:09,843 - INFO - Starting process bash -c 'sleep 5 && exit 0'
2022-04-22 11:08:14,847 - INFO - Process bash -c 'sleep 5 && exit 0' ends normally
```

bash -c "sleep 1 && exit 1"
```
$ python3 ./supervisor.py --process "bash -c 'sleep 1 && exit 1'" --count 3 --seconds 3
2022-04-22 11:09:05,617 - INFO - Starting process bash -c 'sleep 1 && exit 1'
2022-04-22 11:09:06,621 - ERROR - Process bash -c 'sleep 1 && exit 1' ends abnormally
2022-04-22 11:09:06,621 - INFO - Restarting in 3 seconds...
2022-04-22 11:09:09,623 - INFO - Starting process bash -c 'sleep 1 && exit 1'
2022-04-22 11:09:10,630 - ERROR - Process bash -c 'sleep 1 && exit 1' ends abnormally
2022-04-22 11:09:10,630 - INFO - Restarting in 3 seconds...
2022-04-22 11:09:13,633 - INFO - Starting process bash -c 'sleep 1 && exit 1'
2022-04-22 11:09:14,640 - ERROR - Process bash -c 'sleep 1 && exit 1' ends abnormally
2022-04-22 11:09:14,640 - INFO - Restarting in 3 seconds...
2022-04-22 11:09:17,643 - INFO - Starting process bash -c 'sleep 1 && exit 1'
2022-04-22 11:09:18,652 - ERROR - Process bash -c 'sleep 1 && exit 1' ends abnormally
```

sh -c 'sleep 10 && exit 1'
```
$ python3 ./supervisor.py --process "sh -c 'sleep 10 && exit 1'" --count 3 --seconds 3
2022-04-22 11:09:43,153 - INFO - Starting process sh -c 'sleep 10 && exit 1'
2022-04-22 11:09:53,156 - ERROR - Process sh -c 'sleep 10 && exit 1' ends abnormally
2022-04-22 11:09:53,156 - INFO - Restarting in 3 seconds...
2022-04-22 11:09:56,159 - INFO - Starting process sh -c 'sleep 10 && exit 1'
2022-04-22 11:10:06,164 - ERROR - Process sh -c 'sleep 10 && exit 1' ends abnormally
2022-04-22 11:10:06,164 - INFO - Restarting in 3 seconds...
2022-04-22 11:10:09,165 - INFO - Starting process sh -c 'sleep 10 && exit 1'
2022-04-22 11:10:19,169 - ERROR - Process sh -c 'sleep 10 && exit 1' ends abnormally
2022-04-22 11:10:19,169 - INFO - Restarting in 3 seconds...
2022-04-22 11:10:22,171 - INFO - Starting process sh -c 'sleep 10 && exit 1'
2022-04-22 11:10:32,175 - ERROR - Process sh -c 'sleep 10 && exit 1' ends abnormally
```

bash -c "if [ -f lock ]; then exit 1; fi; sleep 10 && touch lock && exit 1"
```
$ python3 ./supervisor.py --process "bash -c 'if [ -f lock ]; then exit 1; fi; sleep 10 && touch lock && exit 1'" --count 3 --seconds 3
2022-04-22 11:12:05,018 - INFO - Starting process bash -c 'if [ -f lock ]; then exit 1; fi; sleep 10 && touch lock && exit 1'
2022-04-22 11:12:15,024 - ERROR - Process bash -c 'if [ -f lock ]; then exit 1; fi; sleep 10 && touch lock && exit 1' ends abnormally
2022-04-22 11:12:15,024 - INFO - Restarting in 3 seconds...
2022-04-22 11:12:18,027 - INFO - Starting process bash -c 'if [ -f lock ]; then exit 1; fi; sleep 10 && touch lock && exit 1'
2022-04-22 11:12:18,032 - ERROR - Process bash -c 'if [ -f lock ]; then exit 1; fi; sleep 10 && touch lock && exit 1' ends abnormally
2022-04-22 11:12:18,032 - INFO - Restarting in 3 seconds...
2022-04-22 11:12:21,035 - INFO - Starting process bash -c 'if [ -f lock ]; then exit 1; fi; sleep 10 && touch lock && exit 1'
2022-04-22 11:12:21,038 - ERROR - Process bash -c 'if [ -f lock ]; then exit 1; fi; sleep 10 && touch lock && exit 1' ends abnormally
2022-04-22 11:12:21,038 - INFO - Restarting in 3 seconds...
2022-04-22 11:12:24,039 - INFO - Starting process bash -c 'if [ -f lock ]; then exit 1; fi; sleep 10 && touch lock && exit 1'
2022-04-22 11:12:24,044 - ERROR - Process bash -c 'if [ -f lock ]; then exit 1; fi; sleep 10 && touch lock && exit 1' ends abnormally
```

bash -c "if [ -f lock ]; then exit 1; fi; sleep 10 && touch lock && exit 1" (with 1 attempt only)
```
$ python3 ./supervisor.py --process "bash -c 'if [ -f lock ]; then exit 1; fi; sleep 10 && touch lock && exit 1'" --count 1 --seconds 3
2022-04-22 11:13:03,866 - INFO - Starting process bash -c 'if [ -f lock ]; then exit 1; fi; sleep 10 && touch lock && exit 1'
2022-04-22 11:13:13,871 - ERROR - Process bash -c 'if [ -f lock ]; then exit 1; fi; sleep 10 && touch lock && exit 1' ends abnormally
2022-04-22 11:13:13,871 - INFO - Restarting in 3 seconds...
2022-04-22 11:13:16,873 - INFO - Starting process bash -c 'if [ -f lock ]; then exit 1; fi; sleep 10 && touch lock && exit 1'
2022-04-22 11:13:16,877 - ERROR - Process bash -c 'if [ -f lock ]; then exit 1; fi; sleep 10 && touch lock && exit 1' ends abnormally
```

