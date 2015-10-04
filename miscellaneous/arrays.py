import datetime

days = {1: ["mon", "pn"],
        2: ["tue", "vt"],
        3: ["wed", "sr"],
        4: ["thu", "cht"],
        5: ["fri", "pt"],
        6: ["sat", "sb"],
        7: ["sun", "vs"]}

# Set all possible commands and max. arguments quantity
commands = {
    '/authors': 0,
    '/bug': 150,
    '/changelang': 1,
    '/help': 0,
    '/idea': 150,
    '/next': 2,
    '/now': 2,
    '/setgroup': 1,
    '/setteacher': 1,
    '/start': 0,
    '/time': 0,
    '/today': 2,
    '/tomorrow': 2,
    '/tt': 5,
    '/week': 0,
    '/where': 1,
    '/who': 1,
}

no_timetable_commands = [
    '/start',
    '/help',
    '/time',
    '/week',
    '/changelang',
    '/authors',
    '/bug',
    '/idea',
]

time = "\
1. 08:30 - 10:05\n\
2. 10:25 - 12:00\n\
3. 12:20 - 13:55\n\
4. 14:15 - 15:50\n\
5. 16:10 - 17:45"

# Timetable
now = datetime.datetime.now()
pairs = [
    datetime.datetime(now.year, now.month, now.day, 0, 1),
    datetime.datetime(now.year, now.month, now.day, 8, 30),
    datetime.datetime(now.year, now.month, now.day, 10, 5),
    datetime.datetime(now.year, now.month, now.day, 12, 00),
    datetime.datetime(now.year, now.month, now.day, 13, 55),
    datetime.datetime(now.year, now.month, now.day, 15, 50),
    datetime.datetime(now.year, now.month, now.day, 17, 45),
    datetime.datetime(now.year, now.month, now.day, 23, 59)]