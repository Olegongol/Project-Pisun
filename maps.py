from wall import Wall
from setting import BLOCK_SIDE

test_room = [
    "w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w",
    "w . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . w",
    "w . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . w",
    "w . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . w",
    "w . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . w",
    "w . . . . . . . . . . . . . . . . . w . . w . . . . . . . . . . . . . . . . . w",
    "w . . . . . . . . . . . . . . . . . w . . . . . . . . . . . . . . . . . . . . w",
    "w . . . . . . . . . . . . . . . . . w . . w . . . . . . . . . . . . . . . . . w",
    "w . . . . . . . . . . . . . w . w w w . w w w w w w . . . . . . . . . . . . . w",
    "w . . . . . . . . . . . . . . . . . . . . w . . . . . . . . . . . . . . . . . w",
    "w . . . . . . . . . . . . . . . . . w w . . . . . . . . . . . . . . . . . . . w",
    "w . . . . . . . . . . . . . w w . . w . . w w w w w . . . . . . . . . . . . . w",
    "w . . . . . . . . . . . . . . . . . w . . . . . . . . . . . . . . . . . . . . w",
    "w . . . . . . . . . . . . . . . . . w . . w . . . . . . . . . . . . . . . . . w",
    "w . . . . . . . . . . . . . . . . . w . . w . . . . . . . . . . . . . . . . . w",
    "w . . . . . . . . . . . . . . . . . . . . w . . . . . . . . . . . . . . . . . w",
    "w . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . w",
    "w . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . w",
    "w . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . w",
    "w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w w"]

text_maps = {
    "test_room": test_room
}

dict_rooms = {}
for name, text_map in text_maps.items():
    game_map = set()
    for y, line in enumerate(text_map):
        line = line.replace(" ", "")
        # if "w" in line:
        for x, symbol in enumerate(line):
            if symbol == "w":
                game_map.add(Wall("w", (x * BLOCK_SIDE, y * BLOCK_SIDE), (BLOCK_SIDE, BLOCK_SIDE)))
            # continue
        # for raw in line.split(";"):
            # key = raw[0].lower()
            # try:
                # params = [int(p) for p in raw[1:].split(",")]
                # if key == "c":
                    # game_map.add(Camera(key, (params[0], params[1]), (params[2], params[3], params[4], params[5])))
                # elif key == "p":
                    # game_map.add(Player(key, (params[0], params[1]), params[2], params[3], params[4]))
                # else:
                    # print(f"Невідома директива '{key}' у '{raw}'")
            # except ValueError:
                # print(f"Неможлива директива: '{raw}'")
                # continue
    dict_rooms[name] = game_map