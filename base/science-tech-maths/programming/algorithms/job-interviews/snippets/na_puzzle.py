"""NA puzzle solver.

In the village, a rich man had 4 daughters,
including one who had just turned 18, so the rich man opened a show find son-in-law.
He gave the boys a topic to test their skills: “We have four rooms for four girls.
Each room has a different color. Each child hates a different food, and likes a different flower.

a) Quynh is in the third room
b) Linh hates shrimp paste
c) Ngoc is in purple room
d) Han is next to the blue room
e) Person that likes orchids is in the pink room
f) Person that likes peach blossom, is not near the person that likes apricot blossom
g) Person that hates bitter is not not near person who hates shrimp paste
h) Person that hates pea is in the yellow room
i) Person in the first room couldn't smell DURIAN

So who likes lotus flowers?"
"""

from dataclasses import dataclass
from enum import Enum
from itertools import permutations

from tqdm import tqdm


class RoomColor(Enum):  # noqa
    PURPLE = 1
    BLUE = 2
    YELLOW = 3
    PINK = 4


class PersonNames(Enum):  # noqa
    Quynh = 1
    Linh = 2
    Ngoc = 3
    Han = 4


class Flower(Enum):  # noqa
    LOTUS = 1
    PEACH_BLOSSOM = 2
    APRICOT_BLOSSOM = 3
    ORCHIDS = 4


class Food(Enum):  # noqa
    SHRIMP_PASTE = 1
    BITTER = 2
    PEA = 3
    DURIAN = 4


@dataclass
class Person:  # noqa
    name: PersonNames
    fav_flower: Flower
    hated_food: Food


@dataclass
class Room:  # noqa
    color: RoomColor
    person: Person


def is_valid_config(rooms: list[Room]):  # noqa
    """
    a) Quynh is in the third room
    b) Linh hates shrimp paste
    c) Ngoc is in purple room
    d) Han is next to the blue room
    e) Person that likes orchids is in the pink room
    f) Person that likes peach blossom, is not near the person that likes apricot blossom
    g) Person that hates bitter is not not near person who hates shrimp paste
    h) Person that hates pea is in the yellow room
    i) Person in the first room couldn't smell DURIAN
    """
    return all(
        [
            rooms[2].person.name == PersonNames.Quynh,  # a
            any(  # b
                room.person.name == PersonNames.Linh and room.person.hated_food == Food.SHRIMP_PASTE
                for room in rooms
            ),
            any(  # c
                room.color == RoomColor.PURPLE and room.person.name == PersonNames.Ngoc
                for room in rooms
            ),
            any(  # d
                room.color == RoomColor.BLUE
                and (
                    ((i - 1 >= 0) and rooms[i - 1].person.name == PersonNames.Han)
                    or ((i + 1 < len(rooms)) and rooms[i + 1].person.name == PersonNames.Han)
                )
                for i, room in enumerate(rooms)
            ),
            any(  # e
                room.color == RoomColor.PINK and room.person.fav_flower == Flower.ORCHIDS
                for room in rooms
            ),
            any(  # f
                room.person.fav_flower == Flower.PEACH_BLOSSOM
                and not (
                    ((i - 1 >= 0) and rooms[i - 1].person.fav_flower == Flower.APRICOT_BLOSSOM)
                    or (
                        (i + 1 < len(rooms))
                        and rooms[i + 1].person.fav_flower == Flower.APRICOT_BLOSSOM
                    )
                )
                for i, room in enumerate(rooms)
            ),
            any(  # g
                room.person.hated_food == Food.BITTER
                and not (
                    ((i - 1 >= 0) and rooms[i - 1].person.hated_food == Food.SHRIMP_PASTE)
                    or (
                        (i + 1 < len(rooms)) and rooms[i + 1].person.hated_food == Food.SHRIMP_PASTE
                    )
                )
                for i, room in enumerate(rooms)
            ),
            any(  # h
                room.color == RoomColor.YELLOW and room.person.hated_food == Food.PEA
                for room in rooms
            ),
            rooms[0].person.hated_food == Food.DURIAN,  # i
        ]
    )


def rooms_gen():  # noqa
    for room_colors in permutations(RoomColor):
        for person_names in permutations(PersonNames):
            for flowers in permutations(Flower):
                for foods in permutations(Food):
                    yield [
                        Room(
                            color=room_colors[0],
                            person=Person(
                                name=person_names[0],
                                fav_flower=flowers[0],
                                hated_food=foods[0],
                            ),
                        ),
                        Room(
                            color=room_colors[1],
                            person=Person(
                                name=person_names[1],
                                fav_flower=flowers[1],
                                hated_food=foods[1],
                            ),
                        ),
                        Room(
                            color=room_colors[2],
                            person=Person(
                                name=person_names[2],
                                fav_flower=flowers[2],
                                hated_food=foods[2],
                            ),
                        ),
                        Room(
                            color=room_colors[3],
                            person=Person(
                                name=person_names[3],
                                fav_flower=flowers[3],
                                hated_food=foods[3],
                            ),
                        ),
                    ]


def main():  # noqa
    for rooms_config in tqdm(rooms_gen()):
        if is_valid_config(rooms_config):
            print(rooms_config)
            found_person = [
                room for room in rooms_config if room.person.fav_flower == Flower.LOTUS
            ][0].person.name
            print(f"The person who likes lotus flower is: {found_person}")
            break


if __name__ == "__main__":
    main()
