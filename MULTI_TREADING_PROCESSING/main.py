import threading
import time
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import requests

# Indicates some task being done
def func(seconds):
  print(f"Sleeping for {seconds} seconds")
  time.sleep(seconds)
  return seconds

def main():
  time1 = time.perf_counter()
  # Normal Code
  # func(4) 
  # func(2)
  # func(1)
  
  
  # Same code using Threads
  t1 = threading.Thread(target=func, args=[4])
  t2 = threading.Thread(target=func, args=[2])
  t3 = threading.Thread(target=func, args=[1])
  t1.start()
  t2.start()
  t3.start()
  
  t1.join()
  t2.join()
  t3.join()
  # Calculating Time 
  time2 = time.perf_counter()
  print(time2 - time1)


def poolingDemo():
  with ThreadPoolExecutor() as executor:
    # future1 = executor.submit(func, 3)
    # future2 = executor.submit(func, 2)
    # future3 = executor.submit(func, 4)
    # print(future1.result())
    # print(future2.result())
    # print(future3.result())
    l = [3, 5, 1, 2]
    results = executor.map(func, l)
    for result in results:
      print(result)


poolingDemo()






# Function to download a file given its URL
def download_file(url):
    filename = url.split("/")[-1]
    print(f"Downloading {filename}")
    response = requests.get(url)
    
    with open(filename, 'wb') as file:
        file.write(response.content)
    
    print(f"{filename} downloaded")

# Function to demonstrate multithreading for file downloads
def download_files_multithreading():
    # List of file URLs to download
    file_urls = [
        "https://www.example.com/file1.html",
        "https://www.example.com/file2.html",
        "https://www.example.com/file3.html"
    ]

    # Using ThreadPoolExecutor to download files concurrently
    with ThreadPoolExecutor() as executor:
        executor.map(download_file, file_urls)

# Function to demonstrate multiprocessing for file downloads
def download_files_multiprocessing():
    # List of file URLs to download
    file_urls = [
        "https://www.example.com/file1.txt",
        "https://www.example.com/file2.txt",
        "https://www.example.com/file3.txt"
    ]

    # Using ProcessPoolExecutor to download files in parallel
    with ProcessPoolExecutor() as executor:
        executor.map(download_file, file_urls)

if __name__ == "__main__":
    print("Using Multithreading:")
    download_files_multithreading()
    
    print("\nUsing Multiprocessing:")
    download_files_multiprocessing()