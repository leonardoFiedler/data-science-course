library("tidyverse")

# Obtém apenas algumas colunas (manufacturer e model)
mpg %>%
  select(manufacturer, model) %>%
  filter(model == "a4")

# Operador AND
mpg %>%
  filter(model == "a4", displ > 2)


# Operador OR
mpg %>%
  filter(model == "a4" | displ > 2)

mpg %>%
  filter(year == 1999) %>%
  select(manufacturer, displ) %>%
  View()


mpg %>%
  filter(year == 1999) %>%
  ggplot(aes(displ, hwy)) +
  geom_point()


mpg %>%
  arrange(model, manufacturer)

mpg %>%
  filter(
    between(displ, 1.5, 2.5)
  )

mpg %>%
  filter(drv %in% c("f", "r") )

#If modo
5 %/% 4

# Permite alterar e calcular novos valores em colunas
mpg %>%
  transmute(
    ratio = hwy / cty,
    hwy = hwy,
    cty = cty,
    ratio_2 = ratio * 2
  )

# Remove a coluna com o operador "-"
mpg %>%
  select(-year, -trans)

# Adiciona novas colunasg
mpg %>%
  mutate(
    ratio = hwy / cty,
    ratio_2 = ratio * 2
  )

mpg %>%
  count(manufacturer) %>%
  arrange(-n) %>%
  top_n(5)


mpg %>%
  group_by(model) %>%
  summarise(
    hwy_medio = mean(hwy),
    cty_medio = mean(cty)
  )

#Transforma os dados de linhas para colunas
mpg %>%
  count(manufacturer) %>%
  spread(manufacturer, n) %>%
  View()

mpg %>%
  count(year) %>%
  spread(year, n) %>%
  gather(`1999`, `2008`,
         key = "year",
         value = "n") %>%
  View()
