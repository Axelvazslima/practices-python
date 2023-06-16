m_antiga = input()

m_nova = '1'
for i in range(1, 8):
    m_nova += m_antiga[i]
    if i == 4:
        m_nova += '0'

print(m_nova)
