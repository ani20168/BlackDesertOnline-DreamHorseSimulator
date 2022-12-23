import random
# 讓使用者輸入材料
def input_materials():
    while True:
        materials = input("請輸入「石尾碎草」、「微風海螺海藻」、「純淨的森林氣息」數量，用空格分開(EX:80 80 40):")
        # 分割材料並轉換成數字
        materials = materials.split()
        materials = [int(x) for x in materials]

        # 判斷材料總和是否為200
        if sum(materials) != 200:
            print("材料須為200")
        # 判斷單種材料是否超過180
        elif any(material > 180 for material in materials):
            print("輸入的材料過多")
        # 如果材料符合條件，則退出迴圈
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
        response = input("目前成功率為{:.1f}%(+{})，按下y確定覺醒:".format(success_rate * 100, layer))

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
        else:
            # 如果使用者沒有按下y，則繼續等待輸入
            continue

while True:
    materials = input_materials()
    horse_probability = calculate_horse_probability(materials)
    awaken_horse(horse_probability[0],horse_probability[1],horse_probability[2])
    # 等待使用者輸入
    choice = input("按下任意鍵結束程式，或按r重新輸入材料: ")
    if choice != 'r':
        break

