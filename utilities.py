def validate_string(input_str, field_name):
    if not input_str.strip():
        raise ValueError(f"{field_name} cannot be empty.")
    return input_str.strip()

def validate_phone(input_phone):
    if not input_phone.isdigit():
        raise ValueError("Phone number must be numeric.")
    return input_phone
