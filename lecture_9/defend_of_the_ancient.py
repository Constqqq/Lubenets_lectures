from enum import StrEnum
from typing import Self
import random
from rich import print
import rich
import time

class Hero_names(StrEnum):
    ABADDON = "Abaddon"
    ALCHEMIST = "Alchemist"
    ANCIENT_APPARITION = "Ancient Apparition"
    ANTI_MAGE = "Anti-Mage"
    ARC_WARDEN = "Arc Warden"
    AXE = "Axe"
    BANE = "Bane"
    BATRIDER = "Batrider"
    BLOODSEEKER = "Bloodseeker"
    BOUNTY_HUNTER = "Bounty Hunter"
    BRISTLEBACK = "Bristleback"
    CENTAUR_WARRUNNER = "Centaur Warrunner"
    CHAOS_KNIGHT = "Chaos Knight"
    CRYSTAL_MAIDEN = "Crystal Maiden"
    DARK_SEER = "Dark Seer"
    DAZZLE = "Dazzle"
    DEATH_PROPHET = "Death Prophet"
    DOOM = "Doom"
    DRAGON_KNIGHT = "Dragon Knight"
    DROW_RANGER = "Drow Ranger"
    EARTHSHAKER = "Earthshaker"
    EMBER_SPIRIT = "Ember Spirit"
    ENCHANTRESS = "Enchantress"
    FACELESS_VOID = "Faceless Void"
    GRIMSTROKE = "Grimstroke"
    GYROCOPTER = "Gyrocopter"
    HUSKAR = "Huskar"
    INVOKER = "Invoker"
    JUGGERNAUT = "Juggernaut"
    KEEPER_OF_THE_LIGHT = "Keeper of the Light"
    LEGION_COMMANDER = "Legion Commander"
    LESHRAC = "Leshrac"
    LINA = "Lina"
    LION = "Lion"
    LUNA = "Luna"
    MAGNUS = "Magnus"
    MEDUSA = "Medusa"
    MIRANA = "Mirana"
    MORPHLING = "Morphling"
    NAGA_SIREN = "Naga Siren"
    NECROPHOS = "Necrophos"
    NIGHT_STALKER = "Night Stalker"
    PHANTOM_ASSASSIN = "Phantom Assassin"
    PHANTOM_LANCER = "Phantom Lancer"
    PUDGE = "Pudge"
    QUEEN_OF_PAIN = "Queen of Pain"
    SHADOW_FIEND = "Shadow Fiend"
    SNIPER = "Sniper"
    STORM_SPIRIT = "Storm Spirit"
    ZEUS = "Zeus"

class Hero:
    HERO_ROLES = {
        'ANTI_MAGE': 'CARRY',
        'PHANTOM_ASSASSIN': 'CARRY',
        'LUNA': 'CARRY',
        'FACELESS_VOID': 'CARRY',
        'JUGGERNAUT': 'CARRY',
        'MORPHLING': 'CARRY',
        'PHANTOM_LANCER': 'CARRY',
        'DROW_RANGER': 'CARRY',
        'MEDUSA': 'CARRY',
        'SHADOW_FIEND': 'MID',
        'STORM_SPIRIT': 'MID',
        'INVOKER': 'MID',
        'LINA': 'MID',
        'QUEEN_OF_PAIN': 'MID',
        'EMBER_SPIRIT': 'MID',
        'AXE': 'OFFLANE',
        'BRISTLEBACK': 'OFFLANE',
        'DOOM': 'OFFLANE',
        'LEGION_COMMANDER': 'OFFLANE',
        'NIGHT_STALKER': 'OFFLANE',
        'CENTAUR_WARRUNNER': 'OFFLANE',
        'CRYSTAL_MAIDEN': 'SUPPORT',
        'LION': 'SUPPORT',
        'KEEPER_OF_THE_LIGHT': 'SUPPORT',
        'DAZZLE': 'SUPPORT',
        'ANCIENT_APPARITION': 'SUPPORT',
        'BANE': 'SUPPORT',
        'ENCHANTRESS': 'HARD_SUPPORT',
        'GRIMSTROKE': 'HARD_SUPPORT',
        'DARK_SEER': 'HARD_SUPPORT',
        'NAGA_SIREN': 'HARD_SUPPORT'
    }
    
    def __init__(self, health_points = 100, name = None, damage = 10):
        health_variation = random.uniform(0.9, 1.5)
        damage_variation = random.uniform(0.9, 1.1)
        self.health_points = round(health_points * health_variation)
        self.max_health = self.health_points
        self.name = name if name else random.choice(list(Hero_names))
        self.damage = round(damage * damage_variation)
        self.role = self._determine_role()
        self.kills = 0
    
    def _determine_role(self):
        return self.HERO_ROLES.get(self.name.name, 'UNKNOWN')
    
    def attack(self, other):
        damage_variation = random.uniform(0.8, 1.2)
        actual_damage = round(self.damage * damage_variation)
        team_color = "green" if self.team == "Radiant" else "red"
        other_color = "green" if other.team == "Radiant" else "red"
        print(f"[{team_color}]{self.name}({self.role})[/] attacks [{other_color}]{other.name}({other.role})[/] for [cyan]{actual_damage}[/] damage")
        other.health_points -= actual_damage
        if other.health_points <= 0:
            print(f"[bold red]{other.name} has been killed by {self.name}![/]")
            other.health_points = 0
            self.kills += 1
            self.health_points = min(self.health_points + 10, self.max_health)

    def is_alive(self):
        return self.health_points > 0

