import json

# This works and takes around 0.1s to read, generate and save to file
def create_starts_with_index(stickers):
    parts_to_stickers = {}
    for sticker in stickers:
        for text_info in sticker["text"]:
            label = text_info["letters"].lower().replace(' ', '')
            for i in range(len(label)):
                part = label[:len(label)-i]
                if part not in parts_to_stickers:
                    parts_to_stickers[part] = []
                parts_to_stickers[part].append(sticker['name'])

    return parts_to_stickers

def find_combinations(word_starts_with: str, sticker_index, depth=0, used_stickers=None):
    if word_starts_with == '':
        # done
        return used_stickers
    
    if depth == 5:
        # failed
        return None
    
    if used_stickers is None:
        used_stickers = []

    possible_combinations = []

    for i in range(len(word_starts_with), 1, -1):
        current_word_start = word_starts_with[:i]
        if current_word_start not in sticker_index:
            continue
        stickers_that_start_with = sticker_index[current_word_start]
        for sticker in stickers_that_start_with:
            word_part_next_search = word_starts_with.replace(current_word_start, '', 1)
            new_used_stickers = used_stickers + [sticker]
            result = find_combinations(word_part_next_search, sticker_index, depth + 1, new_used_stickers)
            if result is not None:
                possible_combinations.append(result)

    if possible_combinations:
        return possible_combinations
    else:
        return None

# Beispielaufruf
if __name__ == '__main__':
    with open('data/stickerAll2.json', 'r', encoding='UTF-8') as f:
        stickerList = json.loads(f.read())
        index = create_starts_with_index(stickerList)
        with open('index.json', 'w') as f2:
            json.dump(index, f2, indent=2)
        word = "good".lower().replace(' ', '').replace("'", "").replace('"', '').replace('`', '')
        arr_2d = []
        result = find_combinations(word, index)
        if result:
            for sub_array in result:
                for inner_array in sub_array:
                    arr_2d.append(inner_array)
            with open('res.json', 'w') as f3:
                json.dump(arr_2d, f3, indent=2)
        # if result:
        #     for combination in result:
        #         print(combination)
        # else:
        #     print("Keine passenden Kombinationen gefunden.")