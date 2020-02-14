from bestiary.models import Dungeon, SecretDungeon, Level, Monster
from bestiary.parse import game_data


def scenarios():
    # Extract names from world map strings by filtering out names that are not for scenarios
    scenario_names = {
        row['region id']: game_data.strings.WORLD_MAP_DUNGEON_NAMES[row['world id']] for row in game_data.tables.WORLD_MAP.values() if row['type'] == 3
    }

    for scenario_id, raw in game_data.tables.SCENARIO_LEVELS.items():
        region_id = raw['region id']
        dungeon, created = Dungeon.objects.update_or_create(
            com2us_id=region_id,
            category=Dungeon.CATEGORY_SCENARIO,
            defaults={
                'name': scenario_names.get(region_id, 'UNKNOWN')
            }
        )

        if created:
            print(f'Added new dungeon {dungeon}')

        level, created = Level.objects.update_or_create(
            dungeon=dungeon,
            difficulty=raw['difficulty'],
            floor=raw['stage no'],
            defaults={
                'energy_cost': raw['energy cost'],
                'frontline_slots': raw['player unit slot'],
                'backline_slots': None,
                'total_slots': raw['player unit slot'],
            }
        )

        if created:
            print(f'Added new level for {dungeon} - {level}')


def rift_raids():
    for master_id, raw in game_data.tables.RIFT_RAIDS.items():
        dungeon, created = Dungeon.objects.update_or_create(
            com2us_id=raw['raid id'],
            category=Dungeon.CATEGORY_RIFT_OF_WORLDS_RAID,
            defaults={
                'name': 'Rift Raid',
            }
        )

        if created:
            print(f'Added new dungeon {dungeon.name} - {dungeon.slug}')

        level, created = Level.objects.update_or_create(
            dungeon=dungeon,
            floor=raw['stage id'],
            defaults={
                "energy_cost": raw['cost energy'],
                "frontline_slots": 4,
                "backline_slots": 4,
                "total_slots": 6,
            },
        )

        if created:
            print(
                f'Added new level for {dungeon.name} - {level.get_difficulty_display() if level.difficulty is not None else ""} B{1}')


def elemental_rifts():
    for master_id, raw in game_data.tables.ELEMENTAL_RIFT_DUNGEONS.items():
        if raw['enable']:
            # Dungeon name is name of the boss
            name = game_data.strings.MONSTER_NAMES[raw['unit id']]
            dungeon, created = Dungeon.objects.update_or_create(
                com2us_id=master_id,
                category=Dungeon.CATEGORY_RIFT_OF_WORLDS_BEASTS,
                defaults={
                    'name': name
                }
            )

            if created:
                print(f'Added new dungeon {dungeon.name} - {dungeon.slug}')

            # Create a single level referencing this dungeon
            level, created = Level.objects.update_or_create(
                dungeon=dungeon,
                floor=1,
                defaults={
                    'energy_cost': raw['cost energy'],
                    'frontline_slots': 4,
                    'backline_slots': 4,
                    'total_slots': 6,
                }
            )

            if created:
                print(
                    f'Added new level for {dungeon.name} - {level.get_difficulty_display() if level.difficulty is not None else ""} B{1}')


def secret_dungeons():
    for instance_id, raw in game_data.tables.SECRET_DUNGEONS.items():
        monster_id = raw['summon pieces']
        monster = Monster.objects.get(com2us_id=monster_id)

        dungeon, created = SecretDungeon.objects.update_or_create(
            com2us_id=instance_id,
            category=SecretDungeon.CATEGORY_SECRET,
            defaults={
                'monster': monster,
                'name': f'{monster.get_element_display()} {monster.name} Secret Dungeon',
            }
        )

        if created:
            print(f'Added new secret dungeon {dungeon.name} - {dungeon.slug}')

        # Create a single level referencing this dungeon
        level, created = Level.objects.update_or_create(
            dungeon=dungeon,
            floor=1,
            defaults={
                'energy_cost': 3,
                'frontline_slots': 5,
                'backline_slots': None,
                'total_slots': 5,
            }
        )

        if created:
            print(f'Added new level for {dungeon.name} - {level.get_difficulty_display() if level.difficulty is not None else ""} B{1}')
