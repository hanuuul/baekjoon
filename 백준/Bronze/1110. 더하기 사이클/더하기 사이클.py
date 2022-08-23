num = input()
cnt = 0

if int(num) < 10:
    num = '0' + num

new = num

while(True):
    sumn = str(int(new[0]) + int(new[1]))
    if int(sumn) < 10:
        sumn = '0' + sumn
    new = new[1] + sumn[1]
    cnt += 1
    if num == new:
        break

print(cnt)