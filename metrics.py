from prometheus_client import Counter, Gauge, Histogram

# counters
http_requests_counter = Counter(
    name="http_requests",
    documentation="Total number of http requests.",
    labelnames=["api", "restaurant_name"],
)
pos_predictions_counter = Counter(
    name="pos_predictions",
    documentation="Total number of positive predictions.",
    labelnames=["api", "restaurant_name"],
)
neg_predictions_counter = Counter(
    name="neg_predictions",
    documentation="Total number of negative predictions.",
    labelnames=["api", "restaurant_name"],
)
predictions_counter = Counter(
    name="predictions",
    documentation="Total number of predictions.",
    labelnames=["api", "restaurant_name"],
)
true_pos_predictions_counter = Counter(
    name="true_pos_predictions",
    documentation="Total number of true positive predictions.",
    labelnames=["api", "restaurant_name"],
)
true_neg_predictions_counter = Counter(
    name="true_neg_predictions",
    documentation="Total number of true negative predictions.",
    labelnames=["api", "restaurant_name"],
)
false_pos_predictions_counter = Counter(
    name="false_pos_predictions",
    documentation="Total number of false positive predictions.",
    labelnames=["api", "restaurant_name"],
)
false_neg_predictions_counter = Counter(
    name="false_neg_predictions",
    documentation="Total number of false negative predictions.",
    labelnames=["api", "restaurant_name"],
)

# gauges
model_accuracy_gauge = Gauge(
    name="model_accuracy",
    documentation="Prediction accuracy of the model.",
    labelnames=["api"],
)

# histograms
response_time_histogram = Histogram(
    name="response_time_seconds",
    documentation="Response time of requests in seconds.",
    labelnames=["api"],
    buckets=(0.001, 0.002, 0.003, 0.01, 0.025, 0.05, 0.1, 0.5, 1, 1.5, 2),
)
