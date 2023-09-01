Gunicorn
------------

![img.png](../.extras/img.png)
-------------

Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX.The documentation is hosted at https://docs.gunicorn.org.

Installation
------------

Gunicorn requires **Python 3.x >= 3.5**.

Install from PyPI::

     pip install gunicorn


Gunicorn Worker
-----
 A Gunicorn worker is a process that is responsible for handling HTTP requests for a Gunicorn application. Gunicorn can spawn multiple worker processes to handle a large number of requests.

Each worker process is responsible for handling a subset of the requests that are sent to the Gunicorn application. When a request is received, it is assigned to a worker process. The worker process then executes the code that corresponds to the request and returns a response.

The number of worker processes that Gunicorn spawns depends on the following factors:

* The number of available CPUs: Gunicorn will spawn one worker process for each available CPU.
* The amount of memory available: Gunicorn will not spawn more worker processes than the amount of memory that is available.
* The load on the application: Gunicorn will spawn more worker processes if the application is under heavy load.
Gunicorn workers can be configured to use different strategies for handling requests. The default strategy is to use a single thread per worker process. This means that each worker process can only handle one request at a time. However, Gunicorn also supports other strategies, such as using multiple threads per worker process or using gevent or eventlet.

The choice of strategy depends on the specific needs of the application. For example, if the application is CPU-intensive, then using multiple threads per worker process may be a better choice. However, if the application is I/O-intensive, then using gevent or eventlet may be a better choice.

#### Worker Calculation:

Here is the calculation:
```markdown
total_worker = (total_memory / worker_memory_per_process) * number_of_concurrent_requests

```

* Total memory = 1 GB = 1024 MB

* Worker memory per process = 256 MB

* Number of concurrent requests = 100

* total_worker = (1024 MB / 256 MB) * 100 = 4

This means that each worker process will have 256 MB of memory available to it. With 4 worker processes, you will have a total of 1024 MB of memory available to handle 100 requests per second.

It is important to note that this is just a general guideline. The actual number of worker processes you need may vary depending on the specific needs of your application. You may need to experiment to find the optimal number of worker processes for your application.

Here are some additional factors that you may want to consider when calculating the number of worker processes:

* The type of application you are running: Some applications are more CPU-intensive than others. If your application is CPU-intensive, you may need to increase the number of worker processes.

* The size of your application: Larger applications may require more worker processes to handle the load.

* The amount of traffic your application is expected to receive: If you expect your application to receive a lot of traffic, you may need to increase the number of worker processes.