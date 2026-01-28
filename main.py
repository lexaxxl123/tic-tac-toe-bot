import telebot
import random
from telebot import types

# Insert your token here if u want to
bot = telebot.TeleBot('YOUR_TOKEN_HERE')

active_games = {}

class Statistics:
    def __init__(self):
        self.move_count = 0
        self.winner = None

    def record_move(self):
        self.move_count += 1

    def set_winner(self, winner_name):
        self.winner = winner_name

    def get_result_text(self):
        text = f"Game Over!\nTotal moves: {self.move_count}\n"
        if self.winner:
            text += f"Winner: {self.winner}"
        else:
            text += "It's a draw!"
        return text

class Bot:
    def __init__(self, board_object):
        self.board = board_object

    def bot_move(self):
        empty_cells = []
        for i in range(3):
            for j in range(3):
                if self.board.grid[i][j] == '[_]':
                    empty_cells.append((i, j))
        
        if len(empty_cells) > 0:
            bot_x, bot_y = random.choice(empty_cells)
            self.board.grid[bot_x][bot_y] = '[O]'

class Board:
    def __init__(self):
        self.grid = []
        self.fill_board()

    def fill_board(self):
        self.grid = []
        for i in range(3):
            self.grid.append([])
            for j in range(3):
                self.grid[i].append('[_]')

    def create_keyboard(self):
        markup = types.InlineKeyboardMarkup()
        for i in range(3):
            row = []
            for j in range(3):
                text_btn = self.grid[i][j]
                row.append(types.InlineKeyboardButton(text=text_btn, callback_data=f"{i}-{j}"))
            markup.add(*row)
        return markup

class Win:
    def check_win(self, grid):
        lines = []
        
        for i in range(3):
            lines.append((grid[i][0], grid[i][1], grid[i][2]))
      
        for j in range(3):
            lines.append((grid[0][j], grid[1][j], grid[2][j]))
          
        lines.append((grid[0][0], grid[1][1], grid[2][2]))
        lines.append((grid[0][2], grid[1][1], grid[2][0]))

        win_user = ('[X]', '[X]', '[X]')
        win_bot = ('[O]', '[O]', '[O]')

        for line in lines:
            if line == win_user:
                return "Player"
            elif line == win_bot:
                return "Bot"
        
        return None

class Game:
    def __init__(self):
        self.board = Board()
        self.stats = Statistics()
        self.bot = Bot(self.board)
        self.win_checker = Win()
        self.is_running = True

@bot.message_handler(commands=['start'])
def start_game(message):
    chat_id = message.chat.id
    active_games[chat_id] = Game()
    
    game = active_games[chat_id]
    
    bot.send_message(
        chat_id, 
        "Game started! You are [X]. Choose a cell:", 
        reply_markup=game.board.create_keyboard()
    )

@bot.callback_query_handler(func=lambda call: True)
def handle_click(call):
    chat_id = call.message.chat.id
    
    if chat_id not in active_games:
        return

    game = active_games[chat_id]
    if not game.is_running:
        return

    coords = call.data.split('-')
    x = int(coords[0])
    y = int(coords[1])

    if game.board.grid[x][y] == '[_]':
        game.board.grid[x][y] = '[X]'
        game.stats.record_move()
    else:
        bot.answer_callback_query(call.id, "Occupied!")
        return

    winner = game.win_checker.check_win(game.board.grid)
    if winner:
        game.stats.set_winner(winner)
        game.is_running = False
        final_text = game.stats.get_result_text()
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=final_text, reply_markup=game.board.create_keyboard())
        return

    is_full = True
    for row in game.board.grid:
        if '[_]' in row:
            is_full = False
    if is_full:
        game.is_running = False
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text="It's a draw! No moves left.", reply_markup=game.board.create_keyboard())
        return

    game.bot.bot_move()

    winner = game.win_checker.check_win(game.board.grid)
    if winner:
        game.stats.set_winner(winner)
        game.is_running = False
        final_text = game.stats.get_result_text()
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=final_text, reply_markup=game.board.create_keyboard())
        return

    bot.edit_message_reply_markup(chat_id=chat_id, message_id=call.message.message_id, reply_markup=game.board.create_keyboard())

bot.polling(non_stop=True)
