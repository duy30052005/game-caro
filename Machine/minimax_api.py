import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, request, jsonify
from AI import AI
from Board.BoardLogic import AdvancedBoardLogic

app = Flask(__name__)

# Cấu hình AI
ai_engine = AI(aiLevel=3, aiPlayer=2, userPlayer=1)

@app.route('/minimax', methods=['POST'])
def minimax_api():
    data = request.get_json()
    board_state = data.get("board")  # mảng 2D
    depth = data.get("depth", 3)

    if board_state is None:
        return jsonify({"error": "Board data missing"}), 400

    # Tạo object AdvancedBoardLogic từ dữ liệu JSON
    board = AdvancedBoardLogic()
    board.loadBoard(board_state)  # Bạn cần cài đặt hàm loadBoard từ mảng 2D

    move = ai_engine.hardLevel(board)
    return jsonify({"row": move[0], "col": move[1]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
