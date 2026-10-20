def classify_books(*args, **kwargs) -> str:
    fiction = {}
    non_fiction = {}

    for genre, title in args:
        if genre == "fiction":
            fiction[title] = ''
        elif genre == "non_fiction":
            non_fiction[title] = ''

    for isbn, title in kwargs.items():
        if title in fiction:
            fiction[title] = isbn
        elif title in non_fiction:
            non_fiction[title] = isbn

    output = []
    if fiction:
        output.append("Fiction Books:")
        for title, isbn in sorted(fiction.items(), key=lambda x: x[1]):
            output.append(f"~~~{isbn}#{title}")
    if non_fiction:
        output.append("Non-Fiction Books:")
        for title, isbn in sorted(non_fiction.items(), key=lambda x: x[1], reverse=True):
            output.append(f"***{isbn}#{title}")

    return '\n'.join(output)


print(classify_books(
    ("fiction", "Brave New World"),
    ("fiction", "The Catcher in the Rye"),
    ("fiction", "1984"),
    FICCITRZZ="The Catcher in the Rye",
    FIC1984XX="1984",
    FICBNWYYY="Brave New World"
))
