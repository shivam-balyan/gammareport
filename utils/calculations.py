def percentage(
    numerator,
    denominator
):

    if denominator <= 0:
        return 0

    return round(
        numerator / denominator * 100,
        2
    )