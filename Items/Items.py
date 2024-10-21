class Items:
    def __init__(self, name, durability, current_stack, max_stack, hunger_points, health_points, damage_buff, hardness, weight, description):
        self.name = name
        self.durability = durability
        self.current_stack = current_stack
        self.max_stack = max_stack
        self.hunger_points = hunger_points
        self.health_points = health_points
        self.damage_buff = damage_buff
        self.hardness = hardness
        self.weight = weight
        self.description = description
        
class Bacon(Items):
    def __init__(self, name, durability, current_stack, max_stack, hunger_points, health_points, damage_buff, hardness, weight, description):
        super().__init__(name="Bacon", durability=2, current_stack=1, max_stack=50, hunger_points=15, health_points=3, damage_buff=0, hardness=0, weight=1, description="Harvest from local pig. Its soggy and slightly cold to the touch.")