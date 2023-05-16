from prometheus_client import Counter, Gauge, Histogram

# counters
pos_predictions_counter = Counter(
    'pos_predictions',
    'The number of positive predictions served',
    ['api']
)
neg_predictions_counter = Counter(
    'neg_predictions',
    'The number of negative predictions served',
    ['api']
)
predictions_counter = Counter(
    'predictions',
    'The number of predictions served',
    ['api']
)
true_pos_predictions_counter = Counter(
    'true_pos_predictions',
    'The number of true positive predictions served',
    ['api']
)
true_neg_predictions_counter = Counter(
    'true_neg_predictions',
    'The number of true negative predictions served',
    ['api']
)
false_pos_predictions_counter = Counter(
    'false_pos_predictions',
    'The number of false positive predictions served',
    ['api']
)
false_neg_predictions_counter = Counter(
    'false_neg_predictions',
    'The number of false negative predictions served',
    ['api']
)

# gauges
model_accuracy_gauge = Gauge(
    'model_accuracy',
    'The prediction accuracy of the model',
    ['api']
)

# histograms
response_time_histogram = Histogram(
    name='response_time_seconds',
    documentation="The response time for a request in seconds",
    labelnames=['api'],
    buckets=(0.001, 0.002, 0.003, 0.01, 0.025, 0.05, 0.1, 0.5, 1)
)

