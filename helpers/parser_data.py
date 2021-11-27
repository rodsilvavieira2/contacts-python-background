def parse_dict_to_tuple(data: dict) -> tuple:
    return tuple(data.values())


def parser_null_values(data: dict) -> str:
    values = {
        k: v for k,
        v in data.items() if v is not None
    }

    str_data = ''

    for k, v in values.items():
        str_data += f"{k} = '{v}', "

    return str_data.rstrip(", ")
