def dash_function(text):
    word_list= text.split("-")
    word_list.sort()
    ordered_text = '-'.join(word_list)
    return ordered_text

print(dash_function("ZHello-World"))