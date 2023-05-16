from prometheus_client import Counter, Gauge, Histogram

# counters
pos_predictions_counter = Counter(
    name="pos_predictions",
    documentation="The number of positive predictions served.",
    labelnames=["api"],
)
neg_predictions_counter = Counter(
    name="neg_predictions",
    documentation="The number of negative predictions served.",
    labelnames=["api"],
)
predictions_counter = Counter(
    name="predictions",
    documentation="The number of predictions served.",
    labelnames=["api"],
)
true_pos_predictions_counter = Counter(
    name="true_pos_predictions",
    documentation="The number of true positive predictions served.",
    labelnames=["api"],
)
true_neg_predictions_counter = Counter(
    name="true_neg_predictions",
    documentation="The number of true negative predictions served.",
    labelnames=["api"],
)
false_pos_predictions_counter = Counter(
    name="false_pos_predictions",
    documentation="The number of false positive predictions served.",
    labelnames=["api"],
)
false_neg_predictions_counter = Counter(
    name="false_neg_predictions",
    documentation="The number of false negative predictions served.",
    labelnames=["api"],
)

# gauges
model_accuracy_gauge = Gauge(
    name="model_accuracy",
    documentation="The prediction accuracy of the model.",
    labelnames=["api"],
)

# histograms
response_time_histogram = Histogram(
    name="response_time_seconds",
    documentation="The response time for a request in seconds.",
    labelnames=["api"],
    buckets=(0.001, 0.002, 0.003, 0.01, 0.025, 0.05, 0.1, 0.5, 1, 1.5, 2),
)
