import json

settings = {}
with open('./assets/json/settings.json', 'r') as settings_json:
    settings = json.load(settings_json)

class ENG:
    text_lang = ["English"]
    text_lang_select = ["Select Your Language"]
    text_lang_continue = ["Continue"]
    text_intro1 = ["A Untitled Project"]
    text_intro2U = ["Produced by"]
    text_intro2D = ["Shimyytrov Studio"]

class TAI:
    text_lang = ["中文(台灣正體)"]
    text_lang_select = ["選擇你的語言"]
    text_lang_continue = ["按此繼續"]
    text_intro1 = ["一個無名項目"]
    text_intro2U = ["希米特羅夫工作室"]
    text_intro2D = ["出品"]

class CHI:
    text_lang = ["中文(中国简体)"]
    text_lang_select = ["选择你的语言"]
    text_lang_continue = ["按此继续"]
    text_intro1 = ["一个无名项目"]
    text_intro2U = ["希米特罗夫工作室"]
    text_intro2D = ["出品"]

class debug:
    text_lang = ["DEBUG (For developer)"]
    text_lang_select = ["<text_lang_select>"]
    text_lang_continue = ["<text_lang_continue>"]
    text_intro1 = ["<text_intro1>"]
    text_intro2U = ["<text_intro2U>"]
    text_intro2D = ["<text_intro2D>"]