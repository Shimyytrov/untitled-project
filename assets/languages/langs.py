import json

config = json.load(open('assets/config/config.json', 'r'))

class ENG:
    text_helloWorld = ["Hello World!"]
    text_lang = ["English"]
    text_lang_select = ["Select Your Language"]
    text_lang_continue = ["Continue"]
    text_intro1 = ["A Untitled Project"]
    text_intro2 = ["Produced by", "Shimyytrov Studio"]

class zhTW:
    text_helloWorld = ["早安世界！"]
    text_lang = ["中文(台灣正體)"]
    text_lang_select = ["選擇你的語言"]
    text_lang_continue = ["按此繼續"]
    text_intro1 = ["一個無名項目"]
    text_intro2 = ["希米特羅夫工作室", "出品"]

class zhCN:
    text_helloWorld = ["早安世界！"]
    text_lang = ["中文(中国简体)"]
    text_lang_select = ["选择你的语言"]
    text_lang_continue = ["按此继续"]
    text_intro1 = ["一个无名项目"]
    text_intro2 = ["希米特罗夫工作室", "出品"]

class debug:
    text_helloWorld = ["<text_helloWorld>"]
    text_lang = ["DEBUG (For developer)"]
    text_lang_select = ["<text_lang_select>"]
    text_lang_continue = ["<text_lang_continue>"]
    text_intro1 = ["<text_intro1>"]
    text_intro2 = ["<text_intro2U>", "<text_intro2D>"]

class SCH:
    text_helloWorld = ["Welt, privetse!"]
    text_lang = ["Schmitŕovkiy (Unfinished)"]
    text_lang_select = ["Duzhe Schtora pikiten"]
    text_lang_continue = ["Kontinen"]
    text_intro1 = ["Eine >Untitled< Prozhekt"]
    text_intro2 = ["Schmitŕov-Studio", "PRODUZENTVA"]

class NOS:
    text_helloWorld = ["Велт, Прівет!"]
    text_lang = ["Нощкаріскі Щтор (Unfinished)"]
    text_lang_select = ["Дуже Щтор пікітән"]
    text_lang_continue = ["Контінән"]
    text_intro1 = ["Одін >Untitled< Прожект"]
    text_intro2 = ["Щмітғов-Студіо", "ПРОДУСӘНТВА"]

for clang_class, clang_config in {ENG:"ENG", zhTW:"zhTW", zhCN:"zhCN", debug:"debug", SCH:"SCH", NOS:"NOS"}.items():
    if clang_config == config["lang"]:
        clang = clang_class