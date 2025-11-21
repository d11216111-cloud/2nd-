# 單元測試結果記錄 (Unit Test Results)

## 任務三：執行單元測試並記錄結果

### 測試環境
- Python 版本: Python 3.x
- 測試框架: unittest (Python 內建)
- 測試檔案: test_safe_division.py
- 被測試模組: safe_division.py

---

## 綠燈測試結果（Green Light - Tests Passing）

### 測試執行時間
執行日期: 2025-11-21

### 執行命令
```bash
python -m unittest test_safe_division.py -v
```

### 測試結果
```
test_boundary_values (test_safe_division.TestSafeDivision.test_boundary_values)
Test division with boundary values ... ok

test_decimal_division (test_safe_division.TestSafeDivision.test_decimal_division)
Test division with decimal numbers ... ok

test_division_by_zero (test_safe_division.TestSafeDivision.test_division_by_zero)
Test division by zero returns None instead of raising an exception ... ok

test_large_numbers (test_safe_division.TestSafeDivision.test_large_numbers)
Test division with large numbers ... ok

test_negative_division (test_safe_division.TestSafeDivision.test_negative_division)
Test division with negative numbers ... ok

test_normal_division (test_safe_division.TestSafeDivision.test_normal_division)
Test normal division with positive numbers ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.000s

OK
```

### 測試案例說明

#### ✅ 1. test_normal_division (正常數值相除)
- **測試內容**: 測試正常的正數相除
- **測試案例**:
  - 10 ÷ 2 = 5.0 ✓
  - 100 ÷ 4 = 25.0 ✓
  - 7 ÷ 2 = 3.5 ✓
- **結果**: 通過 (PASS)

#### ✅ 2. test_negative_division (負數相除)
- **測試內容**: 測試負數的除法運算
- **測試案例**:
  - -10 ÷ 2 = -5.0 ✓
  - 10 ÷ -2 = -5.0 ✓
  - -10 ÷ -2 = 5.0 ✓
- **結果**: 通過 (PASS)

#### ✅ 3. test_boundary_values (邊界值相除)
- **測試內容**: 測試邊界值的除法運算
- **測試案例**:
  - 0 ÷ 5 = 0.0 ✓
  - 1 ÷ 1 = 1.0 ✓
  - 1 ÷ 3 ≈ 0.333... ✓
- **結果**: 通過 (PASS)

#### ✅ 4. test_division_by_zero (除以零)
- **測試內容**: 測試除以零的情況，驗證程式能正確處理而不會當機
- **測試案例**:
  - 10 ÷ 0 = None ✓
  - -10 ÷ 0 = None ✓
  - 0 ÷ 0 = None ✓
- **結果**: 通過 (PASS)
- **說明**: 函式正確處理除以零的狀況，返回 None 而不是拋出 ZeroDivisionError

#### ✅ 5. test_large_numbers (大數相除)
- **測試內容**: 測試大數值的除法運算
- **測試案例**:
  - 1,000,000 ÷ 1,000 = 1,000.0 ✓
  - 999,999 ÷ 3 = 333,333.0 ✓
- **結果**: 通過 (PASS)

#### ✅ 6. test_decimal_division (小數相除)
- **測試內容**: 測試小數的除法運算
- **測試案例**:
  - 5.5 ÷ 2 = 2.75 ✓
  - 10.5 ÷ 3.5 = 3.0 ✓
- **結果**: 通過 (PASS)

### 綠燈總結
✅ **所有測試通過 (6/6)**

所有預期的測試案例都通過，顯示為綠燈。`safe_division` 函式能正確處理各種情境：
- ✓ 正常的數值相除
- ✓ 負數相除
- ✓ 邊界值相除
- ✓ 大數值相除
- ✓ 小數相除
- ✓ **除以零的狀況** - 使程式不會當機

**關鍵程式碼 (safe_division.py 第 18-19 行)**:
```python
if b == 0:
    return None
```
這段程式碼確保了當除數為 0 時，函式會安全地返回 None，而不是拋出 ZeroDivisionError 異常。

---

