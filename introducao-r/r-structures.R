library("tidyverse")

# Ver estatisticas do dataset
summary(mpg)

sd(mpg$hwy)

# Calcula com NA, exceto quando o na.rm esta explicitado
idades <- c(27, 23, NA)
mean(idades, na.rm = TRUE)
sd(idades, na.rm = TRUE)

# Criacao de funcao
media <- function(arr) {
  c <- 0
  s <- 0
  for (v in arr) {
    if (!is.na(v)) {
      s <- s + v
      c <- c + 1
    }
  }
  s / c
}

media(idades)

# Iteracao com While
i <- 0
while (i < 10) {
  i <- i + 1
  print(i)
}

# Criacao de lista/vetor
# Vetor precisa ser do mesmo tipo de dado - senao as informacoes serao convertidas
c("0", 1, 2)

# Lista pode ter tipos diferentes
a <- list("0", 1, 3)

pessoa <- list(
  nome=c("Leonardo", "Maria"),
  idade=c(27, 23)
)

pessoa$nome
