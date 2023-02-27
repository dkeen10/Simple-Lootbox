"""
Simple Lootbox program
"""

from random import randint, sample

odds = {"common": 70, "rare": 90, "epic": 100}
commonRewards = ["sword", "axe", "mace"]
rareRewards = ["rare sword", "rare axe", "race mace"]
epicRewards = ["epic sword", "epic axe", "epic mace"]


def rollLoot(rarity):
    """
    Determine the result for one loot box opening using a cumulative frequency approach.
    """
    roll = randint(1, 100)
    if roll <= odds["common"]:
        return sample(commonRewards, 1)
    elif odds["common"] < roll <= odds["rare"]:
        return sample(rareRewards, 1)
    return sample(epicRewards, 1)


def main():
    print(rollLoot())


if __name__ == "__main__":
    main()
