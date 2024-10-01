# %%
# À ex'écuter en premier
import numpy as np

# %% [markdown]
# # Niveau 1 : Création de tableaux simples

# %% [markdown]
# ## Exercices 1.1.	Créer un tableau de 5 zéros
#
# Compléter la fonction `create_zeros` pour qu'elle retourne un tableau de 5 éléments égaux à 0.


# %%
def create_zeros():
    return np.zeros(5)


print(create_zeros())  # attendu: [0. 0. 0. 0. 0.]

# %% [markdown]
# ## Exercices 1.2.	Créer un tableau de 5 uns
#
# Compléter la fonction `create_ones` pour qu'elle retourne un tableau de 5 éléments égaux à 1.


# %%
def create_ones():
    return np.ones(5)


print(create_ones())  # attendu: [1. 1. 1. 1. 1.]

# %% [markdown]
# ## Exercices 1.3.	Créer un tableau contenant les entiers de 10 à 50
#
# Compléter la fonction `create_range` pour qu'elle retourne un tableau contenant les entiers de 10 à 50 inclus.


# %%
def create_range():
    return np.arange(10,51)


print(create_range())  # attendu: [10 11 12 13 14 15 16 17 ...] (jusqu'à 50 inclus)

# %% [markdown]
# ## Exercices 1.4.	Créer une matrice identité 3x3
#
# Compléter la fonction `create_identity` pour qu'elle retourne une matrice identité de taille 3x3.


# %%
def create_identity():
    return np.eye(3)


print(create_identity())  # attendu: [[1. 0. 0.]
#                                     [0. 1. 0.]
#                                     [0. 0. 1.]]

# %% [markdown]
# ## Exercices 1.5.	Créer un tableau 2D de forme (3,3) rempli de nombres aléatoires entre 0 et 1
#
# Compléter la fonction `create_random` pour qu'elle retourne un tableau 2D de forme (3,3) rempli de nombres aléatoires entre 0 et 1.


# %%
def create_random():
    return np.random.uniform(0,1,size=(3,3))


print(create_random())  # attendu: un tableau 3x3 de valeurs aléatoires entre 0 et 1

# %% [markdown]
# # Niveau 2 : Vectorisation

# %% [markdown]
# ## Exercices 2.1.	Créer une fonction qui ajoute 5 à chaque élément d'un tableau
#
# Compléter la fonction `add_five` pour qu'elle retourne un tableau contenant les éléments du tableau d'entrée augmentés de 5.


# %%
def add_five(arr):
    return np.add(5,arr)


print(add_five(np.array([1, 2, 3, 4, 5])))  # attendu: [6 7 8 9 10]

# %% [markdown]
# ## Exercices 2.2.	Créer une fonction qui met chaque élément d'un tableau au carré
#
# Compléter la fonction `square` pour qu'elle retourne un tableau contenant les éléments du tableau d'entrée mis au carré.


# %%
def square(arr):
    return np.power(arr,2)


print(square(np.array([1, 2, 3, 4, 5])))  # attendu: [ 1  4  9 16 25]

# %% [markdown]
# ## Exercices 2.3.	Créer un tableau contenant les valeurs de $\sin$ pour les nombres de 0 à 2π (inclus) avec un pas de 0.1
#
# Compléter la fonction `sin_values` pour qu'elle retourne un tableau contenant les valeurs de $\sin$ pour les nombres de 0 à 2π (inclus) avec un pas de 0.1.


# %%
def sin_values():
    return np.sin(np.arange(0,2*np.pi+0.1,0.1))

print(
    sin_values()
)  # attendu: un tableau de valeurs de sin(0), sin(0.1), sin(0.2), ... sin(2π)


# %% [markdown]
# ## Exercices 2.4.	Ré-écriture sous forme vectorisée (1/2)
#
# Compléter la fonction `f_vectorized` pour qu'elle effectue la même opération que la fonction `f` donnée ci-dessous, mais sans utiliser de boucle `for`.


# %%
def f(arr1, arr2):
    result = np.zeros(arr1.shape)
    for i in range(len(arr1)):
        result[i] = 2 * arr1[i] + 3 * arr2[i]
    return result


def f_vectorized(arr1, arr2):
    return np.add(2*arr1,3*arr2)



print(
    f_vectorized(np.array([5, 4, 3, 2, 1]), np.array([1, 2, 3, 4, 5]))
)  # attendu: [13 14 15 16 17]

# %% [markdown]
# ## Exercices 2.5.	Ré-écriture sous forme vectorisée (2/2)
#
# Compléter la fonction `g_vectorized` pour qu'elle effectue la même opération que la fonction `g` donnée ci-dessous, mais sans utiliser de boucle `for`.


# %%
def g(x):
    result = np.zeros_like(x)
    for i in range(len(x)):
        if x[i] > 0:
            result[i] = x[i] ** 2
        else:
            result[i] = x[i]
    return result


def g_vectorized(x):
    return np.where(x > 0, x**2, x)

print(g_vectorized(np.array([1, -2, 3, -4, 5])))  # attendu: [ 1 -2  9 -4 25]

# %% [markdown]
# # Niveau 3 : Indexation et slicing

# %% [markdown]
# ## Exercices 3.1.	Sélectionner les éléments pairs d'un tableau
#
# Compléter la fonction `select_even` pour qu'elle retourne un tableau contenant les éléments pairs du tableau d'entrée.


