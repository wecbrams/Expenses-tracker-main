fn = open('Codingal.txt', 'r')
fn1 = open('CodingalUpdated.txt', 'w')
cont = fn.readlines()
for i in range(len(cont)):
    if i % 2 == 0:   
        fn1.write(cont[i])
fn1.close()
fn1 = open('CodingalUpdated.txt', 'r')

print(fn1.read())

fn.close()
fn1.close()