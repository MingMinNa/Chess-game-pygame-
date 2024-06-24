# Chess Game
這是一個用 pygame 套件所做出來的西洋棋遊戲。  
由於是第一次用 python 做遊戲，功能和設計較為簡略。

## 遊戲玩法
一般的西洋棋玩法  
由白棋方先行，移動後會會翻轉棋盤，接著由黑棋方移動。  
背景顏色會因移動方顏色而改變。背景為黑時，黑棋方移動；背景為白時，白旗方移動。

**翻轉棋盤是為了讓移動方永遠從下面往上進攻 (~~雖然自己一個人玩頭很暈~~)**

## 遊戲畫面
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*遊戲初始畫面*&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*棋盤與棋子*   
<img src="https://github.com/MingMinNa/ChessGame/blob/main/img/Display_img/display_init.png" alt="display_init.png" width="200" height="200">
<img src="https://github.com/MingMinNa/ChessGame/blob/main/img/Display_img/display_board.png" alt="display_board.png" width="200" height="200">  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*移動提示(1)*&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*移動提示(2)*  
<img src="https://github.com/MingMinNa/ChessGame/blob/main/img/Display_img/display_play1.png" alt="display_play1.png" width="200" height="200">
<img src="https://github.com/MingMinNa/ChessGame/blob/main/img/Display_img/display_play2.png" alt="display_play2.png" width="200" height="200">


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*晉升提示*&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*晉升面板*  
<img src="https://github.com/MingMinNa/ChessGame/blob/main/img/Display_img/display_promotion1.png" alt="display_promotion1.png" width="200" height="200">
<img src="https://github.com/MingMinNa/ChessGame/blob/main/img/Display_img/display_promotion2.png" alt="display_promotion2.png" width="200" height="200">


## 補充說明
1. 在這個遊戲中，西洋棋棋子移動方面都有盡量還原(例如:吃過路兵、王翼易位)。  
2. 在國王移動的判斷上，有做出不可移動到被攻擊位置上的判斷；當王位於敵方攻擊區域內時，會在棋盤上方顯示 **Check**
3. 沒寫判斷和局的程式碼 (沒有檢查是否**無子可動**)，這點較為可惜。

## 程式碼
由於目前的程式碼是邏輯跟繪畫一起處理，所以可讀性較差，還請見諒。  
本來想要再寫一個分離邏輯跟繪畫的版本，但是每次都寫到一半就寫不下去了...。  
所以我想就不要改好了。
---
# Chess Game 
This is a chess game created using the Pygame library.  
It's my first time developing a game in Python(and Pygame), so the functionality and design are relatively basic.  

## How to play
The general rules of chess are followed in this game.  
The game begins with the white pieces, and after each move, the board is flipped. Then it's turn of the black pieces to move.  
The background color will change based on the color of moving side.

**Flipping the board is for attacker to move from below to above (simplify the code complexity)**

## Game Screen
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*game initial screen*&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*board and chesspiece*   
<img src="https://github.com/MingMinNa/ChessGame/blob/main/img/Display_img/display_init.png" alt="display_init.png" width="200" height="200">
<img src="https://github.com/MingMinNa/ChessGame/blob/main/img/Display_img/display_board.png" alt="display_board.png" width="200" height="200">  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*move hint(1)*&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*move hint(2)*  
<img src="https://github.com/MingMinNa/ChessGame/blob/main/img/Display_img/display_play1.png" alt="display_play1.png" width="200" height="200">
<img src="https://github.com/MingMinNa/ChessGame/blob/main/img/Display_img/display_play2.png" alt="display_play2.png" width="200" height="200">


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*promotion hint*&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*promotion panel*  
<img src="https://github.com/MingMinNa/ChessGame/blob/main/img/Display_img/display_promotion1.png" alt="display_promotion1.png" width="200" height="200">
<img src="https://github.com/MingMinNa/ChessGame/blob/main/img/Display_img/display_promotion2.png" alt="display_promotion2.png" width="200" height="200">


## Note
1. In this game, the movements of the chess pieces are as close to the general rules as possible (e.g. en_passant, castling).
2. For the king's movement, the game include checks to ensure the king cannot to move to a cell under attack, and when your king is in the cell under attack, it show the hint **Check** above the board.
3. The code doesn't include "check whether no legal moves", you have to check it yourself.