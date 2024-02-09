import json

with open('cs2allItems.json', 'r', encoding='UTF-8') as file:
  jsonList = json.loads(file.read())
  stickerList = []
  
  for item in jsonList:
    stickerItem = {}
    stickerItem['name'] = item['name']
    stickerItem['iconUrl'] = item['image']
    stickerItem['rarity'] = item['name'].split()[-1] if ('(' and ')') in item['name'].split()[-1] else 'Paper'
    stickerItem['letters'] = item['name'].split('| ')[1].split('(')[0].replace(' ', '')
    stickerList.append(stickerItem)

with open('stickerAll.json', 'w', encoding='UTF-8') as outFile:
  json.dump(stickerList, outFile, indent=2)

print(len(stickerList))