import json

def get_trait(name: str) -> str:
  if '(Glitter)' in name:
    return 'Glitter'
  elif '(Foil)' in name:
    return 'Foil'
  elif '(Holo)' in name:
    return 'Holo'
  elif '(Gold)' in name:
    return 'Gold'
  elif '(Lenticular)' in name:
    return 'Lenticular'
  else:
    return 'Paper'
  
def get_rarity(name: str) -> str:
  if name == 'Default' or name == 'High Grade':
    return 'High Grade'
  else:
    return name

with open('cs2allItems.json', 'r', encoding='UTF-8') as file:
  jsonList = json.loads(file.read())
  stickerList = []
  
  for item in jsonList:
    stickerItem = {}
    stickerItem['name'] = item['name']
    stickerItem['iconUrl'] = item['image']
    stickerItem['trait'] = get_trait(item['name'])

    if 'rarity' in item:
      stickerItem['rarity'] = get_rarity(item['rarity']['name'])
      stickerItem['rarity_color'] = item['rarity']['color']

    stickerItem['text'] = []
    stickerItem['text'].append(dict(letters = item['name'].split('| ')[1].split('(')[0], rotation = 0))

    stickerList.append(stickerItem)

with open('stickerAll2.json', 'w', encoding='UTF-8') as outFile:
  json.dump(stickerList, outFile, indent=2)

print(len(stickerList))