class Team:
    REQUIRED_ROLES = ['CARRY', 'MID', 'OFFLANE', 'SUPPORT', 'HARD_SUPPORT']

    def __init__(self, name):
        self.name = name
        self.heroes = []
        self._create_team()
        for hero in self.heroes:
            hero.team = name
    
    def _get_random_hero_by_role(self, required_role):
        available_heroes = [
            name for name, role in Hero.HERO_ROLES.items()
            if role == required_role and name not in [h.name.name for h in self.heroes]
        ]
        if not available_heroes:
            return None
        hero_name = random.choice(available_heroes)
        return Hero(name=getattr(Hero_names, hero_name))

    def _create_team(self):
        for role in self.REQUIRED_ROLES:
            hero = self._get_random_hero_by_role(role)
            self.heroes.append(hero)

    def team_alive(self):
        return any(hero.is_alive() for hero in self.heroes)
    
    def battle_round(self, other_team):
        for hero in self.heroes:
            if not hero.is_alive():
                continue
            alive_enemies = [h for h in other_team.heroes if h.is_alive()]
            if not alive_enemies:
                return
            target = random.choice(alive_enemies)
            hero.attack(target)
    
    def get_team_power(self):
        if not self.heroes:
            return 0
        return sum(hero.health_points + hero.damage * 10 for hero in self.heroes)
    
    def __eq__(self, other):
        return abs(self.get_team_power() - other.get_team_power()) < 50
    
    def __lt__(self, other):
        return self.get_team_power() < other.get_team_power()
    
    def __le__(self, other):
        return self.get_team_power() <= other.get_team_power()
    
    def __str__(self):
        team_color = "green" if self.name == "Radiant" else "red"
      
        result = [f"[{team_color}]Team {self.name}[/]"]
        for hero in self.heroes:
            status = "[bold red]DEAD[/]" if not hero.is_alive() else f"{hero.health_points} HP"
            result.append(f"[{team_color}]- {hero.name} ({hero.role}) | {status} | Kills: {hero.kills}[/]")
        return "\n".join(result)

if __name__ == "__main__":
    team1 = Team("Radiant")
    team2 = Team("Dire")
    
    rich.print("[yellow]Команды до боя:[/]")
    rich.print(str(team1))
    rich.print(str(team2))
    time.sleep(2)
    
    rich.print("\n[yellow]Сравнение команд:[/]")
    time.sleep(1)
    if team1 == team2:
        rich.print("Команды примерно равны по силе")
    elif team1 < team2:
        rich.print("[red]Dire сильнее Radiant[/]")
    else:
        rich.print("[green]Radiant сильнее Dire[/]")
    time.sleep(1)
    
    rich.print(f"\n[green]Общая сила Radiant: {team1.get_team_power():.0f}[/]")
    rich.print(f"[red]Общая сила Dire: {team2.get_team_power():.0f}[/]")
    time.sleep(2)
    
    round_number = 1
    while team1.team_alive() and team2.team_alive():
        rich.print(f"\n[yellow]Файт {round_number}:[/]")
        time.sleep(0.5)
        team1.battle_round(team2)
        time.sleep(0.5)
        if team2.team_alive():
            team2.battle_round(team1)
        time.sleep(0.5)
        round_number += 1
        
    rich.print("\n[yellow]Игра окончена![/]")
    time.sleep(1)
    rich.print("\n[yellow]Статистика[/]")
    time.sleep(1)
    rich.print(str(team1))
    rich.print(str(team2))
    time.sleep(1)
    
    winner = "Radiant" if team1.team_alive() else "Dire"
    winner_color = "green" if winner == "Radiant" else "red"
    winning_team = team1 if team1.team_alive() else team2
    
    has_sf = any(hero.name.name == 'SHADOW_FIEND' and hero.is_alive() 
                 for hero in winning_team.heroes)
    
    if has_sf:
        number = 1000
        while number > 0:
            rich.print(f"[red]{number}[/]")
            time.sleep(0.1)
            number -= 7
    
    time.sleep(1)
    rich.print(f"\n[{winner_color}]{winner} wins![/]")

