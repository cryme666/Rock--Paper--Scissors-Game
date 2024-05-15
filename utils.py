CHOICES = ["🪨", "📄", "✂️"]

bot_commands = {
    '/help': 'Список команд',
    '/start_game': 'Почати гру',
    '/admin': 'Інформація для розробників',
    
}


images = {
    'welcome': 'https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExMmRoNDc5NDUzcXV6ZjhyNDBlcW00a2czOW5ia2tqbzVjN3F6Z2IyYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/IzKrzRa01oB2KkvC7I/giphy.gif',
    'choose': 'https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExcnZycGE2ZzNlNWlwYm9manExN3NyMHh5cWJiZGw3dGdpM204eXJ4dCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/eaDai9TQ2o1LKCj8xT/giphy.gif',
    'win': 'https://64.media.tumblr.com/b675b4f06b080a76fc6fc2dd42234588/tumblr_nx9gh7GkDT1rwfctbo2_500.gifv',
    'lose': 'https://64.media.tumblr.com/8da8f386f2820e3be033524e19d1634d/tumblr_nx9gh7GkDT1rwfctbo3_500.gifv',
    'friendship': 'https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExc2Rnczlmb243ZjlocTNhanJoanMxYTl4bGZ2ZGM0cXFmNTVmcTJhbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/VhRU9RvKZWKujYXhlJ/giphy.gif',
    'commands': 'https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExanBwZTFlcXF0NG9tbmY2ODZqaHZxemJvM2lsOXQ1NGh3aHN1eHVtbCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/L2KeF62rjXMyIZ7GMu/giphy.gif',
    'error': 'https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExdWs2YWpmZXlkNDk2NWQzeW5hOXJpNGJ0ZWpucjVydHNvZmc0bXJ6YSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/elPGI1VakLYmuPKPmE/giphy.gif'
}

admins = [
    655826401,
    719626894
]

def get_winner_animation(result):
    if result == 1:
        return images['win']
    elif result == -1:
        return images['lose']
    else:
        return images['friendship']
    
    