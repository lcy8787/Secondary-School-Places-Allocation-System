# 中學學位分配系統

[![Python Version](https://img.shields.io/badge/Python-3.9%20|%203.10%20|%203.11-blue)](./src/main.py)
[![License](https://img.shields.io/badge/License-Apache--2.0-yellow)](LICENSE)
[![DSE ICT](https://img.shields.io/badge/Subject-HKDSE%20ICT%20SBA-orange)](./documents/Task1_Design_Specification.md)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-no-red)](#)

[English](./README.md) | [繁體中文](./README.zh-Hant.md)

---

## 項目簡介

本專案為 **香港中學文憑考試 (HKDSE) 資訊及通訊科技科 (ICT)** 軟件開發單元的校本評核 (SBA) 項目。

系統模擬香港小學升中學的「統一派位」機制，根據學生的呈分試成績進行加權計算、劃分派位組別 (Banding)，並結合隨機編號與志願順序進行公平分配。

> **重要說明：** 本 README 為提升國際化程度而使用 AI 輔助改寫。`documents/` 資料夾中的項目文檔為符合學業誠信標準的原始學生課業。

---

## 功能特點

- **圖形化使用者介面 (GUI)**：使用 Python Tkinter 構建，操作直觀。
- **加權評分機制**：遵循教育局標準（中英數權重為 9，常識權重為 6）。
- **自動化組別劃分**：系統自動將學生按成績平均分為 Band 1、Band 2、Band 3。
- **隨機分配算法**：模擬隨機編號邏輯，處理學位供求衝突。
- **數據驗證**：包含分數範圍檢查、學校 ID 存在性檢查及名額餘額檢測。
- **結果導出**：分配結果自動生成為 `assign.csv`。

---

## 開始使用

### 運行環境
- Python 3.9.0 或更高版本。
- 支援 Windows、macOS 及 Linux 系統。

### 安裝
1. 從本倉庫下載源代碼（`.zip` 或 `.tar.gz`）。
2. 解壓縮檔案。

### 運行步驟
1. 確保資料夾內含有 `school.csv` 和 `students.csv` 數據檔案。
2. 執行 `main.py`：
   ```bash
   python main.py
   ```
3. 按照介面引導：
   - 匯入學校資料。
   - 匯入學生資料。
   - 按下「開始分配」。
   - 使用「查詢」功能查看特定學生結果。

---

## 項目結構

```
Secondary-School-Places-Allocation-System/
├── documents/           # 項目文檔
│   ├── [Task1_Design_Specification.md](./documents/Task1_Design_Specification.md)
│   └── [Task2_Testing_and_Evaluation.md](./documents/Task2_Testing_and_Evaluation.md)
├── src/
│   └── [main.py](./src/main.py)         # 主應用程式原始碼
├── school.csv          # 學校數據檔案
├── students.csv        # 學生數據檔案
├── assign.csv          # 輸出結果
├── README.md           # 英文說明文件
├── README.zh-Hant.md   # 繁體中文說明文件
└── LICENSE             # Apache License 2.0
```

---

## 數據結構說明

本系統使用多種數據結構以確保效率：
- **字典 (Dictionary)**：用於快速查找學生詳細資料。
- **二維陣列 (2D Array)**：管理學校剩餘配額。
- **列表 (List) 與 隊列 (Queue)**：處理 Banding 劃分及循環分配邏輯。
- **選擇排序 (Selection Sort)**：根據總分對學生進行排名。

---

## 學業誠信聲明

本專案為 HKDSE ICT SBA 的原創學生課業。所有 `documents/` 資料夾中的教材均為學生的原創作品，符合學業誠信要求。程式碼由學生親自撰寫，以展示學習成果。

**重要通知：** 本專案僅提供教育參考用途，不適用於實際派位行政工作。

---

## 免責聲明

本專案為高中課業作品。程式碼中可能存在未完善之處，不建議用於真實的升中派位行政工作。開發者對使用本軟件導致的任何數據損失不負責任。

---

```
Copyright © 2025 lcy lo. Licensed under the [Apache License, Version 2.0](LICENSE).
```