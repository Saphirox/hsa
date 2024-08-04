## Description
Stress testing using Siege

In this application we run siege on endpoint that create a note for todo
Server adds the note content into elasticsearch and mongo


| Concurrency | Availability | Avg response time | Throughput   | 
|-------------|--------------|-------------------|--------------|
| 10          | 100%         | 0.05 sec          | 2.28 MB/sec  |
| 25          | 100%         | 0.05 sec          | 11.14 MB/sec |
| 50          | 100%         | 0.06 sec          | 42.14 MB/sec |
| 100         | 100%         | 0.23              | 53.94 MB/sec |