# %%
def select_even(arr):
    T=[]
    for x in arr:
        if x%2==0:
            T.append(x)
    return T


print(
    select_even(np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
)  # attendu: [ 2  4  6  8 10]

# %% [markdown]
# ## Exercices 3.2.	Remplacer les valeurs négatives d’un tableau par 0
#
# Compléter la fonction `replace_negatives` pour qu'elle retourne un tableau contenant les mêmes éléments que le tableau d'entrée, sauf que les valeurs négatives sont remplacées par 0.


# %%
def replace_negatives(arr):
    for i in range(len(arr)):
        if arr[i]<0:
            arr[i]=0
    return arr





print(replace_negatives(np.array([1, -2, 3, -4, 5])))  # attendu: [1 0 3 0 5]

# %% [markdown]
# ## Exercices 3.3.	Créer une fonction qui, étant donné un tableau 2D de dimensions >1, retourne la sous-matrice obtenue en enlevant la première et la dernière ligne et colonne
#                   (on "rogne" la matrice tout autour)
#
# Compléter la fonction `get_center` pour qu'elle retourne la sous-matrice obtenue en enlevant la première et la dernière ligne et colonne du tableau d'entrée.


# %%
def get_center(arr):
    X=np.zeros((len(arr)-2,len(arr)-2))
    for i in range(len(X)):
        for j in range(len(X)):
            X[i,j]=arr[i+1,j+1]
    return X


print(get_center(np.arange(1, 26).reshape(5, 5)))  # attendu: [[ 7  8  9]
#               [12 13 14]
#               [17 18 19]]

# %% [markdown]
# ## Exercices 3.4.	Créer une fonction qui, étant donné un tableau 2D avec au moins 2 lignes, échange ses deux premières lignes
#
# Compléter la fonction `swap_first_rows` pour qu'elle retourne le tableau d'entrée avec ses deux premières lignes échangées.


# %%
def swap_first_rows(arr):
    a=arr[0].copy()
    arr[0]=arr[1]
    arr[1]=a
    return arr



print(swap_first_rows(np.array([[1, 2], [3, 4], [5, 6]])))  # attendu: [[3 4]
#                                                                       [1 2]
#                                                                       [5 6]]

# %% [markdown]
# ## Exercices 3.5.	Créer une fonction qui, étant donné un tableau 2D, retourne une matrice "damier" contenant les valeurs suivantes:
# - pour les éléments de lignes et colonnes paires, la valeur de l'indice de ligne + 1
# - pour les éléments de lignes et colonnes impaires, la valeur 1
# - 0 pour tous les autres éléments
#
# Compléter la fonction `funny_checkerboard` pour qu'elle retourne une matrice "damier" contenant les valeurs décrites ci-dessus.


# %%
def funny_checkerboard(size):
    X=np.zeros((size,size))
    for i in range(len(X)):
        for j in range(len(X)):
            if i%2==0 and j%2==0:
                X[i,j]=i+1
            elif i%2==1 and j%2==1:
                X[i,j]=1
    return X


print(funny_checkerboard(5))  # attendu: [[1. 0. 1. 0. 1.]
#                                         [0. 1. 0. 1. 0.]
#                                         [3. 0. 3. 0. 3.]
#                                         [0. 1. 0. 1. 0.]
#                                         [5. 0. 5. 0. 5.]]


# %% [markdown]
# # Niveau 4 : Fonctions d’agrégation

# %% [markdown]
# ## Exercices 4.1.	Créer une fonction qui, étant donné un tableau 2D, retourne la moyenne de ses éléments
#
# Compléter la fonction `mean` pour qu'elle retourne la moyenne des éléments du tableau d'entrée.


# %%
def mean(arr):
    s1=0
    s2=0
    for i in range(len(arr)):
        for j in range(len(arr)):
            s1+=arr[i,j]
            s2+=1
    return s1/s2 


# %% [markdown]
# ## Exercices 4.2.	Créer une fonction qui, étant donné un tableau 2D, retourne la somme de ses éléments des colonnes d'indice impair
#
# Compléter la fonction `sum_odd_columns` pour qu'elle retourne la somme des éléments des colonnes d'indice impair du tableau d'entrée.


# %%
def sum_odd_columns(arr):
    s=0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if j%2==1:
                s+=arr[i,j]
    return s


print(sum_odd_columns(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])))  # attendu: 15

# %% [markdown]
# ## Exercices 4.3.	Créer une fonction qui, étant donné un tableau 2D, retourne l'élément maximal de chaque ligne
#
# Compléter la fonction `max_per_line` pour qu'elle retourne un tableau contenant l'élément maximal de chaque ligne du tableau d'entrée.
# Le tableau ne doit pas être vide.


# %%
def max_per_line(arr):
    T=[]
    for x in arr:
        T.append(np.max(x))
    return T 


print(max_per_line(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])))  # attendu: [3 6 9]

# %% [markdown]
# ## Exercices 4.4.
#
# Compléter la fonction `min_per_column` pour qu'elle retourne un tableau contenant l'élément minimal de chaque colonne du tableau d'entrée.


# %%
def min_per_column(arr):
    A=np.zeros((arr.shape[1],arr.shape[0]))
    for i in range(arr.shape[1]):
        for j in range(arr.shape[0]):
            A[i,j]=arr[j,i]
    T=[]
    for x in A:
        T.append(np.min(x))
    return T 
    




print(min_per_column(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])))  # attendu: [1 2 3]
