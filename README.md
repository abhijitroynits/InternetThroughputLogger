# InternetThroughputLogger

Speedtest is a CLI for testing internet bandwidth using **speedtest.net**.

Because, XFinity Speed Test(https://speedtest.xfinity.com/) only displays instantaneous download throughputs, I assembled a script to collect these values over a period of time(12 minutes for 30 iterations).

The first step is to pip install the ```speedtest-cli``` in your python environment:
```
    pip install speedtest-cli
```

For gathering more bandwidth information, the provided Python script(```wifi_speed_tracker.py```) would take more time because in each iteration the system command:
```
  $speedtest-cli --simple
```
is run and the required (non-verbose) outputs are stored in a log file.

Also, the time taken to perform the ping(often in milliseconds) can't be ignored in the overall scheme of things. Thus, adding delay to the processing loop.

The output of the above command looks like:
```
  Ping: 22.941 ms
  Download: 29.43 Mbit/s
  Upload: 2.51 Mbit/s
```


***_Utility of the script_***: 
  > It can be used to compare and contrast the actual DL/UL speeds with those claimed by the ISPs. 
  
***_Miscellaneous_***:
  > Python libraries such as pandas, and matplotlib are used to form dataframe and visualization respectively. 

***_References_***:
  > https://github.com/sivel/speedtest-cli
  
***_Possibility of future work_***:
  > - Better data structures can be decided to improve space-time complexity.
  > - A mobile app (irrespective of WiFi service provider) can be developed to log upload/download throughputs over a period of time.
  > - Huge scope of QoS improvement by monitoring logs in WiFi hotspots such as train stations, airports, cafeterias etc.
