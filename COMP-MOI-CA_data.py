# Création :
# ROBIN Jimmy
###comtest
########################
### Nom du programme ###
########################

# 
# fonctionnalitée à implanter :
# - 
# - 
# - 
# - 


# Maintenance :

## Variables
directory = 'files\\'
extension = '.txt'


## Demande à l'utilisateur un nom de fichier
## si il existe : ouverture
## sinon : possibilité de le créer/remplir

def verif_fichier(num_fichier):
    global directory, extension
    name_file = input('Entrer le nom du fichier {0} >'.format(num_fichier))
    
    name_file_comp = directory + name_file + extension
    
    if existe(name_file_comp):
        return name_file_comp
    else:
        print("Le fichier n'existe pas.... connard")
        verif_fichier(num_fichier)
##        bool_creation = input("Le fichier n'existe pas, veux tu le créer ? (y/yes, n/no)")
##        if bool_creation in ('y', 'yes'):
##            fichier1 = open(name_file_comp,'w')
##            print("fichier créer")
##            ecriture(fichier1)
##            print('Fichier {0} créé et écrit'.format(num_fichier))
##            return name_file_comp
##        else:
##            print('fichier non créé')
##            verif_fichier(num_fichier) 



##
## ecrit les premier ligne du fichier resultat contenant les nom fichier et le nombre de lignes
##

def cartouche(name_file,num):
    global directory, extension
    my_str_2 = ''
    for i in range(len(directory),(len(name_file)-len(extension))):
        my_str_2 += name_file[i]
    nb = 0
    with open(name_file,'r') as f:
        for line in f:
            nb += 1
    my_str = 'Fichier N°' + str(num) + ' : ' + my_str_2 + ', Nb ligne : ' + str(nb) + '\n'
    print(my_str)
    return my_str





##
## Test si le fichier existe
##

def existe(nom_fichier):
    try:
        f = open(nom_fichier,'r')
        f.close()
        return True
    except:
        return False


##
## Compare chaque caractère de 2 ligne
##

def comparer(ligne1,ligne2):
    "compare chaque caratère de 2 lignes, créer 2 clones avec juste les diffs"

    # LF1 = ligne fichier 1, avec space si caractère identique
    LF1,LF2,num = '','',0

    for i in ligne1:
        if i =='\n':
            LF1 += ' '
            LF2 += ' '
        elif i == ligne2[ligne1.find(i)]:
            #print('identique : %c et %c' %(i, ligne2[ligne1.find(i)]))
            LF1 += '#'
            LF2 += '#'
        else:
            #print('different : %c et %c' %(i, ligne2[ligne1.find(i)]))
            LF1 += i
            LF2 += ligne2[ligne1.find(i)]

    #print(LF1)
    #print(LF2)
    return (LF1,LF2)














    
    
