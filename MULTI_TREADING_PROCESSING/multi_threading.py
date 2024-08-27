import requests
from threading import Thread 
from time import perf_counter

class Downloader(Thread):
    def __init__(self,url,destination):
        super().__init__()
        self.url = url
        self.destination = destination

    def run(self):
        download_file(self.url,self.destination)

def download_file(path, url):
    start_time = perf_counter()  # Record the start time

    response = requests.get(url)
    with open(path, 'wb') as file:
        file.write(response.content)
    
    end_time = perf_counter()  # Record the end time
    print(f"File for {url} downloaded in {end_time - start_time:.2f} seconds")  # Calculate and print the time taken


if __name__ == '__main__':
    urls = [
        "https://example.com/file1.txt",
        "https://example.com/file2.txt",
        "https://example.com/file3.txt"
    ]
    destinations = [
        "file1.txt",
        "file2.txt",
        "file3.txt"
    ]

    threads = []
    for path,url in zip(destinations,urls):
        thread = Downloader(path,url)
        thread.start()
        threads.append(thread)

    for th in threads:
        th.join()

    print(f"All files Downloaded")

    
