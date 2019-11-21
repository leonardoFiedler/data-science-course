library("tidyverse")

tabela <- tribble(
  ~nome, ~idade, ~sobrenome,
  "Leonardo", 23, "Fiedler",
  "Maria", 18, "Da Silva"
)

# Gerar numeros aleatorios
runif(0, 5)

#Leitura de CSV
read.csv("~/Desktop/data-science-course/introducao-python/household_power_consumption.txt",
         nrows = 10000,
         na.strings = c("?"),
         sep = ";")

#mpg - dataset de exemplo, consiste do consumo de gasolina de automoveis.
# O que esta dentro do aes e atributo do mpg - pode ser consultado usando somente o comando mpg
ggplot(mpg, aes(x = cyl, y = hwy)) + 
  geom_point()

ggplot(mpg) + 
  geom_point(aes(x = cyl, y = hwy))

ggplot(mpg, aes(x = manufacturer)) + 
  geom_bar()

ggplot(mpg, aes(displ, hwy)) + 
  geom_point(aes(color=drv))

# Listar dados de uma coluna
mpg$drv
mpg["drv"]

ggplot(mpg, aes(displ, hwy)) + 
  geom_point(aes(color=drv)) +
  geom_smooth(se = FALSE) +
  labs(
    title = "Um grafico"
  )

ggplot(mpg, aes(displ, hwy)) +
  geom_point() + 
  facet_wrap(~drv)

ggplot(mpg, aes(displ, hwy)) +
  geom_point(aes(color = manufacturer)) +
  facet_grid(drv ~ year)


# Sintaxe maior de linguagem funcional
mpg %>%
  ggplot(aes(displ, hwy)) + 
  geom_point()
