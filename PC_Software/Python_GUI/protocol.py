def build_ping():
    return "@PING?;"


def build_status():
    return "@STATUS?;"


def build_id():
    return "@ID?;"


def build_pic_safe():
    return "@PIC:SAFE?;"


def build_mode(mode):
    return f"@MODE:{mode.upper()};"