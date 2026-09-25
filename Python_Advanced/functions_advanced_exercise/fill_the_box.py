def fill_the_box(height: int, length: int, width: int, *cubes) -> str:
    box_volume = height * length * width
    added_boxes = 0

    for cube in cubes:
        if cube == "Finish":
            break
        added_boxes += cube

    if box_volume > added_boxes:
        return f"There is free space in the box. You could put {box_volume - added_boxes} more cubes."
    return f"No more free space! You have {added_boxes - box_volume} more cubes."


print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
