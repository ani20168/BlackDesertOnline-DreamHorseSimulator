import random
import os
import msvcrt

# 讓使用者輸入材料
def input_materials():
    while True:
        materials = input("請輸入「石尾碎草」、「微風海螺海藻」、「純淨的森林氣息」數量，用空格分開(EX:80 80 40):")
        # 分割材料並轉換成數字
        materials = materials.split()

        try:
            materials = [int(float(x)) for x in materials]
        except ValueError:
            print("錯誤，請重新輸入材料數量")
            continue


        if len(materials) != 3 or sum(materials) != 200 or any(material > 180 for material in materials):
            print("請輸入3種材料，共200個，單種材料最多180個")
            continue
        else:
            return materials

#每種馬的機率
def calculate_horse_probability(materials):
    total_weight = sum(materials)
    probability_flying_horse = materials[0] / total_weight
    probability_unicorn = materials[1] / total_weight
    probability_hell_horse = materials[2] / total_weight

    print("飛馬的機率: {:.0%}".format(probability_flying_horse))
    print("獨角獸的機率: {:.0%}".format(probability_unicorn))
    print("地獄馬的機率: {:.0%}".format(probability_hell_horse))
    return probability_flying_horse, probability_unicorn, probability_hell_horse

#歐洲人篩選
def awaken_horse(probability_flying_horse, probability_unicorn, probability_hell_horse):
    # 初始化變量
    success_rate = 0.01  # 成功率，初始值為1%
    layer = 0  # 層數，初始值為0

    # 重複直到覺醒成功為止
    while True:
        # 顯示訊息並等待使用者的輸入
        print("目前成功率為{:.1f}%(+{})，按下y確定覺醒:".format(success_rate * 100, layer))
        response = msvcrt.getch().decode()
        
        # 如果使用者按下y，則進行計算
        if response == "y":
            # 使用隨機數生成器生成一個0到1之間的小數
            rand = random.random()

            # 如果隨機數小於成功率，則覺醒成功
            if rand < success_rate:
                # 使用隨機數生成器生成一個0到1之間的小數，用於決定覺醒的馬種
                rand = random.random()
                # 如果隨機數小於飛馬的機率，則覺醒成功
                if rand < probability_flying_horse:
                    print("覺醒成功！您覺醒了一匹飛馬！")
                    # 如果隨機數在飛馬的機率和獨角獸的機率之間，則覺醒成功
                elif rand < probability_flying_horse + probability_unicorn:
                    print("覺醒成功！您覺醒了一匹獨角獸！")
                    # 否則，覺醒成功
                else:
                    print("覺醒成功！您覺醒了一匹地獄馬！")
                        
                break
            else:
                # 否則，失敗次數+1，成功率和層數也增加
                layer += 1
                success_rate += 0.002

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    materials = input_materials()
    horse_probability = calculate_horse_probability(materials)
    awaken_horse(horse_probability[0],horse_probability[1],horse_probability[2])
    # 等待使用者輸入
    print("按下y以外的任意鍵結束程式，或按r重新輸入材料: ")
    while True:
        choice = msvcrt.getch().decode()
        if choice == 'r':
            break
        elif choice == 'y':
            continue
        else:
            exit()


