# 打磚塊遊戲
嵌入式系統作業8
- 目前支援以下控制器
    - 鍵盤輸入(wasd, space)
    - 任何實作 IContoller 介面的控制器
- 目前支援以下顯示器
    - Terminel 輸出
    - sense_hat 輸出
    - 任何實作 IDisplay 介面的顯示器

## 如何運作

1. 安裝依賴套件
    ```sh
    pip install -r requirements.txt
    ```
2. 執行 brick_game.py
    ```sh
    python ./brick_game.py
    ```

3. 如何離開程式:
    ctrl + c 強制關閉程式即可