## 紅燈測試結果（Red Light - Tests Failing）

### 測試執行時間
執行日期: 2025-11-21

### 修改內容
將 `safe_division` 函式中「處理除以零」的程式碼註解掉：

**修改前 (safe_division.py)**:
```python
def safe_division(a, b):
    if b == 0:
        return None
    return a / b
```

**修改後 (safe_division.py)**:
```python
def safe_division(a, b):
    # if b == 0:
    #     return None
    return a / b
```

### 執行命令
```bash
python -m unittest test_safe_division.py -v
```

### 測試結果
```
test_boundary_values (test_safe_division.TestSafeDivision.test_boundary_values)
Test division with boundary values ... ok

test_decimal_division (test_safe_division.TestSafeDivision.test_decimal_division)
Test division with decimal numbers ... ok

test_division_by_zero (test_safe_division.TestSafeDivision.test_division_by_zero)
Test division by zero returns None instead of raising an exception ... ERROR

test_large_numbers (test_safe_division.TestSafeDivision.test_large_numbers)
Test division with large numbers ... ok

test_negative_division (test_safe_division.TestSafeDivision.test_negative_division)
Test division with negative numbers ... ok

test_normal_division (test_safe_division.TestSafeDivision.test_normal_division)
Test normal division with positive numbers ... ok

======================================================================
ERROR: test_division_by_zero (test_safe_division.TestSafeDivision.test_division_by_zero)
Test division by zero returns None instead of raising an exception
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/runner/work/2nd-/2nd-/test_safe_division.py", line 32, in test_division_by_zero
    self.assertIsNone(safe_division(10, 0))
                      ^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/2nd-/2nd-/safe_division.py", line 26, in safe_division
    return a / b
           ~~^~~
ZeroDivisionError: division by zero

----------------------------------------------------------------------
Ran 6 tests in 0.001s

FAILED (errors=1)
```

### 紅燈測試案例分析

#### ❌ test_division_by_zero (除以零) - 失敗
- **測試內容**: 測試除以零的情況
- **預期結果**: 返回 None
- **實際結果**: 拋出 ZeroDivisionError 異常
- **失敗原因**: 移除了除以零的處理程式碼後，Python 直接拋出 ZeroDivisionError
- **錯誤訊息**:
  ```
  File "/home/runner/work/2nd-/2nd-/test_safe_division.py", line 32, in test_division_by_zero
    self.assertIsNone(safe_division(10, 0))
                      ^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/2nd-/2nd-/safe_division.py", line 26, in safe_division
    return a / b
           ~~^~~
  ZeroDivisionError: division by zero
  ```

#### ✅ 其他測試案例
- test_normal_division: 仍然通過 ✓
- test_negative_division: 仍然通過 ✓
- test_boundary_values: 仍然通過 ✓
- test_large_numbers: 仍然通過 ✓
- test_decimal_division: 仍然通過 ✓

### 紅燈總結
❌ **測試失敗 (5 通過, 1 錯誤)**

當移除「處理除以零」的程式碼後：
- ✓ 一般的除法測試仍然通過 (5/6)
- ❌ 除以零的測試錯誤 (1/6)
- ❌ 程式直接拋出 `ZeroDivisionError`，未被妥善處理
- ❌ 這會導致程式當機，無法繼續執行

---

## 結論

### 重要性說明
這個測試演示充分證明了「處理除以零」程式碼的重要性：

1. **綠燈狀態（有處理除以零）**:
   - ✅ 所有測試通過
   - ✅ 程式能安全處理所有情況
   - ✅ 不會因為除以零而當機

2. **紅燈狀態（沒有處理除以零）**:
   - ❌ 除以零測試失敗
   - ❌ 程式拋出未處理的異常
   - ❌ 可能導致程式崩潰

### 最佳實踐
在進行除法運算時，**必須**處理除以零的情況，以確保程式的健壯性和穩定性。單元測試可以有效驗證這些邊界條件是否被正確處理。

### 程式碼恢復
測試完成後，已將除以零處理程式碼恢復，確保 `safe_division` 函式能正常運作。
