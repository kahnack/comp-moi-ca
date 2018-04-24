# Création :
# ROBIN Jimmy et APRIN Florian

########################
### Comp'moi ça ###
########################

# Comparaison de 2 fichiers venant de BATCH Cobol

# fonctionnalitée à implanter :
# - 
# - 
# - 
# - 


# Maintenance :


### Importation
from COMP-MOI-CA_data import *




name_F1 = verif_fichier(1)
fichier1 = open(name_F1,'r')

name_F2 = verif_fichier(2)
fichier2 = open(name_F2,'r')

name_F3 = verif_fichier(3)
fichier3 = open(name_F3,'w')



        
""" construction du cartouche du fichier resultat """
fichier3.write(cartouche(name_F1,1))
fichier3.write(cartouche(name_F2,2))


a = fichier1.readline()
b = fichier2.readline()

"""boucle de comparaison de chaque ligne"""
### TODO : gérer des fichier avec des nombre d'enreg differents

while (a!='' and b!=''):
    print('rpout')
    for i in comparer(a,b):
        fichier3.write(i+'\n')
    a = fichier1.readline()
    b = fichier2.readline()

    

fichier3.close()


prout = "Caca"
printf('Je suis immature')












    
    
