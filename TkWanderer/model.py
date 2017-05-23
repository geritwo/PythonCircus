import csv

class AreaMap:

    def __init__(self):
        self.area_floorplan = []

        with open('./mapdata.csv', 'r', newline='') as f:
            f_reader=csv.reader(f, delimiter=',')
            for line in f_reader:
                self.area_floorplan.append(line)

        self.area_dimensions = [len(self.area_floorplan), len(self.area_floorplan[0])]
        # NOTE: rows, columns (y, x!)

        self.valid_character_positions = []

        for row in range(self.area_dimensions[0]):
            for column in range(self.area_dimensions[1]):
                if int(self.area_floorplan[row][column]) == 0:
                    self.valid_character_positions += [[column, row]]

    def get_area_floorplan(self):
        return self.area_floorplan

    def get_area_dimensions(self):
        return self.area_dimensions

    def get_valid_character_positions(self):
        return self.valid_character_positions

class Hero:

    def __init__(self):
        self.hero_position = [0, 0]
        self.hero_level = 1
        self.max_hp = 10
        self.hp = 10
        self.dp = 6
        self.sp = 3

    def get_hero_position(self):
        return self.hero_position

    def set_hero_position(self, alteration):
        self.hero_position[0] += alteration[0]
        self.hero_position[1] += alteration[1]

    def get_hero_stats(self):
        stats_output = [self.hero_level, self.max_hp, self.hp, self.dp, self.sp]
        return stats_output

class Boss:

    def __init__(self, enemy_type, position, hp, dp, sp):
        self.enemy_type = enemy_type
        self.position = position
        self.hp = hp
        self.dp = dp
        self.sp = sp

    def set_position(self, alteration):
        self.position[0] += alteration[0]
        self.position[1] += alteration[1]

    def get_position(self):
        return self.position

    def get_enemy_type(self):
        return self.enemy_type

    def get_enemy_stats(self):
        stats_output = [self.hp, self.dp, self.sp]
        return stats_output

class Skeleton:

    def __init__(self, enemy_type, position, hp, dp, sp, has_key):
        self.enemy_type = enemy_type
        self.position = position
        self.hp = hp
        self.dp = dp
        self.sp = sp
        self.has_key = has_key

    def set_position(self, alteration):
        self.position[0] += alteration[0]
        self.position[1] += alteration[1]

    def get_position(self):
        return self.position

    def get_enemy_type(self):
        return self.enemy_type

    def get_enemy_stats(self):
        stats_output = [self.hp, self.dp, self.sp]
        return stats_output
