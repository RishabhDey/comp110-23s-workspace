"""File to define River class."""
__author__: str = "730558424"

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """Hi."""

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Hi."""
        copy_bears: list[Bear] = list()
        copy_fish: list[Fish] = list()
        for x in self.bears:
            if x.age <= 5:
                copy_bears.append(x)
        for x in self.fish:
            if x.age <= 3:
                copy_fish.append(x) 
        self.bears = copy_bears
        self.fish = copy_fish
        return None

    def bears_eating(self):
        """Hi."""
        for x in self.bears:
            if (len(self.fish) < 5):
                break
            else:
                x.eat(3)
                self.remove_fish(3)

        return None
    
    def remove_fish(self, amount: int):
        """Hi."""
        self.fish = self.fish[amount:]
        return None
    
    def check_hunger(self):
        """Hi."""
        copy_bears: list[Bear] = list()
        for x in self.bears:
            if x.hunger_score >= 0:
                copy_bears.append(x)
        self.bears = copy_bears        
        return None
        
    def repopulate_fish(self):
        """Hi."""
        init_fish = len(self.fish)
        for i in range(0, init_fish // 2 * 4):
            self.fish.append(Fish())
        return None
    
    def repopulate_bears(self):
        """Hi."""
        init_bears = len(self.bears)
        for i in range(0, init_bears // 2):
            self.bears.append(Bear())
        return None
    
    def view_river(self):
        """Hi."""
        nBears = len(self.bears)
        nFish = len(self.fish)

        print(f"~~~ Day {self.day}: ~~~") 
        print(f"Fish population: {nFish}") 
        print(f"Bear population: {nBears}")
        return None
    
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Hi."""
        for i in range(0, 7):
            self.one_river_day()
    
    
