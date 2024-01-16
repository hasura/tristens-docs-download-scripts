import requests
import time
import numpy as np

# GraphQL queries and endpoint
query1 = """
query Python($thing: Int) {
  p2: pythonTursoAlbum(
    where: {AlbumId: {_gt: $thing}, _and: [{AlbumId: {_lt: 1000}}], _not: {AlbumId: {_gte: 900}}}
    limit: 100
  ) {
    AlbumId
    ArtistId
    Title
    Artist {
      ArtistId
      Name
    }
  }
}
"""

query2 = """
query Typescript($thing: Int) {
  p2: tursoAlbum(
    where: {AlbumId: {_gt: $thing}, _and: [{AlbumId: {_lt: 1000}}], _not: {AlbumId: {_gte: 900}}}
    limit: 100
  ) {
    AlbumId
    ArtistId
    Title
    Artist {
      ArtistId
      Name
    }
  }
}
"""

url = "http://localhost:8000/graphql"


# Function to send the request and time it
def send_request(query):
    start_time = time.time()
    response = requests.post(url, json={'query': query, 'variables': {'thing': 5}})
    end_time = time.time()
    return end_time - start_time


# Running the requests 1000 times for each query
num_requests = 3000
[send_request(query1) for _ in range(5)]
times_query1 = [send_request(query1) for _ in range(num_requests)]
[send_request(query2) for _ in range(5)]
times_query2 = [send_request(query2) for _ in range(num_requests)]

# Calculating average time, various percentiles, and requests per second
total_time_query1 = sum(times_query1)
total_time_query2 = sum(times_query2)
average_time_query1 = np.mean(times_query1)
average_time_query2 = np.mean(times_query2)
p99_query1 = np.percentile(times_query1, 99)
p99_query2 = np.percentile(times_query2, 99)
p95_query1 = np.percentile(times_query1, 95)
p95_query2 = np.percentile(times_query2, 95)
p90_query1 = np.percentile(times_query1, 90)
p90_query2 = np.percentile(times_query2, 90)
p50_query1 = np.percentile(times_query1, 50)
p50_query2 = np.percentile(times_query2, 50)
requests_per_second_query1 = num_requests / total_time_query1
requests_per_second_query2 = num_requests / total_time_query2

diff_avg_time = (average_time_query2 - average_time_query1) * 1000
diff_p99 = (p99_query2 - p99_query1) * 1000
diff_p95 = (p95_query2 - p95_query1) * 1000
diff_p90 = (p90_query2 - p90_query1) * 1000
diff_p50 = (p50_query2 - p50_query1) * 1000

# Printing the results
print(f"Requests sent: {num_requests}")
print(
    f"Query 1 Python Connector - Average Time: {average_time_query1:.5f} seconds, P99: {p99_query1:.5f} seconds, P95: {p95_query1:.5f} seconds, P90: {p90_query1:.5f} seconds, P50: {p50_query1:.5f} seconds, Requests/Sec: {requests_per_second_query1:.2f}")
print(
    f"Query 2 Typescript Connector - Average Time: {average_time_query2:.5f} seconds, P99: {p99_query2:.5f} seconds, P95: {p95_query2:.5f} seconds, P90: {p90_query2:.5f} seconds, P50: {p50_query2:.5f} seconds, Requests/Sec: {requests_per_second_query2:.2f}")
print(
    f"Differences (Query 2 - Query 1) in milliseconds - Avg Time: {diff_avg_time:.2f} ms, P99: {diff_p99:.2f} ms, P95: {diff_p95:.2f} ms, P90: {diff_p90:.2f} ms, P50: {diff_p50:.2f} ms")
