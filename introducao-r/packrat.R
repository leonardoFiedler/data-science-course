install.packages("packrat")

# importa a lib do packrat
library(packrat)
# Inicia um virtual environment
packrat::init()

# Obtem todas as dependencias instaladas no computador
packrat::snapshot()