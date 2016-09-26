F_users_h = open('C:\\Users\\RETELLIGENCE\\Desktop\\WADING\\DB_iwen\\WAD_id_WAD_pw(s).txt', 'w')

for i in range(999999):
    app = '[s01-'
    appp = str(i)
    apppp = 10-len(appp)
    zipcode = 'kr1'
    wad_pw = '-[000000]'
    app = app+('0'*apppp)+appp+'-'+zipcode+']'+wad_pw
    
    F_users_h.write(app)
    F_users_h.write('\n')
    

print("done")
