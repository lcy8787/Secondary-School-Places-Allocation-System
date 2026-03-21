# Secondary School Places Allocation System

[![Python Version](https://img.shields.io/badge/Python-3.9%20|%203.10%20|%203.11-blue)](./src/main.py)
[![License](https://img.shields.io/badge/License-Apache--2.0-yellow)](LICENSE)
[![DSE ICT](https://img.shields.io/badge/Subject-HKDSE%20ICT%20SBA-orange)](./documents/Task1_Design_Specification.md)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-no-red)](#)

[English](./README.md) | [繁體中文](./README.zh-Hant.md)

---

## Overview

This project is a school-based assessment (SBA) for the **Hong Kong Diploma of Secondary Education Examination (HKDSE) Information and Communications Technology (ICT)** subject, software development unit.

The system simulates Hong Kong's Primary School Placement Admission mechanism. It calculates weighted scores based on internal assessment results, assigns students to placement bands, and allocates school places based on random numbers and application preferences.

> **Important Note:** This README was partially rewritten with AI assistance for clarity and international presentation. The underlying project documentation in the `documents/` folder represents original student coursework that complies with academic integrity standards.

---

## Features

- **Graphical User Interface (GUI)**: Built with Python Tkinter for intuitive operation.
- **Weighted Scoring System**: Follows Education Bureau standards (Chinese/English/Math weight = 9, General Science weight = 6).
- **Automated Banding**: Automatically divides students into Band 1, Band 2, and Band 3.
- **Random Allocation Algorithm**: Simulates random number logic for seat allocation.
- **Data Validation**: Includes score range validation, school ID existence checks, and quota balance detection.
- **Export Results**: Allocation results are automatically exported to `assign.csv`.

---

## Getting Started

### Requirements
- Python 3.9.0 or higher.
- Compatible with Windows, macOS, and Linux.

### Installation
1. Download the source code from this repository (`.zip` or `.tar.gz`).
2. Extract the files.

### How to Run
1. Ensure `school.csv` and `students.csv` data files are present.
2. Run `main.py` by double-clicking or executing in terminal:
   ```bash
   python main.py
   ```
3. Follow the on-screen instructions:
   - Import school data.
   - Import student data.
   - Click "Start Allocation".
   - Use "Query" to view specific student results.

---

## Project Structure

```
Secondary-School-Places-Allocation-System/
├── documents/           # Project documentation
│   ├── [Task1_Design_Specification.md](./documents/Task1_Design_Specification.md)
│   └── [Task2_Testing_and_Evaluation.md](./documents/Task2_Testing_and_Evaluation.md)
├── src/
│   └── [main.py](./src/main.py)         # Main application source code
├── school.csv          # School data file
├── students.csv        # Student data file
├── assign.csv          # Output results
├── README.md           # English documentation
├── README.zh-Hant.md   # Traditional Chinese documentation
└── LICENSE             # Apache License 2.0
```

---

## Data Structures

This system utilizes various data structures for efficiency:
- **Dictionary**: For fast student detail lookup.
- **2D Array**: For managing school remaining quotas.
- **List & Queue**: For banding allocation and cyclic allocation logic.
- **Selection Sort**: For ranking students by total scores.

---

## Academic Integrity Statement

This project represents original coursework completed for HKDSE ICT SBA. All materials in the `documents/` folder are the original work of the student and comply with academic integrity requirements. The code was written by the student to demonstrate learning outcomes.

**Important Notice:** This project is provided for educational reference only. It is not intended for actual administrative use in real placement exercises.

---

## Disclaimer

This project is a high school coursework assignment. The code may contain imperfections and should not be used for real-world placement administration. The developer assumes no responsibility for any data loss resulting from the use of this software.

---

```
Copyright © 2025 lcy lo. Licensed under the [Apache License, Version 2.0](LICENSE).
```