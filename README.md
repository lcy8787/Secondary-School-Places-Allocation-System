# 中學學位分配系統 (Secondary School Places Allocation System)

![Python Version](https://img.shields.io/badge/Python-3.9%20|%203.10%20|%203.11-blue)
![License](https://img.shields.io/badge/License-Apache--2.0-yellow)
![DSE ICT](https://img.shields.io/badge/Subject-HKDSE%20ICT%20SBA-orange)
![Maintenance](https://img.shields.io/badge/Maintained%3F-no-red)
![Last Commit](https://img.shields.io/github/last-commit/lcy8787/Secondary-School-Places-Allocation-System)

## 項目簡介 (Introduction)

歡迎！這是一個專為 **香港中學文憑考試 (HKDSE) 資訊及通訊科技科 (ICT)** 軟件開發單元設計的校本評核 (SBA) 項目。

本系統模擬了香港小學升中學的「統一派位」機制。系統會根據學生的呈分試成績進行加權計算、劃分派位組別 (Banding)，並結合隨機編號與志願順序進行公平分配。

**特別聲明：**
- 項目開發者：**lcy lo**
- 本項目僅供學術交流與研究使用，**無任何實際行政用途**。
- 所有腳本編寫均符合學術誠信原則。

---

## 功能特點 (Features)

- **圖形化使用者介面 (GUI)**：使用 Python Tkinter 構建，操作直觀。
- **加權評分機制**：嚴格遵循教育局標準（中英數權重為 9，常識為 6 等）。
- **自動化組別劃分**：系統自動將學生按成績平均分為 Band 1, Band 2, Band 3。
- **隨機分配算法**：模擬隨機編號邏輯，處理學位供求衝突。
- **數據驗證**：包含分數範圍檢查、學校 ID 存在性檢查及名額餘額檢測。
- **結果導出**：分配結果自動生成為 `assign.csv`。

---

## 開始使用 (Getting Started)

### 運行環境 (Requirements)
- Python 3.9.0 或更高版本。
- 本程序支持 Windows, macOS 及 Linux 系統。

### 下載與安裝 (Download)
1. 從本倉庫下載源代碼（`.zip` 或 `.tar.gz`）。
2. 解壓縮文件。

### 運行步驟 (How to run)
1. 確保文件夾內含有 `school.csv` 和 `students.csv` 數據文件。
2. 雙擊運行 `ict_sba_v1.3.py` 或在終端輸入：
   ```bash
   python ict_sba_v1.3.py