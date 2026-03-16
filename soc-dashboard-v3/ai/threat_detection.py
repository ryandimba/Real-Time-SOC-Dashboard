def detect_threat(log):

    log = log.lower()

    if "malware" in log:
        return "High"

    elif "failed login" in log:
        return "Medium"

    else:
        return "Low"