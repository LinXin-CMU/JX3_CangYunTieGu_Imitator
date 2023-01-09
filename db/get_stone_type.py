# coding: utf-8
# author: LinXin
from jx3_stone import stone


_Attrs = []
_Attr_ID = {}
dwUnEnabledSlots = {'Spunk', 'Spirit', 'Magic', 'Lunar', 'Solar', 'Neutral', 'Poison', 'Decritical', 'Dodge', 'Life', 'Mana', 'Tough', 'Therapy', 'Threat', 'Resist', 'Strength', 'Agility', 'WeaponDamage', 'AllTypeCritical', 'Haste'}

for dwID, dwStoneDatas in stone[6].items():
    attrs = set(i for i in dwStoneDatas['_Attrs'] if i is not None)

    for attr in attrs:
        for other_slot in dwUnEnabledSlots:
            if other_slot in attr:
                break

        else:   # 如果没有被break就检查下一个属性，否则会在外层也被break
            continue

        break

    else:
        if attrs not in _Attrs:
            _Attrs.append(attrs)
            _attr_id = len(_Attrs) - 1
            _Attr_ID[_attr_id] = [dwID]
        else:
            for index, i in enumerate(_Attrs):
                if i == attrs:
                    _Attr_ID[index].append(dwID)


print(*(f"{i}\n" for i in _Attrs))
print(len(_Attrs))
print(*(f"{k}: {v}\n" for k, v in _Attr_ID.items()))

