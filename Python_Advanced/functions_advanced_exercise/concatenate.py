def concatenate(*args: str, **kwargs: dict) -> str:
    output_string = ''.join(args)

    for key, value in kwargs.items():
        if key in output_string:
            output_string = output_string.replace(key, value)

    return output_string


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
