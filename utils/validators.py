MAX_FILE_SIZE = 10 * 1024 * 1024


def validate_file(file):

    if file is None:
        return True

    allowed_types = {
        "application/pdf",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    }

    if file.type not in allowed_types:
        return False

    if file.size > MAX_FILE_SIZE:
        return False

    return True


def validate_required(value):
    return bool(value)