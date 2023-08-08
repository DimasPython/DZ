import re
file_name = "example.txt"
file_name2 = "example2.txt"
text_task3 = "TEXT.txt"

with open(file_name, "w", encoding="utf8") as file:
    file.write(input("Введитe какой-то текст, и чтобы пару слов было длиннее 7-ми смиволов: "))

with open(file_name, "r", encoding="utf8") as file:
    the_text = file.read()
    print(f"количевство слов в файле: ", len(re.findall(r"[A-Za-z]+", the_text)))

#####################################################################################
#####################################################################################

with open(file_name2, "w") as file:
    moded_text = re.findall(r"\b\w{7,}\b", the_text)
    for word7 in moded_text:
        file.write(word7 + ", ")

with open(file_name2, "r") as file:
    new_text_in_file = file.read()
    print(f"вот слова которые длиннее 7-ми символов:", new_text_in_file)
    print(f"вот количивство слов длинее 7-ми символов:", len(moded_text))


#########################################################################
#########################################################################
with open(text_task3, "w") as file:
    file.write(input("введите какой-то текст где будут слова die:"))

with open(text_task3, "r") as file:
    main_text = file.read()
    print(f"кол-во слов die в тексте:", len(re.findall(r"\bdie\b", main_text)))

with open(text_task3, "w") as file:
    newtext = re.sub(r"\bdie\b", "***", main_text)
    file.write(newtext)
    print(f"вот новый текст:", newtext) 

