def calculate_metrics(
        completed,
        missed,
        profit):

    total_tasks = (
        len(completed)
        +
        len(missed)
    )

    completion_rate = 0

    if total_tasks > 0:

        completion_rate = (
            len(completed)
            /
            total_tasks
        ) * 100

    return {

        "Total Tasks":
            total_tasks,

        "Completed Tasks":
            len(completed),

        "Missed Tasks":
            len(missed),

        "Completion Rate":
            round(
                completion_rate,
                2
            ),

        "Total Profit":
            profit
    }