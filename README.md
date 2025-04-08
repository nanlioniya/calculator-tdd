# Calculator TDD Development Process

這個文件記錄了使用測試驅動開發（TDD）方法開發 Calculator Class 的完整過程。

## 開發環境

- Python 3.9.13
- unittest 測試框架

## CI 工具

本專案使用多個工具來確保程式品質：

### 1. CodeCov
- 追蹤並報告代碼覆蓋率
- 視覺化展示測試覆蓋範圍
- 自動生成覆蓋率報告
- 當前專案測試覆蓋率：100%

### 2. GitHub Actions
- 自動化測試執行
- 程式撰寫風格檢查
- Pull Request 審查輔助

### 3. Pylint
- 靜態程式分析
- 確保符合 PEP 8 規範
- 程式品質評分 9.23/10

## TDD 開發流程紀錄

### 1. 加法功能 (Addition)

1. **建立測試**
   ```python
   def test_add(self):
       self.assertEqual(self.calc.add(3, 5), 8)
   ```
   - 創建基本加法測試
   - 測試失敗原因：Calculator Class 缺少 add 方法

2. **實現功能**
   ```python
   def add(self, a, b):
       return a + b
   ```
   - 實現最簡單的加法功能
   - 測試通過

3. **重構（Refactor）**
   ```python
   def test_add(self):
       test_cases = [
           (3, 5, 8),    # 正數加法
           (-1, 1, 0),   # 正負數相加
           (-1, -1, -2)  # 負數相加
       ]
       for a, b, expected in test_cases:
           with self.subTest(f"{a} + {b} = {expected}"):
               self.assertEqual(self.calc.add(a, b), expected)
   ```
   - 增加更多測試案例
   - 使用 subTest 改善測試結構
   - 原有實現足夠簡潔，無需修改

### 2. 減法功能 (Subtraction)

1. **建立測試**
   ```python
   def test_subtract(self):
       self.assertEqual(self.calc.subtract(5, 3), 2)
   ```
   - 創建基本減法測試
   - 測試失敗原因：缺少 subtract 方法

2. **實現功能**
   ```python
   def subtract(self, a, b):
       return a - b
   ```
   - 實現基本減法功能
   - 測試通過

3. **重構（Refactor）**
   ```python
   def test_subtract(self):
       test_cases = [
           (5, 3, 2),    # 基本減法
           (1, 5, -4),   # 結果為負數
           (-1, -1, 0)   # 負數相減
       ]
       for a, b, expected in test_cases:
           with self.subTest(f"{a} - {b} = {expected}"):
               self.assertEqual(self.calc.subtract(a, b), expected)
   ```
   - 擴展測試案例覆蓋更多情況
   - 原有實現已經足夠簡潔

### 3. 乘法功能 (Multiplication)

1. **建立測試**
   ```python
   def test_multiply(self):
       self.assertEqual(self.calc.multiply(4, 3), 12)
   ```
   - 創建基本乘法測試
   - 測試失敗原因：缺少 multiply 方法

2. **實現功能**
   ```python
   def multiply(self, a, b):
       return a * b
   ```
   - 實現基本乘法功能
   - 測試通過

3. **重構（Refactor）**
   ```python
   def test_multiply(self):
       test_cases = [
           (3, 5, 15),   # 正數相乘
           (-2, 3, -6),  # 正負數相乘
           (0, 5, 0)     # 乘以零
       ]
       for a, b, expected in test_cases:
           with self.subTest(f"{a} * {b} = {expected}"):
               self.assertEqual(self.calc.multiply(a, b), expected)
   ```
   - 增加邊界情況測試
   - 實現程式無需修改

### 4. 除法功能 (Division)

#### 第一個 iteration
1. **建立測試**
   ```python
   def test_divide(self):
       self.assertEqual(self.calc.divide(6, 2), 3.0)
   ```
   - 創建基本除法測試
   - 測試失敗原因：缺少 divide 方法

2. **實現功能**
   ```python
   def divide(self, a, b):
       return float(a) / b
   ```
   - 實現基本除法功能
   - 測試通過

#### 第二個 iteration
1. **建立測試**
   ```python
    print("\n測試除以零的情況")
    with self.assertRaises(ValueError):
        self.calc.divide(5, 0)
    print("成功捕獲除以零錯誤")
   ```
   - 添加除以零的測試
   - 測試失敗原因：未處理除以零的情況

2. **實現功能（Green）**
   ```python
   def divide(self, a, b):
       if b == 0:
           raise ValueError("Cannot divide by zero")
       return float(a) / b
   ```
   - 添加除以零的檢查
   - 測試通過

3. **重構（Refactor）**
   ```python
   def test_divide(self):
       test_cases = [
           (6, 2, 3.0),    # 整數除法
           (-6, 2, -3.0),  # 負數除法
           (5, 2, 2.5)     # 小數結果
       ]
       for a, b, expected in test_cases:
           with self.subTest(f"{a} / {b} = {expected}"):
               result = self.calc.divide(a, b)
               self.assertEqual(result, expected)
               self.assertIsInstance(result, float)
   ```
   - 增加更多測試案例
   - 添加返回類型檢查
   - 實現程式已經足夠 robust

### CI/CD 實驗記錄

成功進行了以下 CI/CD 相關實驗：

1. **破壞構建測試**
   - 通過引入錯誤的程式導致構建失敗
   - 通過添加失敗的測試案例測試 CI 系統
   - 成功檢測到問題並在修復後恢復構建

2. **代碼品質改進**
   - 根據靜態分析工具的回饋進行改進
   - 補充完整的文檔字符串
   - 修正程式風格問題

3. **持續改進流程**
   - 即時發現並修復問題
   - 維護程式品質標準
   - 確保測試覆蓋率維持在高水準

## 開發總結

整個 TDD 開發過程展示了：
1. 遵循建立測試、實現功能、refactoring 的循環
2. 從簡單測試開始，逐步增加複雜度
3. 持續改進測試案例
4. 注意邊界條件處理
5. 保持程式簡潔性

每個功能都經過了完整的 TDD 循環：
- 先寫測試（失敗）
- 實現功能（通過）
- 必要時 refactoring
- 添加更多測試案例

這種開發方式確保了程式的品質和可維護性。