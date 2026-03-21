"""
Secondary School Places Allocation System
==========================================
Coursework for HKDSE ICT SBA

WARNING: This is student coursework provided for REFERENCE ONLY.
Do not copy or submit as your own work. Plagiarism may result in academic penalties.
All code was written by the student to demonstrate learning outcomes.

Documentation: [English](../README.md) | [繁體中文](../README.zh-Hant.md)
"""

import os
import random
import tkinter as tk
from tkinter import messagebox, filedialog

school_quota = []
students_data = {}
assign = []
band1 = []
band2 = []
band3 = []
cant_assign = []


def input_school_data():
    if school_file_path == "":
        raise FileNotFoundError("學校資料檔案未選擇")
    # 讀取學校資料
    print("讀取學校資料")
    f = open(school_file_path, 'r') 
    school_data = f.readlines() 
    f.close()
    
    for i in range(1, len(school_data)): # no標題
        data = school_data[i].strip().split(',')  # 分割成列表
        school_id = data[0] # 提取學校 ID
        quota = data[2] # 提取志願
        school_quota.append([school_id, quota]) # 將學校 ID 和志願添加到列表中
    print("學校資料讀取完成\n") 





def input_student_data():
    if student_file_path == "":
        raise FileNotFoundError("學生資料檔案未選擇")
    # 讀取學生資料
    print("讀取學生資料")
    f = open(student_file_path, 'r') 
    student_data = f.readlines() 
    f.close()
    
    for i in range(1, len(student_data)): # no標題
        data = student_data[i].strip().split(',')  # 分割成列表
        student_id = data[0]  # 提取學生 ID
        app_id = data[19] # 提取申請 ID
        name = data[1]  # 提取學生姓名
        
        p5_score = []
        for i in range(5, 12):  # 提取小五成績，去除錯誤引號並轉換為 int
            score = int(data[i].replace('"', '').strip())
            p5_score.append(score)

        p6_score = []
        for i in range(12, 19): # 提取小六成績，去除錯誤引號並轉換為 int
            score = int(data[i].replace('"', '').strip())
            p6_score.append(score)
            
        ss_choices = []
        for j in range(20, 39): # 提取中學選擇，去除錯誤引號
            ss_choice = data[j].replace('"', '').strip()
            ss_choices.append(ss_choice)
        
        students_data[student_id] = {
            'app_id': app_id,
            'name': name,
            'p5_score': p5_score,
            'p6_score': p6_score,
            'ss_choices': ss_choices, 
            'total_score': 0,
            'choice': 0,
        }  # 添加到字典中
    print("學生資料讀取完成\n")    

def verify_data():
    print("驗證學校 ID")
    has_error = False
    student_items = list(students_data.items())
    
    for i in range(len(student_items)):
        # 提取學生資料
        data = student_items[i][1]
        name = data['name']
        ss_choices = data['ss_choices']
        
        # 提取所有學校 ID
        school_ids = []
        for i in range(len(school_quota)):
            school_ids.append(school_quota[i][0])
        # 驗證學生選擇的學校是否在學校名單中
        for j in range(len(ss_choices)):
            if ss_choices[j] not in school_ids:
                print(f"學生 {name} 的選擇 {ss_choices[j]} 不在學校名單中")
                has_error = True
                
    # 驗證分數是否在 0 到 100 之間
    print("驗證分數是否在 0 到 100 之間")
    for i in range(len(student_items)):
        # 提取學生資料
        data = student_items[i][1]
        p5_score = data['p5_score']
        p6_score = data['p6_score']
        # 驗證分數範圍
        for score in p5_score + p6_score:
            if score < 0 or score > 100:
                print(f"學生 {data['name']} 的分數 {score} 不在 0 到 100 之間")
                has_error = True
    # 驗證學校名額是否足夠  
    print("驗證學校名額是否足夠")         
    total_quotas = 0
    for i in range(len(school_quota)):
        total_quotas += int(school_quota[i][1])
        
    if total_quotas < len(students_data):
        print(f"學校的名額 {total_quotas} 少於學生人數 {len(students_data)}")
        has_error = True

    return not has_error

def calculate_score():
    print("計算總分")
    student_items = list(students_data.items())
    for i in range(len(student_items)):
        student_id = student_items[i][0]
        data = student_items[i][1]
        p5_score = data['p5_score']
        p6_score = data['p6_score']
        total_score = 0
        for j in range(len(p5_score)):
            if j == 0 or j == 1: # 中文和英文
                total_score += p5_score[j] * 9 + p6_score[j] * 9
            elif j == 2: # 數學
                total_score += p5_score[j] * 8 + p6_score[j] * 8
            elif j == 3: # 常識
                total_score += p5_score[j] * 6 + p6_score[j] * 6
            elif j == 4: # 藝術
                total_score += p5_score[j] * 3 + p6_score[j] * 3
            elif j == 5: #音樂
                total_score += p5_score[j] * 2 + p6_score[j] * 2
            elif j == 6: # 體育
                total_score += p5_score[j] * 2 + p6_score[j] * 2
        students_data[student_id]['total_score'] = total_score
    
    print("計算總分完成\n")
    print("開始排序")
    
    global student_scores
    student_scores = []
    for i in range(len(student_items)):
        ss_id = student_items[i][0]
        ss_score = student_items[i][1]['total_score']
        student_scores.append((ss_id, ss_score))
        
    # 使用選擇排序根據總分從大到小排序學生
    for i in range(len(student_scores)):
        max_index = i
        for j in range(i + 1, len(student_scores)):
            if student_scores[j][1] > student_scores[max_index][1]:
                max_index = j
        student_scores[i], student_scores[max_index] = student_scores[max_index], student_scores[i]
    print("排序完成\n")
    
