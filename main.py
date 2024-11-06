def main():
    frankensteinFile = "books/frankenstein.txt"

    with open(frankensteinFile) as f:
        file_contents = f.read()
        count = get_num_words(file_contents)
        chars = get_chars_count(file_contents)
        make_report(frankensteinFile, count, chars)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_count(text):
    chars_dict = {}
    lowered_text = text.lower()

    for c in lowered_text:
        if c in chars_dict:
            chars_dict[c] += 1
        else:
            if c.isalpha():
                chars_dict[c] = 1
    return chars_dict


def sort_on(dict):
    return dict["symb"]


def make_report(fileName, words_count, chars_dict):
    chars_arr = []
    for k, v in chars_dict.items():
        chars_arr.append({"symb": k, "num": v})
    chars_arr.sort(reverse=False, key=sort_on)

    print(f"--- Begin Report of {fileName} ---")
    print(f"{words_count} words found in the documentn")
    print(" ")

    for c in chars_arr:
        print(f"The {c["symb"]} character was found {c["num"]} times")
    print("--- End report ---")


main()
