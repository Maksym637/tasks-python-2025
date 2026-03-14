#
# Problem description:
# You are given a list of logs as shown in the example below
# logs = [
#     "INFO: Test 1 was executed successfully",
#     "WARNING: Test 10 was skipped",
#     "INFO: Test 20 was executed successfully",
#     "ERROR: File not found",
#     "WARNING: Test 30 was skipped",
#     "ERROR: File not found",
#     "ERROR: Zero division error",
#     "INFO: Test 5 was executed successfully",
#     "ERROR: File not found",
# ]
# Your goal is to find a log with the "ERROR" prefix that occurs most frequently
#


def get_most_frequent_log(logs: list[str]) -> str:
    logs_frequency = {}
    max_log_count, max_log_name = 0, ""

    for log in logs:
        prefix, postfix = log.split(": ")

        if prefix == "ERROR":
            if postfix in logs_frequency:
                logs_frequency[postfix] += 1
            else:
                logs_frequency[postfix] = 1

    for log, frequence in logs_frequency.items():
        if frequence > max_log_count:
            max_log_count = frequence
            max_log_name = log

    return max_log_name


if __name__ == "__main__":
    logs = [
        "INFO: Test 1 was executed successfully",
        "WARNING: Test 10 was skipped",
        "INFO: Test 20 was executed successfully",
        "ERROR: File not found",
        "WARNING: Test 30 was skipped",
        "ERROR: File not found",
        "ERROR: Zero division error",
        "INFO: Test 5 was executed successfully",
        "ERROR: File not found",
    ]

    assert get_most_frequent_log(logs) == "File not found"