def assign_student():
    print("分配學生到 band1, band2, band3")
    # 把數據寫入 assign 隊列之中
    for i in range(len(student_scores)):
        assign.append(student_scores[i][0])
    

    # 將 assign 頭三分之一的數據放到 band1
    total = len(assign)
    one_third = total // 3
    two_third = (total // 3) * 2
    for i in range(total):
        if i < one_third:
            band1.append(assign[i]) # 頭三分之一的數據放到 band1
        elif i < two_third:
            band2.append(assign[i]) # 三分之一到三分之二的數據放到 band2
        else:
            band3.append(assign[i]) # 三分之二到結尾的數據放到 band3
    print("學生分配完成\n")
    
def assign_school():
    print("分配學生到學校\n")
    print("打亂 band1, band2, band3 的順序\n")
    # 打亂 band1, band2, band3 的順序
    random.shuffle(band1)
    random.shuffle(band2)
    random.shuffle(band3)
    # 建立學校分配列表
    global school_assign_list
    school_assign_list = {}
    for i in range(len(school_quota)):
        school_id = school_quota[i][0]
        quota = int(school_quota[i][1])
        school_assign_list[school_id] = []

    # 建立學生分配限額
    school_quota_left = []
    for school_id, quota in school_quota:
        school_quota_left.append([school_id, int(quota)])

    

    def process_band(band):
        queue = band.copy()
        while queue:  # 當 band 還有學生時
            student_id = queue[0]  # 取得 band 第一個學生的 ID
            student = students_data[student_id]  # 取得該學生的資料
            choice = student['choice']  # 取得學生目前選擇的志願序號
            if choice >= len(student['ss_choices']):  # 如果超過志願數，則移除該學生
                cant_assign.append(student_id)
                queue.pop(0)
                continue
            
            school_id = student['ss_choices'][choice]  # 取得學生目前選擇的學校 ID
            
            # 找到該學校剩餘名額,如果找不到則設為 0
            for i in range(len(school_quota_left)):
                if school_quota_left[i][0] == school_id:
                    quota_left = school_quota_left[i][1]
                    break
            else:
                quota_left = 0
            

            if quota_left > 0:  # 如果該學校還有名額
                school_assign_list[school_id].append(student_id)  # 把學生加入學校分配名單
                for i in range(len(school_quota_left)):  # 名額減一
                    if school_quota_left[i][0] == school_id:
                        school_quota_left[i][1] -= 1
                        break
                queue.pop(0)  # 從 band 移除該學生
            else:  # 如果該學校已滿
                students_data[student_id]['choice'] += 1  # 學生選擇下一個志願
                queue.append(queue.pop(0))  # 把學生放到 band 的最後
                
    print("開始處理 band1")        
    process_band(band1)
    print("完成處理 band1\n")
    print("開始處理 band2")
    process_band(band2)
    print("完成處理 band2\n")
    print("開始處理 band3")
    process_band(band3)
    print("完成處理 band3\n")
    # 輸出無法分配的學生
    if cant_assign:
        print("以下學生無法分配到任何學校:")
        for i in range(len(cant_assign)):
            print(f"學生 ID: {cant_assign[i]}, 姓名: {students_data[cant_assign[i]]['name']}")
    # 將分配結果寫入檔案

def write_assign_to_file():
    print("寫入分配結果到檔案")
    f = open('assign.csv', 'w')  # 開啟檔案
    f.write("school_id,student_id\n")
    for school_id, students in school_assign_list.items(): 
        f.write(f"{school_id}") 
        for student_id in students: # 將學生 ID 寫入檔案
            f.write(f",{student_id}")
        f.write("\n")
    f.close()
    
    print("寫入完成\n")
    print("請查看 assign.csv 檔案\n")
    

def find_student_school(student_id):
    f = open('assign.csv', 'r') # 開啟檔案
    assign_data = f.readlines()  # 讀取檔案內容
    f.close()
    
    for i in range(1, len(assign_data)):  # 跳過標題行
        data = assign_data[i].strip().split(',') # 分割成列表
        school_id = data[0] # 提取學校 ID
        students = data[1:] 
        for j in range(len(students)):
            if student_id == students[j]:
                return school_id
    return None  # 如果未找到學生，返回 None


def search_ss_school(ss_id):
    school_id = find_student_school(ss_id)
    if school_id is None:
        messagebox.showerror("錯誤", f"學生 ID {ss_id} 未找到或未分配到任何學校。")
    else:    
        school.config(text=f"分配到學校: {school_id}")
        ssid.config(text=f"學生 ID: {ss_id}")
        ss_name.config(text=f"姓名: {students_data[ss_id]['name']}")
        ss_total_score.config(text=f"總分: {students_data[ss_id]['total_score']}")
        ss_choice.config(text=f"志願: {students_data[ss_id]['choice'] + 1}")


def main():
    
    try:        
        input_school_data()
        input_student_data()
        if verify_data():
            print("所有資料驗證通過\n")
            calculate_score()
            assign_student()
            assign_school()
            write_assign_to_file()
            assign_button.config(state=tk.DISABLED, text='分配完成', background='#D3D3D3',cursor='arrow')  # 禁用分配按鈕
            check_button.config(state=tk.NORMAL, cursor='hand2', background='#ADD8E6')  # 啟用查詢按鈕
            open_button.config(state=tk.NORMAL,cursor='hand2', background='#FFD700') # 啟用打開檔案按鈕

        else:
            print("資料驗證失敗\n")
            messagebox.showerror("錯誤", "資料驗證失敗，請查看控制台輸出以獲取更多信息。")
    
    except Exception as e:
        print(f"發生錯誤: {e}")
        messagebox.showerror("錯誤", f"發生錯誤: {e}")
        
        
# ****************************
# 打開檔案對話框
def open_school_file():
    global school_file_path
    school_file_path = filedialog.askopenfilename(title="選擇學校資料檔案", filetypes=[("CSV files", "*.csv")])
    school_file_button.config(text=os.path.basename(school_file_path))
    if school_file_path != "":
        print(f"已匯入學校資料檔案: {school_file_path}")
    else:
        print("未選擇學校資料檔案")
def open_student_file():
    global student_file_path
    student_file_path = filedialog.askopenfilename(title="選擇學生資料檔案", filetypes=[("CSV files", "*.csv")])
    ss_file_button.config(text=os.path.basename(student_file_path))
    if student_file_path != "":
        print(f"已匯入學生資料檔案: {student_file_path}")
    else:
        print("未選擇學生資料檔案")

top = tk.Tk()
# 設定視窗標題
top.title("中學學位自行分配學位系統")
top.geometry("1200x800")
top.resizable(False, False)
# 大標題
title = tk.Label(top, text="中學學位自行分配學位系統", font=("Arial", 24), pady=20)


# 匯入檔案
text0 = tk.Label(top, text='1. 請匯入學校資料檔案和學生資料檔案', font=("Arial", 20), pady=10)
school_file_button = tk.Button(top, text="匯入學校資料檔案", command=open_school_file, font=("Arial", 14), background='#D3D3D3', cursor='arrow', padx=15, pady=8)
ss_file_button = tk.Button(top, text="匯入學生資料檔案", command=open_student_file, font=("Arial", 14), background='#D3D3D3', cursor='arrow', padx=15, pady=8)


# 分配功能
text1 = tk.Label(top, text='2. 按下按鈕進行分配', font=("Arial", 20), pady=10)
assign_button = tk.Button(top, text="開始分配", command=main, font=("Arial", 14), background='#90EE90',cursor='hand2', padx=15, pady=8)


# 查詢功能
text2 = tk.Label(top, text='3. 輸入學生 ID 進行查詢', font=("Arial", 20), pady=10)
entry = tk.Entry(top, font=("Arial", 16), width=30, justify='center')
check_button = tk.Button(top, text="查詢學生分配", command=lambda: search_ss_school(entry.get()), font=("Arial", 14), background='#D3D3D3', cursor='arrow',state=tk.DISABLED, padx=15, pady=8)
open_button = tk.Button(top, text="打開分配結果檔案", command=lambda: os.startfile('assign.csv'), font=("Arial", 14), background='#D3D3D3', cursor='arrow', state=tk.DISABLED, padx=15, pady=8)


# 顯示學生資料
group = tk.LabelFrame(top, text="學生資料", font=("Arial", 16), padx=10, pady=10)
ssid = tk.Label(group, text="學生 ID", font=("Arial", 14))
school = tk.Label(group, text="分配到學校", font=("Arial", 14))
ss_name = tk.Label(group, text="姓名", font=("Arial", 14))
ss_total_score = tk.Label(group, text="總分", font=("Arial", 14))
ss_choice = tk.Label(group, text="志願", font=("Arial", 14))



# 包裝界面
title.pack()
text0.pack()
school_file_button.pack()
ss_file_button.pack()
text1.pack()
assign_button.pack()
text2.pack()
entry.pack()
check_button.pack()
open_button.pack()

ssid.grid(row=0, column=0, padx=5, pady=5, sticky='w')
ss_name.grid(row=1, column=0, padx=5, pady=5, sticky='w')
school.grid(row=2, column=0, padx=5, pady=5, sticky='w')
ss_total_score.grid(row=5, column=0, padx=5, pady=5, sticky='w')
ss_choice.grid(row=7, column=0, padx=5, pady=5, sticky='w')
group.pack()

top.mainloop()
    

