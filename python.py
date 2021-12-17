KT = []
R_TYPE = {'A': 200000, 'B': 150000, 'C': 100000}


def add():
    while True:
        name = input("Ten KT: ").title()
        day = int(input("So Ngay Thue: "))
        r_type = input("Loai Phong: ").upper()

        if name and day > 0 and r_type in R_TYPE:
            KT.append({
                "name": name,
                "day": day,
                "r_type": r_type
            })
        else:
            print("Dau vao khong hop le. Vui long thu lai:")
            continue

        yn = input("Nhap Tiep (Y/N): ").lower()

        if yn == 'n':
            break
        
        print()

def cost_pd(r_type):
    return R_TYPE.get(r_type)


def cost_pc(day, r_type):
    return R_TYPE.get(r_type)*day


def prt():
    print('{:<20}\t{:<12}\t{:<10}\t{:<10}'
          .format('Ten Khach Hang', 'So Ngay Thue', 'Loai Phong', 'Tien Thue'))

    for kt in KT:
        print('{:<20}\t{:<12}\t{:<10}\t{:<10}'
              .format(*kt.values(), cost_pc(kt.get('day'), kt.get('r_type'))))


def exp_f():
    with open('baiso2.txt', 'w') as F:
        for kt in KT:
            print(*kt.values(), cost_pc(kt.get('day'),
                                        kt.get('r_type')), sep='\t', file=F)


add()
prt()
exp_f()
