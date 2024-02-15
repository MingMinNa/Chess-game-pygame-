# Chess Game
這是一個用 pygame 套件所做出來的西洋棋遊戲。  
由於是第一次用 python 做遊戲，功能和設計較為簡略。

## 遊戲玩法
一般的西洋棋玩法  
由白棋方先行，移動後會會翻轉棋盤，接著由黑棋方移動。

**翻轉棋盤是為了讓移動方永遠從下面往上進攻 (~~雖然自己一個人玩頭很暈~~)**

## 遊戲畫面
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*遊戲初始畫面*&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*棋盤與棋子*   
<img src="https://github.com/MingMinNa/ChessGame/blob/main/img/display_init.png" alt="display_init.png" width="200" height="200">
<img src="https://github.com/MingMinNa/ChessGame/blob/main/img/display_board.png" alt="display_board.png" width="200" height="200">  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*移動提示(1)*&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*移動提示(2)*  
<img src="https://github.com/MingMinNa/ChessGame/blob/main/img/display_play1.png" alt="display_play1.png" width="200" height="200">
<img src="https://github.com/MingMinNa/ChessGame/blob/main/img/display_play2.png" alt="display_play2.png" width="200" height="200">


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*晉升提示*&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*晉升面板*  
<img src="https://github.com/MingMinNa/ChessGame/blob/main/img/display_promotion1.png" alt="display_promotion1.png" width="200" height="200">
<img src="https://github.com/MingMinNa/ChessGame/blob/main/img/display_promotion2.png" alt="display_promotion2.png" width="200" height="200">


## 補充說明
1. 在這個遊戲中，西洋棋棋子移動方面都有盡量還原(例如:吃過路兵、王翼易位)。  
2. 在國王移動的判斷上，有做出不可移動到被攻擊位置上的判斷；但是，當國王被攻擊時，並沒有特殊顯示，需要自行判斷敵人有沒有威脅到王。  
3. 沒寫判斷和局的程式碼 (沒有檢查是否**無子可動**)，這點較為可惜。
